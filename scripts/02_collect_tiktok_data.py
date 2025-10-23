"""
Collect actual TikTok performance data for Wicked songs

Since TikTok API is restricted, this provides:
1. A template for manual data collection
2. Methods to scrape public TikTok data (where possible)
3. Example data structure
"""

import pandas as pd
from datetime import datetime
import time
import os
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'

def create_tiktok_template():
    """Create template for manually collecting TikTok data"""
    
    wicked_df = pd.read_csv(DATA_DIR / 'spotify' / 'wicked_audio_features.csv')
    
    template = pd.DataFrame({
        'song_name': wicked_df['track_name'],
        'tiktok_video_count': [0] * len(wicked_df),
        'tiktok_view_estimate_millions': [0.0] * len(wicked_df),
        'peak_trend_date': [''] * len(wicked_df),
        'weeks_trending': [0] * len(wicked_df),
        'primary_trend_type': [''] * len(wicked_df),
        'viral_moment': [''] * len(wicked_df),
        'celebrity_boost': [''] * len(wicked_df),
        'notes': [''] * len(wicked_df)
    })
    
    instructions = """
TIKTOK DATA COLLECTION INSTRUCTIONS:

For each Wicked song, search on TikTok and record:

1. tiktok_video_count: Number of videos using this sound
   - Search the song name on TikTok
   - Look at the sound page
   - Record the video count

2. tiktok_view_estimate_millions: Rough view estimate
   - Based on top videos' view counts
   - Estimate total views across all videos

3. peak_trend_date: When did it peak?
   - Check Google Trends
   - Look at TikTok video dates
   - When were most videos posted?

4. weeks_trending: How long was it popular?
   - Count weeks with significant activity

5. primary_trend_type: What format dominated?
   - Dance Challenge
   - Lip Sync / Vocal Showcase
   - POV / Storytelling
   - Duets
   - Comedy / Parody
   - GRWM (Get Ready With Me)
   - Transition
   - Other

6. viral_moment: Why did it go viral?
   - Movie release hype
   - Dance challenge created
   - Celebrity used it
   - Meme format emerged
   - Emotional resonance

7. celebrity_boost: Which celebrities used it?
   - List major influencers who posted with this sound

8. notes: Any additional context

Save completed data as: ../data/tiktok/wicked_tiktok_performance.csv
"""
    
    template.to_csv(DATA_DIR / 'tiktok' / 'tiktok_collection_template.csv', index=False)
    
    with open(DATA_DIR / 'tiktok' / 'INSTRUCTIONS.txt', 'w') as f:
        f.write(instructions)
    
    print("Created TikTok data collection template")
    print("\nSee data/tiktok/INSTRUCTIONS.txt for detailed collection guide")
    
    return template

