"""
Analyze patterns between audio features and TikTok performance
Discover what actually drives virality
"""

import pandas as pd
import numpy as np
from scipy.stats import spearmanr, pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

WICKED_COLORS = {
    'emerald': '#00A86B',
    'pink': '#E91E8C',
    'black': '#1C1C1C',
    'gold': '#FFD700',
    'light_green': '#90EE90'
}

def load_data():
    """Load Spotify and TikTok data"""
    spotify = pd.read_csv('../data/spotify/wicked_audio_features.csv')
    
    try:
        tiktok = pd.read_csv('../data/tiktok/wicked_tiktok_performance.csv')
        print("Loaded actual TikTok data")
    except:
        tiktok = pd.read_csv('../data/tiktok/wicked_tiktok_performance_EXAMPLE.csv')
        print("Using example TikTok data - replace with real data for final analysis!")
    
    return spotify, tiktok

def merge_data(spotify, tiktok):
    """Merge Spotify features with TikTok performance"""
    merged = spotify.merge(tiktok, left_on='track_name', right_on='song_name', how='inner')
    
    merged['virality_score'] = (
        (merged['tiktok_video_count'] / merged['tiktok_video_count'].max()) * 50 +
        (merged['tiktok_view_estimate_millions'] / merged['tiktok_view_estimate_millions'].max()) * 30 +
        (merged['weeks_trending'] / merged['weeks_trending'].max()) * 20
    ).round(2)
    
    merged['virality_rank'] = merged['virality_score'].rank(ascending=False).astype(int)
    
    return merged

def analyze_feature_correlations(df):
    """Analyze which audio features correlate with virality"""
    audio_features = ['energy', 'danceability', 'valence', 'tempo', 
                     'acousticness', 'speechiness', 'loudness', 'duration_min']
    
    correlations = []
    for feature in audio_features:
        spearman_corr, spearman_p = spearmanr(df[feature], df['virality_score'])
        pearson_corr, pearson_p = pearsonr(df[feature], df['virality_score'])
        
        correlations.append({
            'feature': feature,
            'spearman_correlation': spearman_corr,
            'spearman_pvalue': spearman_p,
            'pearson_correlation': pearson_corr,
            'pearson_pvalue': pearson_p,
            'significant': 'Yes' if spearman_p < 0.05 else 'No'
        })
    
    corr_df = pd.DataFrame(correlations).sort_values('spearman_correlation', ascending=False, key=abs)
    return corr_df

def analyze_content_types(df):
    """Analyze which content types performed best"""
    content_performance = df.groupby('primary_trend_type').agg({
        'virality_score': ['mean', 'count'],
        'tiktok_video_count': 'sum',
        'weeks_trending': 'mean'
    }).round(2)
    
    content_performance.columns = ['avg_virality_score', 'num_songs', 'total_videos', 'avg_weeks_trending']
    content_performance = content_performance.sort_values('avg_virality_score', ascending=False)
    
    return content_performance

def find_surprising_results(df):
    """Find songs that defied audio feature expectations"""
    df['expected_virality'] = (
        df['energy'] * 0.3 +
        df['danceability'] * 0.3 +
        df['valence'] * 0.2 +
        (1 - df['acousticness']) * 0.2
    ) * 100
    
    df['surprise_factor'] = df['virality_score'] - df['expected_virality']
    
    overperformers = df.nlargest(3, 'surprise_factor')[['track_name', 'expected_virality', 'virality_score', 'surprise_factor', 'viral_moment']]
    underperformers = df.nsmallest(3, 'surprise_factor')[['track_name', 'expected_virality', 'virality_score', 'surprise_factor', 'notes']]
    
    return overperformers, underperformers

def identify_key_insights(df, correlations):
    """Generate key insights from the data"""
    insights = []
    
    most_viral = df.loc[df['virality_score'].idxmax()]
    insights.append({
        'insight': 'Most Viral Song',
        'finding': f"{most_viral['track_name']} - {most_viral['tiktok_video_count']:,} videos",
        'why': most_viral['viral_moment']
    })
    
    top_corr = correlations.iloc[0]
    insights.append({
        'insight': 'Most Important Audio Feature',
        'finding': f"{top_corr['feature']} (correlation: {top_corr['spearman_correlation']:.3f})",
        'why': 'Strongest correlation with viral success'
    })
    
    df['surprise_rank'] = (df['virality_rank'] - df['expected_virality'].rank(ascending=False)).abs()
    surprise_hit = df.loc[df['surprise_rank'].idxmax()]
    insights.append({
        'insight': 'Biggest Surprise Hit',
        'finding': f"{surprise_hit['track_name']}",
        'why': surprise_hit['viral_moment']
    })
    
    content_perf = analyze_content_types(df)
    top_content = content_perf.index[0]
    insights.append({
        'insight': 'Most Successful Content Type',
        'finding': top_content,
        'why': f"Average virality score: {content_perf.iloc[0]['avg_virality_score']:.1f}"
    })
    
    celebrity_songs = df[df['celebrity_boost'].str.contains('Ariana|Jonathan', na=False)]
    if not celebrity_songs.empty:
        avg_celeb = celebrity_songs['virality_score'].mean()
        avg_no_celeb = df[~df['celebrity_boost'].str.contains('Ariana|Jonathan', na=False)]['virality_score'].mean()
        insights.append({
            'insight': 'Celebrity Boost Effect',
            'finding': f"Songs with major celebrity boost: {avg_celeb:.1f} vs {avg_no_celeb:.1f}",
            'why': f"{(avg_celeb - avg_no_celeb):.1f} point increase in virality score"
        })
    
    return pd.DataFrame(insights)

def main():
    print("\n" + "="*70)
    print("WICKED RETROSPECTIVE ANALYSIS - PATTERN ANALYSIS")
    print("="*70)
    
    print("\nLoading data...")
    spotify, tiktok = load_data()
    
    print("Merging datasets...")
    df = merge_data(spotify, tiktok)
    
    print("\nAnalyzing audio feature correlations...")
    correlations = analyze_feature_correlations(df)
    
    print("Analyzing content type performance...")
    content_performance = analyze_content_types(df)
    
    print("Finding surprising results...")
    overperformers, underperformers = find_surprising_results(df)
    
    print("Generating key insights...")
    insights = identify_key_insights(df, correlations)
    
    df.to_csv('../data/processed/merged_analysis.csv', index=False)
    correlations.to_csv('../outputs/tables/feature_correlations.csv', index=False)
    content_performance.to_csv('../outputs/tables/content_type_performance.csv', index=False)
    insights.to_csv('../outputs/tables/key_insights.csv', index=False)
    
    print("\n" + "="*70)
    print("FEATURE CORRELATIONS WITH VIRALITY")
    print("="*70)
    print(correlations.to_string(index=False))
    
    print("\n" + "="*70)
    print("CONTENT TYPE PERFORMANCE")
    print("="*70)
    print(content_performance)
    
    print("\n" + "="*70)
    print("KEY INSIGHTS")
    print("="*70)
    for idx, row in insights.iterrows():
        print(f"\n{idx+1}. {row['insight']}")
        print(f"   Finding: {row['finding']}")
        print(f"   Why: {row['why']}")
    
    print("\n" + "="*70)
    print("TOP 10 MOST VIRAL WICKED SONGS")
    print("="*70)
    top10 = df.nlargest(10, 'virality_score')[['virality_rank', 'track_name', 'virality_score', 'tiktok_video_count', 'primary_trend_type']]
    print(top10.to_string(index=False))
    
    return df, correlations, content_performance, insights

if __name__ == "__main__":
    df, correlations, content_perf, insights = main()
