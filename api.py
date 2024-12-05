import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

# set up API credentials and authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ccde7e87d847406385d72de3862c4027",
    client_secret="a49033b7c5ff4ec8951c6a96d60f4519",
    redirect_uri="http://localhost:8080",
    scope='user-library-read'
))

def get_random_albums_by_genre(genre, limit=5):
    # Search Spotify for albums by genre
    results = sp.search(q=f'genre:{genre}', type='album', limit=50)  # Fetch up to 50 results
    albums = results.get('albums', {}).get('items', [])
    
    # Shuffle and select 20 random albums
    random.shuffle(albums)
    selected_albums = albums[:limit]
    
    # Extract album names
    album_names = [album['name'] for album in selected_albums]
    return album_names

def get_top_tracks_by_genre(genre, num_artists=5, num_tracks=10):
    # Step 1: Search for artists in the genre
    search_results = sp.search(q=f'genre:{genre}', type='artist', limit=num_artists)
    artists = search_results.get('artists', {}).get('items', [])
    
    if not artists:
        print(f"No artists found for genre: {genre}")
        return

    # Step 2: Retrieve the top tracks for each artist
    genre_top_tracks = {}
    for artist in artists:
        artist_name = artist['name']
        artist_id = artist['id']
        
        # Fetch the top tracks for the artist
        top_tracks = sp.artist_top_tracks(artist_id)['tracks']
        top_track_names = [track['name'] for track in top_tracks[:num_tracks]]
        
        genre_top_tracks[artist_name] = top_track_names

    # Step 3: Print results
    for artist, tracks in genre_top_tracks.items():
        print(f"\nTop {num_tracks} tracks by {artist}:")
        for i, track in enumerate(tracks, start=1):
            print(f"{i}. {track}")

