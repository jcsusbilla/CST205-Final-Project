# CST 205
# TEAM 11483
# MUSIC RECOMMENDATION APP
''' JC Susbilla, Minsol Cho, Sunwoo Lee, Juan Garcia'''

# API FUNCTION FILE

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


def fetch_and_display_genre_results(self, genre):
    # fetch top 5 artists for specific genre and get their top 10 songs
    # step 1: search for artists in the given genre
    results = sp.search(q=f"genre:{genre}", type="artist", limit=5)                     # only pull the first 5 artists
    artists = results.get("artists", {}).get("items", [])

    # had some help from forums / youtube on efficient ways to pull from API

    # error handling
    if not artists:                                                                     # if not a valid artist
        self.results_text.set_text(f"No artists found for genre: {genre}.")         
        return

    # step 2: get the top 10 songs for each artist
    output = []                                                                         # the final output to be displayed
    for artist in artists:
        artist_name = artist["name"]                                                    # pull and separate artist name into own variable
        artist_id = artist["id"]                                                        # pull artist id and put into own variable
        output.append(f"Artist: {artist_name}")                                         # i.e: "Arist: Kendrick Lamar"

        # fetch top 10 songs
        top_tracks = sp.artist_top_tracks(artist_id, country="US").get("tracks", [])    # list of top songs from artist
        for track in top_tracks[:10]:                                                   # pull 10 only
            output.append(f"  - {track['name']}")                                       # more format to output

        output.append("")                                                               # newline between artists

    # step 3: display result
    self.results_text.set_text("\n".join(output))                                       # concatenate the whole string output





''' old code for manually loading in API token before i discovered terminal install for spotify API'''
# # --------------------- load in environment variables ---------------------
# # pip install python-dotenv
# # pip install requests
# from dotenv import load_dotenv
# import spotipy
# import base64
# import json
# from requests import post, get                                   # allow to send post request
# load_dotenv()
# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")
# #print(client_id, client_secret) # TEST

# # retrieve and post access token for Spotify API
# def get_token():
#     auth_string = client_id + ":" + client_secret
#     auth_bytes = auth_string.encode("utf-8")
#     auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Authorization": "Basic " + auth_base64,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {"grant_type": "client_credentials"}
#     result = post(url, headers=headers, data=data)
#     json_result = json.loads(result.content)
#     token = json_result["access_token"]
#     return token

# def get_auth_header(token):
#     return {"Authorization": "Bearer "+ token}

# def search_for_artist(token, artist_name):
#     url = "https://api.spotify.com/v1/search"               # define url
#     headers = get_auth_header(token)                        # get headers
#     # contruct query
#     query = f"?q={artist_name}&type=artist&limit=1"          #return top 1 artist
    
#     query_url = url + query
#     result = get(query_url, headers=headers)
#     json_result = json.loads(result.content)
#     print(json_result)

# # ******** TEST API FUNCTION CALLS ********
# token = get_token() 
# #print("token: " + token) #TEST                             # retrieve api token

# search_for_artist(token, "Bruno Mars")                      # search by artist
# # genre search
# # song search


# --------------------- SPOTIPY TEST ---------------------
# Specify the genre
# genre = "Folk"
# random_albums = api.get_random_albums_by_genre(genre)

# print(f"Random {len(random_albums)} albums for genre '{genre}':")
# for album in random_albums:
#     print(album)

# Specify the genre to search
# genre_to_search = "Reggae"  # Change the genre as needed
# api.get_top_tracks_by_genre(genre_to_search)