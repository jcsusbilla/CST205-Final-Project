# CST 205
# TEAM 11483
# MUSIC RECOMMENDATION APP
''' JC Susbilla, Minsol Cho, Sunwoo Lee, Juan Garcia'''

# API FUNCTION FILE
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PySide6.QtGui import QPixmap
import random
from PySide6.QtCore import Qt
from io import BytesIO
#from api import sp

# set up API credentials and authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ccde7e87d847406385d72de3862c4027",
    client_secret="a49033b7c5ff4ec8951c6a96d60f4519",
    redirect_uri="http://localhost:8080",
    scope='user-library-read'
))

# --------------------- DAILY RECOMMENDATIONS SECTION ---------------------
def fetch_workout_songs(self):
    # we chose predefined genres and moods for a workout playlist
    workout_genres = ["hip-hop", "electronic", "pop", "r&b", "rock"]
    workout_moods = ["energetic", "motivational", "upbeat", "power"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in workout_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # get songs from moods
    for mood in workout_moods:
        results = sp.search(q=mood, type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # select 50 random songs
    random.shuffle(total_songs)
    selected_songs = total_songs[:50]

    # format results
    output = [
        f"<div style='text-align: center; font-size: 18px;'>"
        f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
        for i, track in enumerate(selected_songs)
    ]

    # display results
    self.results_text.setHtml("<br>".join(output))

def fetch_house_cleaning_songs(self):
    # predefined genre's and mood
    cleaning_genres = ["pop", "funk", "soul", "disco", "indie"]
    cleaning_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in cleaning_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in cleaning_moods:
        results = sp.search(q=mood, type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # select 50 random songs
    random.shuffle(total_songs)
    selected_songs = total_songs[:50]

   # format results
    output = [
        f"<div style='text-align: center; font-size: 18px;'>"
        f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
        for i, track in enumerate(selected_songs)
    ]

    # display results
    self.results_text.setHtml("<br>".join(output))

# --------------------- GENERAL RECOMMENDATIONS SECTION ---------------------
def weather_results(self, weather):
    weather_mapping = {
        "Sunny": "sunny",
        "Rainy": "rainy",
        "Cloudy": "cloudy",
        "Snowy": "snowy",
        "Windy": "windy",
        "Foggy": "foggy",
        "Stormy": "stormy",
        "Clear Night": "clear night"
    }

    weather_query = weather_mapping.get(weather, weather.lower())

    #  get songs for the selected weather
    results = sp.search(q=f"{weather_query}", type="track", limit=50)
    tracks = results.get("tracks", {}).get("items", [])
    random.shuffle(tracks)                                                                  # randomize so it's different every time

    # format the results
    output = [f"<div style='text-align: center; font-size: 18px;'>"
              f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
              for i, track in enumerate(tracks)]

    # display results
    self.results_text.setHtml("<br>".join(output))

def region_results(self, region):
    # map region to spotify market codes
    region_mapping = {
        "United States": "US",
        "United Kingdom": "GB",
        "Canada": "CA",
        "Germany": "DE",
        "France": "FR",
        "Italy": "IT",
        "Spain": "ES",
        "Japan": "JP",
        "Australia": "AU",
        "Brazil": "BR",
        "Mexico": "MX",
        "India": "IN"
    }

    market_code = region_mapping.get(region, "US")                                          # default to US if region not found

    # get songs for the selected region
    results = sp.search(q="top hits", type="track", limit=50, market=market_code)
    tracks = results.get("tracks", {}).get("items", [])
    random.shuffle(tracks)                                                                  # randomize so it's different every time

    # format the results
    output = [f"<div style='text-align: center; font-size: 18px;'>"
              f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
              for i, track in enumerate(tracks)]

    # display results
    self.results_text.setHtml("<br>".join(output))

def season_results(self, season):
    # Map season to search queries
    season_mapping = {
        "Spring": "spring",
        "Summer": "summer",
        "Autumn": "autumn",
        "Winter": "winter"
    }
    season_query = season_mapping.get(season, season.lower())
    results = sp.search(q=f"{season_query}", type="track", limit=50)
    tracks = results.get("tracks", {}).get("items", [])
    random.shuffle(tracks)                                                                  # randomize so it's different every time

    # format the results
    output = [f"<div style='text-align: center; font-size: 18px;'>"
              f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
              for i, track in enumerate(tracks)]

    # display results
    self.results_text.setHtml("<br>".join(output))

def mood_results(self, mood):
    # map mood to playlist categories or keywords
    mood_mapping = {
        "Happy": "happy",
        "Sad": "sad",
        "Energetic": "workout",
        "Chill": "chill",
        "Romantic": "romantic",
        "Focus": "focus",
        "Sleep": "sleep",
    }
    mood_query = mood_mapping.get(mood, mood.lower())

    # find the songs based on mood
    results = sp.search(q=f"{mood_query}", type="track", limit=50)
    tracks = results.get("tracks", {}).get("items", [])
    random.shuffle(tracks)                                                                  # randomize so it's different every time

    # format output
    output = [
        f"<div style='text-align: center; font-size: 18px;'>"
        f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
        for i, track in enumerate(tracks)
    ]

    # display results
    self.results_text.setHtml("<br>".join(output))

def artist_results(self, artist):
    # search for artist
    results = sp.search(q=f"artist:{artist}", type="artist", limit=1)
    artist_items = results.get("artists", {}).get("items", [])

    if not artist_items:
        self.results_text.setText("No artist found with that name.")
        return

    # retrieve the artist's ID and image
    artist_data = artist_items[0]
    artist_id = artist_data["id"]
    artist_images = artist_data.get("images", [])

    # artist image
    if artist_images:
        image_url = artist_images[0]["url"]
        response = requests.get(image_url)
        image = QPixmap()
        image.loadFromData(BytesIO(response.content).read())
        self.image_label.setPixmap(image.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    # artist's top 10 songs
    top_tracks = sp.artist_top_tracks(artist_id, country="US").get("tracks", [])
    output = [f"<div style='text-align: center; font-size: 45px; font-weight: bold;'>Top 10 Songs</div>"]
    for i, track in enumerate(top_tracks[:10]):
        output.append(f"<div style='text-align: center; font-size: 18px;'>{i + 1}. {track['name']}</div><br>")

    # display albums
    albums = sp.artist_albums(artist_id, album_type='album', limit=10).get('items', [])
    output.append("<br>")
    output.append(f"<div style='text-align: center; font-size:45px; font-weight: bold;'>Albums</div>")
    for album in albums:
        album_name = album["name"]
        release_date = album.get("release_date", "Unknown Date")
        album_images = album.get("images", [])
        output.append(f"<div style='text-align: center; margin-bottom: 40px;'>"
                        f"<span style='font-size: 18px; font-weight: bold;'>{album_name}</span><br>"
                        f"Release Date: {release_date}</div>")
    output.append("<br>")

    # Display final result
    self.results_text.setHtml("".join(output))

def genre_results(self, genre):
    # fetch top 5 artists for specific genre and get their top 10 songs
    # step 1: search for artists in the given genre
    results = sp.search(q=f"genre:{genre}", type="artist", limit=5)                                         # only pull the first 5 artists
    artists = results.get("artists", {}).get("items", [])

    # had some help from forums / youtube on efficient ways to pull from this Spotipy API

    # error handling
    if not artists:                                                                                         # if not a valid artist
        self.results_text.set_text(f"No artists found for genre: {genre}.")         
        return

    # get the top 10 songs for each artist
    output = []  # The final output to be displayed
    for artist in artists:
        artist_name = artist["name"]  
        artist_id = artist["id"]      
        artist_images = artist.get("images", [])

        # artist name 
        output.append(f"<div style='text-align: center; font-weight: bold; font-size: 25px;'>"
                      f"Artist: {artist_name}</div>")                                                       # i.e. "Kendrick Lamar"

        # top 10 songs
        top_tracks = sp.artist_top_tracks(artist_id, country="US").get("tracks", [])  
        for i, track in enumerate(top_tracks[:10]):                                                         # top 10 only
            # Add each track centered
            output.append(f"<div style='text-align: center; font-size: 16px;'>"
                          f"{i + 1}. {track['name']}</div>")

        output.append("<br>")                                                                               # newline between each artists                               
    # display results using html
    self.results_text.setHtml("".join(output))

''' old code for manually loading in API token before i found terminal install for spotify API'''
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