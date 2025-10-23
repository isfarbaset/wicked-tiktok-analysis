"""
Test Spotify API credentials
"""

import sys
sys.path.append('..')
from spotify_config import CLIENT_ID, CLIENT_SECRET

print("Testing Spotify API Credentials...")
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"CLIENT_ID length: {len(CLIENT_ID)}")
print(f"CLIENT_SECRET: {CLIENT_SECRET[:8]}...{CLIENT_SECRET[-8:]}")
print(f"CLIENT_SECRET length: {len(CLIENT_SECRET)}")

# Try to authenticate
try:
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    
    auth_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # Test with a simple search
    results = sp.search(q='Wicked', type='album', limit=1)
    print("\nSuccess! Credentials are valid.")
    print(f"Test search returned: {results['albums']['items'][0]['name']}")
    
except Exception as e:
    print(f"\nError: {e}")
    print("\nPlease verify your credentials at:")
    print("https://developer.spotify.com/dashboard")
    print("\nMake sure:")
    print("1. The app is active (not deleted)")
    print("2. Client ID and Secret are copied correctly")
    print("3. No extra spaces or quotes in spotify_config.py")
