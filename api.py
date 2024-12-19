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

def artist_of_the_day(self):
    # Randomly select an artist
    results = sp.search(q="year:2023", type="artist", limit=20)
    artists = results.get("artists", {}).get("items", [])
    if not artists:
        self.artist_name_label.setText("No artist found.")
        self.artist_image.clear()
        self.top_songs_label.setText("")
        return

    artist = random.choice(artists)
    artist_name = artist["name"]
    artist_id = artist["id"]
    artist_images = artist.get("images", [])
    
    # Display Artist Name
    self.artist_name_label.setText(artist_name)

    # Display Artist Image
    if artist_images:
        image_url = artist_images[0]["url"]
        response = requests.get(image_url)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.artist_image.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
    else:
        self.artist_image.setText("No image available.")

    # Fetch and Display Top 5 Songs
    top_tracks = sp.artist_top_tracks(artist_id, country="US").get("tracks", [])
    if top_tracks:
        songs = [f"{i + 1}. {track['name']}" for i, track in enumerate(top_tracks[:5])]
        self.top_songs_label.setText(
            "<br>".join(f"<div style='text-align: center;'>{song}</div>" for song in songs)
        )
    else:
        self.top_songs_label.setText("No top songs available.")

# --------------------- NEW RELEASE RECOMMENDATION BY REGION ---------------------
def get_user_location():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return data.get("country", "US")                                                            # default to US
    except:
        return "US"
    
def fetch_new_release(country_code):
    results = sp.new_releases(country=country_code, limit=20)                                       # set 20 max
    albums = results.get("albums", {}).get("items", [])
    if not albums:
        return None

    return random.choice(albums)                                                                    # randomly select 1 album to display

def display_new_release(self):
    country_code = get_user_location()                                                              # retrieve user location
    new_release = fetch_new_release(country_code)                                                   # retrieve new releases by location

    # retrieve album details
    album_name = new_release["name"]
    artist_name = ", ".join(artist["name"] for artist in new_release["artists"])
    release_date = new_release["release_date"]
    image_url = new_release["images"][0]["url"] if new_release["images"] else None

    # display album cover
    if image_url:
        response = requests.get(image_url)                                                          # get image
        pixmap = QPixmap()                                                                          # creat pixmap
        pixmap.loadFromData(response.content)
        self.new_release_image.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio))               # set image size

    # display album details
    self.new_release_details.setText(
        f"<div style='text-align: center; font-size: 16px;'>"                                       # set text style
        f"<span style='font-size: 40px; font-weight: bold;'>{album_name}</span><br>"                # set text style
        f"<span style='font-size: 28px;'>Artist: {artist_name}</span><br>"                          # set text style
        f"<span style='font-size: 20px;'>Release Date: {release_date}</span>"                       # set text style
        f"</div>"
    )

