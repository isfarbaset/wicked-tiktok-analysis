"""
Collect audio features for Wicked and comparison musicals from Spotify
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
from datetime import datetime
import sys
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))
DATA_DIR = PROJECT_ROOT / 'data'

from spotify_config import CLIENT_ID, CLIENT_SECRET

print(f"Authenticating with Spotify...")
print(f"Client ID: {CLIENT_ID[:10]}...")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

print("✓ Authentication successful!")

def get_album_tracks_with_features(album_id, musical_name):
    """Get all tracks with audio features from an album"""
    
    results = sp.album_tracks(album_id)
    tracks = results['items']
    
    track_data = []
    
    for track in tracks:
        track_id = track['id']
        
        try:
            audio_features = sp.audio_features(track_id)[0]
            track_info = sp.track(track_id)
            
            if audio_features:
                track_data.append({
                    'musical': musical_name,
                    'track_name': track['name'],
                    'track_number': track['track_number'],
                    'duration_ms': track['duration_ms'],
                    'duration_min': round(track['duration_ms'] / 60000, 2),
                    'track_id': track_id,
                    'popularity': track_info['popularity'],
                    'release_date': track_info['album']['release_date'],
                    
                    'danceability': audio_features['danceability'],
                    'energy': audio_features['energy'],
                    'key': audio_features['key'],
                    'loudness': audio_features['loudness'],
                    'mode': audio_features['mode'],
                    'speechiness': audio_features['speechiness'],
                    'acousticness': audio_features['acousticness'],
                    'instrumentalness': audio_features['instrumentalness'],
                    'liveness': audio_features['liveness'],
                    'valence': audio_features['valence'],
                    'tempo': audio_features['tempo'],
                    'time_signature': audio_features['time_signature']
                })
                
        except Exception as e:
            print(f"Error with {track['name']}: {e}")
        
        time.sleep(0.1)
    
    return pd.DataFrame(track_data)

def main():
    print("\n" + "="*70)
    print("WICKED RETROSPECTIVE ANALYSIS - SPOTIFY DATA COLLECTION")
    print("="*70)
    
    print("\nCollecting Wicked audio features...")
    wicked_df = get_album_tracks_with_features(
        '1woCvthHJakakroP6dXNxs',
        'Wicked'
    )
    wicked_df.to_csv(DATA_DIR / 'spotify' / 'wicked_audio_features.csv', index=False)
    print(f"✓ Collected {len(wicked_df)} Wicked songs")
    
    print("\nCollecting comparison musicals...")
    comparison_musicals = {
        'Hamilton': '1kCHru7uhxBUdzkm4gzRQc',
        'The Greatest Showman': '5GbW8HByrbMhhnBAiH8q92',
        'Frozen Broadway': '0hPMEEX3kvEdbqRiVVAucW',
        'Mean Girls': '3jXBkjLZXDwJFbMZqPvdOl',
        'Six': '1OWqShZzyDvtVCOoF8q7uf',
    }
    
    all_comparison = []
    for name, album_id in comparison_musicals.items():
        print(f"  Collecting {name}...")
        df = get_album_tracks_with_features(album_id, name)
        all_comparison.append(df)
        time.sleep(1)
    
    comparison_df = pd.concat(all_comparison, ignore_index=True)
    comparison_df.to_csv(DATA_DIR / 'spotify' / 'comparison_musicals.csv', index=False)
    print(f"✓ Collected {len(comparison_df)} comparison songs")
    
    print("\n" + "="*70)
    print("SPOTIFY DATA COLLECTION COMPLETE")
    print("="*70)
    print(f"\nWicked songs: {len(wicked_df)}")
    print(f"Comparison songs: {len(comparison_df)}")
    print(f"Total: {len(wicked_df) + len(comparison_df)}")
    
    print("\nWicked Songs Preview:")
    print(wicked_df[['track_name', 'energy', 'danceability', 'valence']].head(10))
    
    return wicked_df, comparison_df

if __name__ == "__main__":
    wicked_df, comparison_df = main()
