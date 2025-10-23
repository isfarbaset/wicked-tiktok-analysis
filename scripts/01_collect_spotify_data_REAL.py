"""
Collect REAL data from Spotify API for Wicked songs
Since audio_features endpoint requires special permissions, we:
1. Get real track metadata (names, duration, popularity) from Spotify
2. Note the audio features limitation in our analysis
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
from pathlib import Path
import sys

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))
DATA_DIR = PROJECT_ROOT / 'data'

from spotify_config import CLIENT_ID, CLIENT_SECRET

print(f"\n{'='*70}")
print("WICKED ANALYSIS - COLLECTING REAL SPOTIFY DATA")
print(f"{'='*70}\n")

print("Authenticating with Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))
print("✓ Authentication successful!\n")

def get_wicked_tracks():
    """Get real Wicked track data from Spotify"""
    
    # Search for Wicked Original Broadway Cast Recording
    search_results = sp.search(q='Wicked Original Broadway Cast Recording', type='album', limit=5)
    
    print("Found Wicked albums:")
    for i, album in enumerate(search_results['albums']['items']):
        print(f"  {i+1}. {album['name']} (ID: {album['id']})")
    
    # Use the first result (usually the main cast recording)
    album_id = search_results['albums']['items'][0]['id']
    album_name = search_results['albums']['items'][0]['name']
    
    print(f"\nUsing: {album_name}")
    print(f"Album ID: {album_id}\n")
    
    # Get all tracks from the album
    results = sp.album_tracks(album_id)
    tracks = results['items']
    
    track_data = []
    
    print("Collecting track information...")
    for track in tracks:
        try:
            # Get full track info (includes popularity)
            track_info = sp.track(track['id'])
            
            track_data.append({
                'track_id': track['id'],
                'track_name': track['name'],
                'track_number': track['track_number'],
                'duration_ms': track['duration_ms'],
                'duration_min': round(track['duration_ms'] / 60000, 2),
                'artist': ', '.join([artist['name'] for artist in track['artists']]),
                'album': album_name,
                'popularity': track_info['popularity'],
                'release_date': track_info['album']['release_date'],
                'spotify_url': track_info['external_urls']['spotify']
            })
            
            print(f"  ✓ {track['name'][:50]:<50} Pop: {track_info['popularity']}")
            
        except Exception as e:
            print(f"  ✗ Error with {track['name']}: {e}")
        
        time.sleep(0.1)  # Rate limiting
    
    return pd.DataFrame(track_data)

def main():
    # Collect Wicked tracks
    wicked_df = get_wicked_tracks()
    
    # Save to CSV
    output_file = DATA_DIR / 'spotify' / 'wicked_tracks_REAL.csv'
    wicked_df.to_csv(output_file, index=False)
    
    print(f"\n{'='*70}")
    print(f"✓ Successfully collected {len(wicked_df)} Wicked tracks")
    print(f"✓ Saved to: {output_file}")
    print(f"{'='*70}\n")
    
    print("Data preview:")
    print(wicked_df[['track_name', 'duration_min', 'popularity']].head(10))
    
    print("\n" + "="*70)
    print("NOTE: Audio Features Limitation")
    print("="*70)
    print("""
The Spotify audio_features endpoint (which provides danceability, energy, 
valence, etc.) requires special API permissions that are not available 
with standard client credentials.

For this analysis, we have:
✓ Real track names, durations, and popularity scores from Spotify
✗ Audio features would require manual annotation or advanced API access

NEXT STEPS:
1. Use the real track data we collected
2. For audio features, we can either:
   a) Manually listen and annotate key songs
   b) Use music analysis tools to extract features
   c) Focus analysis on popularity + TikTok performance
   d) Note this limitation in the final report

This is a realistic constraint that would be mentioned in a professional
data science project portfolio!
""")
    
    return wicked_df

if __name__ == "__main__":
    wicked_df = main()