# --------------------- DAILY RECOMMENDATIONS SECTION ---------------------
def fetch_workout_songs(self):
    # we chose predefined genres and moods for a workout playlist
    workout_genres = ["hip-hop", "work-out", "pop", "r&b", "rock"]
    workout_moods = ["energetic", "motivational", "upbeat", "power"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10                                                                         # max 10 songs
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

# to do: meditation 
def fetch_meditation_songs(self):
    # predefined genre's and mood
    meditation_genres = ["jazz", "classical", "chill", "house"]
    meditation_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in meditation_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in meditation_moods:
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

# to do: studying 
def fetch_studying_songs(self):
    # predefined genre's and mood
    studying_genres = ["pop", "classical", "chill", "study", "jazz"]
    studying_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in studying_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in studying_moods:
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

# to do: cooking 
def fetch_cooking_songs(self):
    # predefined genre's and mood
    cooking_genres = ["pop", "ambient", "chill", "house", "dance"]
    cooking_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in cooking_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in cooking_moods:
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

# to do: party 
def fetch_party_songs(self):
    # predefined genre's and mood
    party_genres = ["pop", "electronic", "party", "house", "rock"]
    party_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in party_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in party_moods:
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

# to do: road trip 
def fetch_road_trip_songs(self):
    # predefined genre's and mood
    road_trip_genres = ["pop", "funk", "soul", "road-trip", "indie"]
    road_trip_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in road_trip_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in road_trip_moods:
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

# to do: gaming 
def fetch_gaming_songs(self):
    # predefined genre's and mood
    gaming_genres = ["pop", "funk", "chill", "groove", "indie"]
    gaming_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in gaming_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in gaming_moods:
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

# to do: kids 
def fetch_kids_songs(self):
    # predefined genre's and mood
    kids_genres = ["pop", "children", "reggae", "disco", "chill"]
    kids_moods = ["happy", "upbeat", "feel-good", "cheerful"]

    # set number of songs to fetch per genre/mood
    # set to 100 total chosen songs so that we can randomize and select 50
    songs_per_category = 10
    total_songs = []

    # get songs from genres
    for genre in kids_genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

     # get songs from moods
    for mood in kids_moods:
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

# thank you guys :)
# --------------------- GENERAL RECOMMENDATIONS SECTION ---------------------
def weather_results(self, weather):
    # selected predefined genre's and moods and link them to regions
    weather_genre_mapping = {
        "Sunny": ["pop", "dance", "electronic", "summer"],
        "Rainy": ["blues", "rainy-day", "acoustic", "indie"],
        "Cloudy": ["ambient", "chill", "lo-fi", "instrumental"],
        "Stormy": ["rock", "metal", "grunge", "electronic"],
        "Snowy": ["classical", "instrumental", "folk", "acoustic"],
        "Clear Night": ["blues", "indie", "soothing", "jazz"]
    }
    weather_mood_mapping = {
        "Sunny": ["uplifting", "happy", "energetic"],
        "Rainy": ["melancholic", "soothing", "reflective"],
        "Cloudy": ["calm", "relaxed"],
        "Stormy": ["intense", "powerful"],
        "Snowy": ["peaceful", "nostalgic"],
        "Clear Night": ["calm", "relaxed", "soothing"]
    }

    # Retrieve genres and moods for the selected weather condition
    genres = weather_genre_mapping.get(weather, [])
    moods = weather_mood_mapping.get(weather, [])

    # get songs for genres and moods
    songs_per_category = 10  # Number of songs to fetch per genre/mood
    total_songs = []

    # get songs for each genre
    for genre in genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # get songs for each mood
    for mood in moods:
        results = sp.search(q=mood, type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # shuffle
    random.shuffle(total_songs)
    selected_songs = total_songs[:50]

    # format the results
    output = [
        f"<div style='text-align: center; font-size: 18px;'>"
        f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
        for i, track in enumerate(selected_songs)
    ]

    # display the results
    self.results_text.setHtml("<br>".join(output))

def region_results(self, region):
    # selected predefined genre's and moods and link them to regions
    region_genre_mapping = {
        "USA": ["pop", "hip-hop", "country", "rock"],
        "Latin America": ["reggaeton", "salsa", "bachata", "cumbia"],
        "Europe": ["electronic", "classical", "indie", "pop"],
        "Asia": ["k-pop", "bollywood", "j-pop", "traditional", "malay", "philippines-opm"],
        "Africa": ["afrobeats", "highlife", "gqom", "soukous"]
    }
    region_mood_mapping = {
        "USA": ["energetic", "upbeat"],
        "Latin America": ["cheerful", "party"],
        "Europe": ["relaxed", "inspirational"],
        "Asia": ["vibrant", "soothing"],
        "Africa": ["dynamic", "uplifting"]
    }
    # get genres and moods for the selected region
    genres = region_genre_mapping.get(region, [])
    moods = region_mood_mapping.get(region, [])

    # get songs for genres and moods
    songs_per_category = 10 
    total_songs = []

    # get songs for each genre
    for genre in genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # get songs for each mood
    for mood in moods:
        results = sp.search(q=mood, type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # shuffle
    random.shuffle(total_songs)
    selected_songs = total_songs[:50]

    # format results output
    output = [
        f"<div style='text-align: center; font-size: 18px;'>"
        f"{i + 1}. <span style='font-weight: bold;'>{track['name']}</span> - {track['artists'][0]['name']}</div>"
        for i, track in enumerate(selected_songs)
    ]

    # display results
    self.results_text.setHtml("<br>".join(output))

def season_results(self, season):
    # select predefined genre's and link them to specific moods
    season_genre_mapping = {
        "Spring": ["acoustic", "folk", "indie", "pop"],
        "Summer": ["reggaeton", "summer", "hip-hop", "electronic"],
        "Autumn": ["rock", "soul", "jazz", "classical"],
        "Winter": ["ambient", "classical", "blues", "instrumental"]
    }

    season_mood_mapping = {
        "Spring": ["uplifting", "happy"],
        "Summer": ["energetic", "party"],
        "Autumn": ["reflective", "calm"],
        "Winter": ["soothing", "melancholic"]
    }

    # retrieve genres and moods for the selected season
    genres = season_genre_mapping.get(season, [])
    moods = season_mood_mapping.get(season, [])

    # get songs for genres and moods
    songs_per_category = 10
    total_songs = []

    # get songs for each genre
    for genre in genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # get songs for each mood
    for mood in moods:
        results = sp.search(q=mood, type="track", limit=songs_per_category)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # shuffle
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

def mood_results(self, mood):
    # select predefined genre's and link them to specific moods
    mood_genre_mapping = {
        "Energetic": ["pop", "electronic", "dance"],
        "Calm": ["ambient", "classical", "acoustic"],
        "Happy": ["pop", "funk", "soul"],
        "Sad": ["indie", "folk", "blues"],
        "Motivational": ["rock", "hip-hop", "electronic"],
        "Sleep": ["soul", "blues", "indie"]
    }

    # retrieve genres for the selected mood
    genres = mood_genre_mapping.get(mood, [])

    # fetch songs for each genre
    songs_per_genre = 10
    total_songs = []

    for genre in genres:
        results = sp.search(q=f"genre:{genre}", type="track", limit=songs_per_genre)
        tracks = results.get("tracks", {}).get("items", [])
        total_songs.extend(tracks)

    # shuffle the songs
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
        self.image_label.setPixmap(image.scaled(300, 300, Qt.KeepAspectRatio))

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

    # display results
    self.results_text.setHtml("".join(output))

def genre_results(self, genre):
    # fetch top 5 artists for specific genre and get their top 10 songs
    # search for artists in the given genre
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