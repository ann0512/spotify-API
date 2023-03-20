from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


# Set up authorization
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get artist ID
artist_name = 'Ed Sheeran'
results = sp.search(q=artist_name, type='artist')
artist_id = results['artists']['items'][0]['id']

# Get artist's top tracks
top_tracks = sp.artist_top_tracks(artist_id)

# Print out the top 10 tracks
print(f'Top 10 tracks of {artist_name}:')
for i, track in enumerate(top_tracks['tracks'][:10]):
    print(f"{i+1}. {track['name']} by {track['artists'][0]['name']}")
