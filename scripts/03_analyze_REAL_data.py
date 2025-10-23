"""
Analyze Wicked TikTok Performance Using REAL Spotify Data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy.stats import spearmanr

# Setup paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
OUTPUT_DIR = PROJECT_ROOT / 'outputs'

# Wicked colors
EMERALD = '#00A86B'
PINK = '#E91E8C'
GOLD = '#FFD700'

plt.style.use('seaborn-v0_8-darkgrid')

def load_data():
    """Load REAL Spotify data"""
    print("Loading REAL Spotify data...")
    spotify = pd.read_csv(DATA_DIR / 'spotify' / 'wicked_tracks_REAL.csv')
    print(f"Loaded {len(spotify)} tracks from Spotify")
    
    try:
        tiktok = pd.read_csv(DATA_DIR / 'tiktok' / 'wicked_tiktok_performance.csv')
        print(f"Loaded TikTok data")
    except:
        tiktok = pd.read_csv(DATA_DIR / 'tiktok' / 'wicked_tiktok_performance_EXAMPLE.csv')
        print("Using example TikTok data")
    
    return spotify, tiktok

def clean_and_merge(spotify, tiktok):
    """Merge datasets"""
    print("\nMerging data...")
    
    # Clean track names
    spotify['clean_name'] = spotify['track_name'].str.replace(
        r' - From "Wicked".*', '', regex=True
    ).str.strip()
    
    spotify['clean_name'] = spotify['clean_name'].str.replace(
        r'\s*\(.*?\)\s*', '', regex=True
    ).str.strip()
    
    # Merge
    merged = pd.merge(
        spotify,
        tiktok,
        left_on='clean_name',
        right_on='song_name',
        how='inner'
    )
    
    print(f"Merged {len(merged)} tracks successfully")
    return merged

def analyze_correlations(df):
    """Analyze relationships"""
    print("\nAnalyzing correlations...")
    
    if len(df) >= 3 and 'tiktok_video_count' in df.columns:
        corr, p_val = spearmanr(df['popularity'], df['tiktok_video_count'])
        print(f"Popularity vs TikTok Videos: r={corr:.3f}, p={p_val:.4f}")
        return corr, p_val
    return None, None

def create_plots(df):
    """Create visualizations"""
    print("\nCreating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Wicked Analysis - Real Spotify Data', fontsize=16, fontweight='bold')
    
    # Plot 1: Popularity histogram
    ax1 = axes[0, 0]
    ax1.hist(df['popularity'], bins=15, color=EMERALD, edgecolor='black', alpha=0.7)
    ax1.set_title('Spotify Popularity Distribution')
    ax1.set_xlabel('Popularity Score')
    ax1.set_ylabel('Count')
    ax1.axvline(df['popularity'].mean(), color=PINK, linestyle='--', linewidth=2)
    
    # Plot 2: Popularity vs TikTok
    ax2 = axes[0, 1]
    if 'tiktok_video_count' in df.columns:
        ax2.scatter(df['popularity'], df['tiktok_video_count'], s=100, alpha=0.6, color=EMERALD)
        ax2.set_title('Popularity vs TikTok Videos')
        ax2.set_xlabel('Spotify Popularity')
        ax2.set_ylabel('TikTok Videos')
    
    # Plot 3: Top songs
    ax3 = axes[1, 0]
    top = df.nlargest(10, 'popularity')[['clean_name', 'popularity']].sort_values('popularity')
    ax3.barh(range(len(top)), top['popularity'], color=EMERALD, edgecolor='black')
    ax3.set_yticks(range(len(top)))
    ax3.set_yticklabels([n[:25] for n in top['clean_name']], fontsize=9)
    ax3.set_xlabel('Popularity')
    ax3.set_title('Top 10 Songs by Popularity')
    
    # Plot 4: Duration vs Popularity
    ax4 = axes[1, 1]
    ax4.scatter(df['duration_min'], df['popularity'], s=100, alpha=0.6, color=PINK)
    ax4.set_title('Duration vs Popularity')
    ax4.set_xlabel('Duration (minutes)')
    ax4.set_ylabel('Popularity')
    
    plt.tight_layout()
    output = OUTPUT_DIR / 'figures' / 'wicked_analysis.png'
    plt.savefig(output, dpi=300, bbox_inches='tight')
    print(f"Saved: {output}")
    plt.close()

def generate_report(df):
    """Generate insights report"""
    print("\nGenerating report...")
    
    lines = []
    lines.append("="*70)
    lines.append("WICKED TIKTOK ANALYSIS - KEY INSIGHTS")
    lines.append("="*70)
    lines.append("")
    lines.append(f"Total songs: {len(df)}")
    lines.append(f"Avg popularity: {df['popularity'].mean():.1f}")
    lines.append(f"Popularity range: {df['popularity'].min()}-{df['popularity'].max()}")
    lines.append("")
    lines.append("TOP 5 MOST POPULAR:")
    for i, (_, row) in enumerate(df.nlargest(5, 'popularity').iterrows(), 1):
        lines.append(f"{i}. {row['clean_name']} - {row['popularity']}")
    lines.append("")
    lines.append("KEY FINDINGS:")
    lines.append(f"- Most popular: {df.loc[df['popularity'].idxmax(), 'clean_name']}")
    lines.append(f"- Longest song: {df.loc[df['duration_min'].idxmax(), 'clean_name']}")
    lines.append("")
    lines.append("DATA NOTES:")
    lines.append("- Used REAL Spotify API data")
    lines.append("- Audio features unavailable (API restriction)")
    lines.append("="*70)
    
    report = "\n".join(lines)
    
    output = OUTPUT_DIR / 'reports' / 'analysis_insights.txt'
    with open(output, 'w') as f:
        f.write(report)
    
    print("\n" + report)
    print(f"\nSaved: {output}")

def main():
    print("\n" + "="*70)
    print("WICKED TIKTOK ANALYSIS - REAL DATA")
    print("="*70)
    
    # Load and merge
    spotify, tiktok = load_data()
    df = clean_and_merge(spotify, tiktok)
    
    # Save merged data
    df.to_csv(DATA_DIR / 'processed' / 'wicked_merged.csv', index=False)
    print(f"Saved merged data")
    
    # Analyze
    analyze_correlations(df)
    create_plots(df)
    generate_report(df)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    
    return df

if __name__ == "__main__":
    df = main()
