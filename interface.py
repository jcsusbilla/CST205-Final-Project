# CST 205
# TEAM 11483
# MUSIC RECOMMENDATION APP
''' JC Susbilla, Minsol Cho, Sunwoo Lee, Juan Garcia'''

# INTERFACE GUI FILE

# IMPORTS
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QComboBox, QVBoxLayout, QGroupBox, QLineEdit, QTextEdit, QPushButton, QSpacerItem, QSizePolicy
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import os
import api
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from io import BytesIO
from api import sp

# --------------------- GUI INTERFACE ---------------------

# set up spotify API credentials and authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ccde7e87d847406385d72de3862c4027",
    client_secret="a49033b7c5ff4ec8951c6a96d60f4519",
    redirect_uri="http://localhost:8080",
    scope='user-library-read'
))

# ------------------ NEW WINDOWS SECTION ------------------

# WINDOW TO DISPLAY 50 SONGS BASED ON WEATHER
class WeatherResultsWindow(QWidget):
    def __init__(self, weather):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        weather_title_label = QLabel(f"50 Songs for {weather} Weather")
        weather_title_label.alignment = Qt.AlignCenter
        weather_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(weather_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.weather_results(self, weather)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON REGION
class RegionResultsWindow(QWidget):
    def __init__(self, region):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        region_title_label = QLabel(f"50 Songs for {region}")
        region_title_label.alignment = Qt.AlignCenter
        region_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(region_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.region_results(self, region)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON SEASON
class SeasonResultsWindow(QWidget):
    def __init__(self, season):
        super().__init__()
        self.resize(600, 800)

        # Main layout
        layout = QVBoxLayout()
        season_title_label = QLabel(f"50 Songs for {season}")
        season_title_label.alignment = Qt.AlignCenter
        season_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(season_title_label)

        # Text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # Fetch and display results
        api.season_results(self, season)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON MOOD
class MoodResultsWindow(QWidget):
    def __init__(self, mood):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        mood_title_label = QLabel(f"50 Songs for {mood} Mood")
        mood_title_label.alignment = Qt.AlignCenter
        mood_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(mood_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.mood_results(self, mood)
        self.set_layout(layout)

# WINDOW TO DISPLAY SPECIFIED ARTIST AND THEIR TOP 10 SONGS. ALSO SHOW AN IMAGE AND ALBUMS
class ArtistResultsWindow(QWidget):
    def __init__(self, artist):
        super().__init__()
        self.resize(800, 1000)

        # main layout
        layout = QVBoxLayout()
        artist = artist.title()
        artist_name_label = QLabel(f"{artist}")
        artist_name_label.alignment = Qt.AlignCenter
        artist_name_label.set_style_sheet("font-size: 75px; font-weight: bold;")
        layout.add_widget(artist_name_label)
        
        # artist image placeholder
        self.image_label = QLabel()  # initialize the image label here
        self.image_label.alignment = Qt.AlignCenter
        layout.add_widget(self.image_label)

        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        self.set_layout(layout)

        # display artist info
        api.artist_results(self, artist)
        
# WINDOW TO DISPLAY GENRE'S TOP 5 ARTISTS AND EACH ARTIST TOP 10 SONGS
class GenreResultsWindow(QWidget):  
    def __init__(self, genre):
        super().__init__()
        self.resize(800, 1000)                                                  # window header
        layout = QVBoxLayout()                                                  # init layout
        genre = genre.title()

        # HEADER / WINDOW TITLE
        genre_results_label = QLabel(f"Top Artists and Songs for the {genre} Genre")
        genre_results_label.alignment = Qt.AlignCenter
        genre_results_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(genre_results_label)                                  #add widget to layout

        # area to display results
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                      # set it so that text cannot be edited after being displayed
        layout.add_widget(self.results_text)                                    # add results widget to the layout
        self.results_text.alignment = Qt.AlignCenter

        # get results
        api.genre_results(self, genre)
        self.set_layout(layout)

# ------------------ MAIN ------------------
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        top_hbox = QHBoxLayout()                                                # create horizontal box layout for the top
        # -------------------- ARTIST OF THE DAY SECTION (Juan) --------------------    
        # top horizontal box -- group box 1 and group box 2)                    
        group_box_1 = QGroupBox("Artist of the Day")                            # create group box 1





        # -------------------- DAILY RECOMMENDATION SECTION (Minsol / Sunwoo) --------------------
        group_box_2 = QGroupBox("Daily Recommendations")                        # create group box 2
        group_box_2_layout = QVBoxLayout()                                      # create layout for group box 2

        workout_button = QPushButton("Workout")                                 # create workout button
        group_box_2_layout.add_widget(workout_button)                           # add workout button to layout

        house_cleaning_button = QPushButton("House Cleaning")                   # create house cleaning button
        group_box_2_layout.add_widget(house_cleaning_button)                    # add house cleaning button to layout

        meditation_button = QPushButton("Meditation")                           # create meditation button
        group_box_2_layout.add_widget(meditation_button)                        # add meditation button to layout

        studying_button = QPushButton("Studying")                               # create studying button
        group_box_2_layout.add_widget(studying_button)                          # add Studying button to layout

        cooking_button = QPushButton("Cooking")                                 # create cooking button
        group_box_2_layout.add_widget(cooking_button)                           # add Cooking button to layout

        party_button = QPushButton("Party")                                     # create party button
        group_box_2_layout.add_widget(party_button)                             # add party button to layout

        road_trip_button = QPushButton("Road Trip")                             # create road trip button
        group_box_2_layout.add_widget(road_trip_button)                         # add road trip button to layout

        gaming_button = QPushButton("Gaming")                                   # create gaming button
        group_box_2_layout.add_widget(gaming_button)                            # add gaming button to layout

        kids_button = QPushButton("Kids")                                       # create kids button
        group_box_2_layout.add_widget(kids_button)                              # add kids button to layout

        group_box_2.set_layout(group_box_2_layout)                              # assign layout to group box 2

        # add boxes to top row of boxes
        top_hbox.add_widget(group_box_1, stretch=1)                             # add group box 1 to the horizontal layout
        top_hbox.add_widget(group_box_2, stretch=1)                             # add group box 2 to the horizontal layout


        # -------------------- PLAYLIST SECTION (Minsol / Sunwoo) --------------------
        # bottom-left box -- playlist
        bottom_left_hbox = QVBoxLayout()                                        # create left vertical box
        group_box_3 = QGroupBox("Most Recent Playlist")                         # create group box 3
        bottom_left_hbox.add_widget(group_box_3)                                # add group box 3 to the left vertical box

        # buttons under the playlist box
        button_1 = QPushButton("Create Playlist")
        button_2 = QPushButton("View Playlists")
        bottom_left_hbox.add_widget(button_1)
        bottom_left_hbox.add_widget(button_2)


        # -------------------- MUSIC RECOMMENDATION SECTION (JC) --------------------
        # bottom right box -- music recommendation
        bottom_right_hbox = QVBoxLayout()                                       # create right vertical box
        group_box_4 = QGroupBox("General Recommendations")                      # create group box 4
        group_box_4_layout = QVBoxLayout()                                      # create layout for elements inside the Group Box

        # genre entry boc with submit button
        genre_label = QLabel("Enter a Genre:")                                  
        self.genre_le = QLineEdit()
        genre_submit_btn = QPushButton("Submit Genre")
        genre_submit_btn.clicked.connect(self.submit_genre)
        group_box_4_layout.add_widget(genre_label)
        group_box_4_layout.add_widget(self.genre_le)
        group_box_4_layout.add_widget(genre_submit_btn)

        # artist entry boc with submit button
        artist_label = QLabel("Enter an Artist:")
        self.artist_le = QLineEdit()
        artist_submit_btn = QPushButton("Submit Artist")
        artist_submit_btn.clicked.connect(self.submit_artist)
        group_box_4_layout.add_widget(artist_label)
        group_box_4_layout.add_widget(self.artist_le)
        group_box_4_layout.add_widget(artist_submit_btn)

        # dropdown menu for mood
        mood_label = QLabel("Select a Mood:")
        self.mood_dropdown = QComboBox()
        self.mood_dropdown.add_items(["","Happy", "Sad", "Energetic", "Chill", "Romantic", "Focus", "Sleep"])
        mood_submit_btn = QPushButton("Submit Mood")
        mood_submit_btn.clicked.connect(self.submit_mood)
        group_box_4_layout.add_widget(mood_label)
        group_box_4_layout.add_widget(self.mood_dropdown)
        group_box_4_layout.add_widget(mood_submit_btn)

        # dropdown menu for seasons
        season_label = QLabel("Select a Season:")
        self.season_dropdown = QComboBox()
        self.season_dropdown.add_items(["","Spring", "Summer", "Autumn", "Winter"])
        season_submit_btn = QPushButton("Submit Season")
        season_submit_btn.clicked.connect(self.submit_season)
        group_box_4_layout.add_widget(season_label)
        group_box_4_layout.add_widget(self.season_dropdown)
        group_box_4_layout.add_widget(season_submit_btn)

        # dropdown menu for regions
        region_label = QLabel("Select a Region:")
        self.region_dropdown = QComboBox()
        self.region_dropdown.add_items(["", "United States", "United Kingdom", "Canada", "Germany", "France", "Italy", "Spain", "Japan", "Australia", "Brazil", "Mexico", "India"])
        region_submit_btn = QPushButton("Submit Region")
        region_submit_btn.clicked.connect(self.submit_region)
        group_box_4_layout.add_widget(region_label)
        group_box_4_layout.add_widget(self.region_dropdown)
        group_box_4_layout.add_widget(region_submit_btn)

        # dropdown menu for weather
        weather_label = QLabel("Select Weather Condition:")
        self.weather_dropdown = QComboBox()
        self.weather_dropdown.add_items(["", "Sunny", "Rainy", "Cloudy", "Snowy", "Windy", "Foggy", "Stormy", "Clear Night"])
        weather_submit_btn = QPushButton("Submit Weather")
        weather_submit_btn.clicked.connect(self.submit_weather)
        group_box_4_layout.add_widget(weather_label)
        group_box_4_layout.add_widget(self.weather_dropdown)
        group_box_4_layout.add_widget(weather_submit_btn)

        # set layout
        group_box_4.set_layout(group_box_4_layout)                              # assign layout to the group box
        bottom_right_hbox.add_widget(group_box_4)                               # add group box to the right vertical box

        # -------------------- PUT TOGETHER LAYOUT --------------------
        # bottom horizontal layout -- holds 2 vertical boxes
        bottom_hbox = QHBoxLayout()
        bottom_hbox.add_layout(bottom_left_hbox, stretch=1)                     # equal width for bottom-left
        bottom_hbox.add_layout(bottom_right_hbox, stretch=1)                    # equal width for bottom-right

        # main layout -- vertical: top horizontal, bottom horizontal
        main_layout = QVBoxLayout()
        main_layout.add_layout(top_hbox, stretch=1)                             # equal height for top layout
        main_layout.add_layout(bottom_hbox, stretch=1)                          # equal height for bottom layout

        # set layout of the window
        self.set_layout(main_layout)                                            # set layout
        self.resize(1600, 800)                                                  # set window size
        self.window_title = "CST 205 FINAL PROJECT"                             # set window title

    # -------------------- ****** SLOT FUNCTIONS FOR BUTTONS ****** --------------------
    # @ everyone ---- each button needs a slot function 

    # -------------------- DAILY RECOMMENDATION SLOTS --------------------


    # -------------------- GENERAL RECOMMENDATIONS SLOTS --------------------
    @Slot()
    def submit_genre(self):
        genre = self.genre_le.text
        if not genre:                                                           # check if genre is empty
            self.genre_response_label.set_text("Please enter a valid genre.")   # show error
            return

        # open a new window to display results
        self.genre_results_window = GenreResultsWindow(genre)
        self.genre_results_window.show()                                        # open the window displaying the genre's songs

    @Slot()
    def submit_artist(self):
        artist = self.artist_le.text
        if not artist:
            self.artist_response_label.setText("Please enter a valid artist name.")
            return

        # open new window to display artist results
        self.artist_results_window = ArtistResultsWindow(artist)
        self.artist_results_window.show()

    @Slot()
    def submit_mood(self):
        mood = self.mood_dropdown.current_text
        if not mood:
            return

        # open a new window to display mood-based results
        self.mood_results_window = MoodResultsWindow(mood)
        self.mood_results_window.show()

    @Slot()
    def submit_season(self):
        season = self.season_dropdown.current_text
        if not season:
            return

        # open a new window to display season-based results
        self.season_results_window = SeasonResultsWindow(season)
        self.season_results_window.show()

    @Slot()
    def submit_region(self):
        region = self.region_dropdown.current_text
        if not region:
            return

        # open a new window to display region-based results
        self.region_results_window = RegionResultsWindow(region)
        self.region_results_window.show()

    @Slot()
    def submit_weather(self):
        weather = self.weather_dropdown.current_text
        if not weather:
            return

        # open a new window to display weather-based results
        self.weather_results_window = WeatherResultsWindow(weather)
        self.weather_results_window.show()
    # ---------------------------------------------------------------------

# --------------------- FUNCTION CALLS ---------------------
app = QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())