def create_example_data():
    """
    Create example TikTok data based on what we know happened
    
    NOTE: This is EXAMPLE data for demonstration.
    Replace with actual data you collect from TikTok!
    """
    
    example_data = pd.DataFrame({
        'song_name': [
            'Defying Gravity',
            'Popular',
            'The Wizard and I',
            'What Is This Feeling?',
            'Dancing Through Life',
            'I\'m Not That Girl',
            'One Short Day',
            'For Good',
            'No Good Deed',
            'As Long As You\'re Mine',
            'No One Mourns the Wicked',
            'Wonderful',
            'Thank Goodness',
            'A Sentimental Man',
            'March of the Witch Hunters'
        ],
        'tiktok_video_count': [
            287000, 195000, 58000, 142000, 98000, 45000, 52000, 91000,
            67000, 38000, 71000, 29000, 35000, 15000, 41000
        ],
        'tiktok_view_estimate_millions': [
            850.0, 520.0, 95.0, 310.0, 180.0, 72.0, 98.0, 165.0,
            125.0, 65.0, 142.0, 48.0, 61.0, 28.0, 75.0
        ],
        'peak_trend_date': [
            '2024-11-30', '2024-12-05', '2024-12-10', '2024-11-27',
            '2024-12-03', '2024-12-15', '2024-12-08', '2024-12-20',
            '2024-12-12', '2024-12-18', '2024-11-25', '2024-12-07',
            '2024-12-14', '2025-01-05', '2024-12-09'
        ],
        'weeks_trending': [
            16, 14, 6, 10, 8, 5, 7, 9, 8, 4, 7, 4, 5, 2, 6
        ],
        'primary_trend_type': [
            'Vocal Showcase / Lip Sync', 'Dance / POV', 'Storytelling / Aspiration',
            'Duets / Comedy', 'Dance', 'Sad POV / Emotional', 'GRWM / Transition',
            'Friendship Posts', 'Dramatic Lip Sync', 'Romantic POV', 'Storytelling',
            'Comedy / Satire', 'Irony / Comedy', 'Background Music', 'Dramatic Edit'
        ],
        'viral_moment': [
            'THE Wicked song - vocal showcases + movie hype',
            'Ariana Grande effect + catchy + relatable',
            'Aspiration content + dream sequences',
            'Roommate humor + college content + duet format',
            'Jonathan Bailey thirst edits + dance challenges',
            'Emotional vulnerability + sad girl hours',
            'Emerald City aesthetic + outfit transitions',
            'End credits boost + friendship appreciation',
            'Villain arc content + dramatic reveals',
            'Romantic edits + couple content',
            'Context setting + movie opening',
            'Political satire + authority figures',
            'Graduation / achievement irony',
            'Background for other content',
            'Dramatic edit music'
        ],
        'celebrity_boost': [
            'Idina Menzel, Cynthia Erivo, countless Broadway performers',
            'Ariana Grande (HUGE), dance creators',
            'Cynthia Erivo performances',
            'College influencers, comedy creators',
            'Jonathan Bailey edits, dance community',
            'Mental health influencers',
            'Fashion/beauty creators',
            'Friendship content creators',
            'Theater kids, dramatic content',
            'Couple content creators',
            'Movie reviewers',
            'Political commentary',
            'Graduation season creators',
            'General background use',
            'Edit community'
        ],
        'notes': [
            'Became THE defining Wicked sound on TikTok',
            'Second only to Defying Gravity, massive range appeal',
            'Moderate trend, aspirational content',
            'Surprise hit - comedy + relatability > audio features',
            'Visual appeal (Jonathan Bailey) drove virality',
            'Emotional vulnerability resonated',
            'Visual/aesthetic focus',
            'Sustained by end credits emotional impact',
            'Villain content popular',
            'Romantic subplot content',
            'Movie opening context',
            'Lower virality despite cultural relevance',
            'Ironic use cases',
            'Background use, not main focus',
            'Edit community adoption'
        ]
    })
    
    example_data.to_csv(DATA_DIR / 'tiktok' / 'wicked_tiktok_performance_EXAMPLE.csv', index=False)
    
    print("\nCreated EXAMPLE TikTok performance data")
    print("IMPORTANT: This is sample data. Replace with real TikTok data!")
    
    return example_data

def collect_content_type_breakdown():
    """
    Create template for analyzing what content types worked for each song
    """
    
    content_types = pd.DataFrame({
        'content_type': [
            'Dance Challenge', 'Lip Sync / Vocal Showcase', 'POV / Storytelling',
            'Duets', 'Comedy / Parody', 'GRWM / Transition', 'Emotional / Sad Content',
            'Thirst Edits', 'Friendship Posts', 'Couple Content', 'Background Music'
        ],
        'description': [
            'Choreographed dance routines', 'Singing along or showcasing vocals',
            'Point of view storytelling videos', 'Duet format with split screen',
            'Funny takes or parodies', 'Get ready with me or outfit transitions',
            'Emotional vulnerability or sad content', 'Attractive person edits',
            'Celebrating friendships', 'Romantic couple content',
            'Used as background for other content'
        ],
        'typical_duration': [
            '30-60 seconds', '30-90 seconds', '15-60 seconds', '15-30 seconds',
            '15-45 seconds', '30-90 seconds', '30-60 seconds', '15-30 seconds',
            '30-60 seconds', '30-60 seconds', 'Full song or clip'
        ]
    })
    
    content_types.to_csv(DATA_DIR / 'tiktok' / 'content_type_reference.csv', index=False)
    
    print("\nCreated content type reference")
    
    return content_types

def main():
    print("\n" + "="*70)
    print("WICKED RETROSPECTIVE ANALYSIS - TIKTOK DATA COLLECTION")
    print("="*70)
    
    print("\n1. Creating collection template...")
    template = create_tiktok_template()
    
    print("\n2. Creating example data...")
    example = create_example_data()
    
    print("\n3. Creating content type reference...")
    content_types = collect_content_type_breakdown()
    
    print("\n" + "="*70)
    print("TIKTOK DATA COLLECTION SETUP COMPLETE")
    print("="*70)
    
    print("\nNext Steps:")
    print("1. Read data/tiktok/INSTRUCTIONS.txt")
    print("2. Go to TikTok and search each Wicked song")
    print("3. Fill in data/tiktok/tiktok_collection_template.csv")
    print("4. Save as data/tiktok/wicked_tiktok_performance.csv")
    print("\nOR use the example data to proceed with analysis")
    
    return template, example, content_types

if __name__ == "__main__":
    template, example, content_types = main()
