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
import api
import windows
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
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

# ------------------ NEW WINDOWS SECTION (MINSOL/SUNWOO)------------------
class HouseCleaningResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # Main layout
        layout = QVBoxLayout()
        cleaning_title_label = QLabel("Top 50 Random House Cleaning Songs")
        cleaning_title_label.alignment = Qt.AlignCenter
        cleaning_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(cleaning_title_label)

        # Text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # Fetch and display results
        api.fetch_house_cleaning_songs(self)
        self.set_layout(layout)

class WorkoutResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        workout_title_label = QLabel("Top 50 Random Workout Songs")
        workout_title_label.alignment = Qt.AlignCenter
        workout_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(workout_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_workout_songs(self)
        self.set_layout(layout)

# to do: meditation window

# to do: studying window

# to do: cooking window

# to do: party window

# to do: road trip window

# to do: gaming window

# to do: kids window

# ------------------ MAIN ------------------
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        top_hbox = QHBoxLayout()                                                # create horizontal box layout for the top

        # -------------------- ARTIST OF THE DAY SECTION (Juan) --------------------                
        group_box_1 = QGroupBox("Artist of the Day")                            # Create group box 1
        group_box_1_layout = QVBoxLayout()                                      # Create layout for Artist of the Day

        self.artist_header = QLabel("ARTIST OF THE DAY")
        self.artist_header.alignment = Qt.AlignCenter                           # align everything to the center
        self.artist_header.set_style_sheet("font-size: 40px; font-weight: bold;")            
        group_box_1_layout.add_widget(self.artist_header)                       # add widget to layout

        # artist Image
        self.artist_image = QLabel()
        self.artist_image.alignment = Qt.AlignCenter                            # align to center
        group_box_1_layout.add_widget(self.artist_image)                        # add widget to layout

        # artist Name
        self.artist_name_label = QLabel()
        self.artist_name_label.alignment = Qt.AlignCenter                       # align to center
        self.artist_name_label.set_style_sheet("font-size: 20px; font-weight: bold;")       # format text
        group_box_1_layout.add_widget(self.artist_name_label)                   # add widget to layout

        # top 5 Songs
        self.top_songs_label = QLabel()
        self.top_songs_label.alignment = Qt.AlignCenter                         # align to center
        self.top_songs_label.set_style_sheet("font-size: 20px;")                # format text
        group_box_1_layout.add_widget(self.top_songs_label)                     # add widget to layout

        group_box_1.set_layout(group_box_1_layout)                              # assign layout to the group box
        top_hbox.add_widget(group_box_1, stretch=1)                             # add group box 1 to the horizontal layout

        # display the artist of the day during initialization
        api.artist_of_the_day(self)

        # -------------------- DAILY RECOMMENDATION SECTION (Minsol / Sunwoo) --------------------
        group_box_2 = QGroupBox("Daily Recommendations")                        # create group box 2
        group_box_2_layout = QVBoxLayout()                                      # create layout for group box 2

        workout_button = QPushButton("Workout")                                 # create workout button
        workout_button.clicked.connect(self.fetch_workout_songs)
        group_box_2_layout.add_widget(workout_button)                           # add workout button to layout  

        house_cleaning_button = QPushButton("House Cleaning")                   # create house cleaning button
        house_cleaning_button.clicked.connect(self.open_house_cleaning_results_window)
        group_box_2_layout.add_widget(house_cleaning_button)                    # add house cleaning button to layout

        meditation_button = QPushButton("Meditation")                           # create meditation button
        # to do: link button to @SLOT 
        group_box_2_layout.add_widget(meditation_button)                        # add meditation button to layout

        studying_button = QPushButton("Studying")                               # create studying button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(studying_button)                          # add Studying button to layout

        cooking_button = QPushButton("Cooking")                                 # create cooking button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(cooking_button)                           # add Cooking button to layout

        party_button = QPushButton("Party")                                     # create party button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(party_button)                             # add party button to layout

        road_trip_button = QPushButton("Road Trip")                             # create road trip button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(road_trip_button)                         # add road trip button to layout

        gaming_button = QPushButton("Gaming")                                   # create gaming button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(gaming_button)                            # add gaming button to layout

        kids_button = QPushButton("Kids")                                       # create kids button
        # to do: link button to @SLOT
        group_box_2_layout.add_widget(kids_button)                              # add kids button to layout

        group_box_2.set_layout(group_box_2_layout)                              # assign layout to group box 2

        # add boxes to top row of boxes
        top_hbox.add_widget(group_box_2, stretch=1)                             # add group box 2 to the horizontal layout


        # -------------------- NEW RELEASE RECOMMENDATION BASED ON REGION (Minsol / Sunwoo) --------------------
        # bottom-left box -- playlist
        bottom_left_hbox = QVBoxLayout()                                        # create left vertical box
        group_box_3 = QGroupBox("Recommended New Release")                      # create group box 3
        bottom_left_hbox.add_widget(group_box_3)                                # add group box 3 to the left vertical box

        # New Releases Section inside Group Box
        new_release_layout = QVBoxLayout()                                      # layout for the new release content

        self.release_header = QLabel("POPULAR NEW RELEASE")
        self.release_header.alignment = Qt.AlignCenter                          # align everything to the center
        self.release_header.set_style_sheet("font-size: 40px; font-weight: bold;")            
        new_release_layout.add_widget(self.release_header)                      # add widget to layout

        # album cover
        self.new_release_image = QLabel()
        self.new_release_image.alignment = Qt.AlignCenter                       # align everything to the center
        new_release_layout.add_widget(self.new_release_image)                   # add widget to layout

        # album details
        self.new_release_details = QLabel()
        self.new_release_details.alignment = Qt.AlignCenter                     # align everything to the center
        self.new_release_details.set_style_sheet("font-size: 16px;")            
        new_release_layout.add_widget(self.new_release_details)                 # add widget to layout

        # refresh button
        self.refresh_button = QPushButton("Refresh")                            # create button
        self.refresh_button.clicked.connect(self.refresh_new_release)           # link button to refresh function in slot
        new_release_layout.add_widget(self.refresh_button)                      # add widget to layout

        # set the layout for the group box
        group_box_3.set_layout(new_release_layout)
        api.display_new_release(self)                   

        # -------------------- MUSIC RECOMMENDATION SECTION (JC) --------------------
        # bottom right box -- music recommendation
        bottom_right_hbox = QVBoxLayout()                                       # create right vertical box
        group_box_4 = QGroupBox("General Recommendations")                      # create group box 4
        group_box_4_layout = QVBoxLayout()                                      # create layout for elements inside the Group Box

        # genre entry boc with submit button
        genre_label = QLabel("Enter a Genre:")                                  
        self.genre_le = QLineEdit()
        genre_submit_btn = QPushButton("Submit Genre")                          # create button
        genre_submit_btn.clicked.connect(self.submit_genre)                     # link button to function in slot
        group_box_4_layout.add_widget(genre_label)                              # add widget to layout
        group_box_4_layout.add_widget(self.genre_le)                            # add widget to layout
        group_box_4_layout.add_widget(genre_submit_btn)                         # add widget to layout

        # artist entry boc with submit button
        artist_label = QLabel("Enter an Artist:")
        self.artist_le = QLineEdit()
        artist_submit_btn = QPushButton("Submit Artist")                        # create button
        artist_submit_btn.clicked.connect(self.submit_artist)                   # link button to function in slot
        group_box_4_layout.add_widget(artist_label)                             # add widget to layout
        group_box_4_layout.add_widget(self.artist_le)                           # add widget to layout
        group_box_4_layout.add_widget(artist_submit_btn)                        # add widget to layout

        # dropdown menu for mood
        mood_label = QLabel("Select a Mood:")
        self.mood_dropdown = QComboBox()                                        # create dropdown menu
        self.mood_dropdown.add_items(["","Happy", "Sad", "Energetic", "Calm", "Focus", "Sleep"])    # add items to dropdown menu
        mood_submit_btn = QPushButton("Submit Mood")                            # create button
        mood_submit_btn.clicked.connect(self.submit_mood)                       # link button to function in slot
        group_box_4_layout.add_widget(mood_label)                               # add widget to layout
        group_box_4_layout.add_widget(self.mood_dropdown)                       # add widget to layout
        group_box_4_layout.add_widget(mood_submit_btn)                          # add widget to layout

        # dropdown menu for seasons
        season_label = QLabel("Select a Season:")
        self.season_dropdown = QComboBox()                                      # create dropdown menu
        self.season_dropdown.add_items(["","Spring", "Summer", "Autumn", "Winter"]) # add items to dropdown menu
        season_submit_btn = QPushButton("Submit Season")                        # create button
        season_submit_btn.clicked.connect(self.submit_season)                   # link button to function in slot
        group_box_4_layout.add_widget(season_label)                             # add widget to layout
        group_box_4_layout.add_widget(self.season_dropdown)                     # add widget to layout
        group_box_4_layout.add_widget(season_submit_btn)                        # add widget to layout

        # dropdown menu for regions
        region_label = QLabel("Select a Region:")
        self.region_dropdown = QComboBox()                                      # create dropdown menu
        self.region_dropdown.add_items(["", "USA", "Latin America", "Europe", "Asia", "Africa"])    # add items to dropdown menu
        region_submit_btn = QPushButton("Submit Region")                        # create button
        region_submit_btn.clicked.connect(self.submit_region)                   # link button to function in slot
        group_box_4_layout.add_widget(region_label)                                 
        group_box_4_layout.add_widget(self.region_dropdown)                     # add widget to layout
        group_box_4_layout.add_widget(region_submit_btn)                        # add widget to layout

        # dropdown menu for weather
        weather_label = QLabel("Select Weather Condition:") 
        self.weather_dropdown = QComboBox()                                     # create dropdown menu
        self.weather_dropdown.add_items(["", "Sunny", "Rainy", "Cloudy", "Snowy", "Stormy", "Clear Night"]) # add items to dropdown menu
        weather_submit_btn = QPushButton("Submit Weather")                      # create button
        weather_submit_btn.clicked.connect(self.submit_weather)                 # link button to function in slot
        group_box_4_layout.add_widget(weather_label)                            # add widget to layout
        group_box_4_layout.add_widget(self.weather_dropdown)                    # add widget to layout
        group_box_4_layout.add_widget(weather_submit_btn)                       # add widget to layout

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

    # -------------------- NEW RELEASE BY REGION -------------------- 
    @Slot()
    def refresh_new_release(self):                                              
        api.display_new_release(self)

    # -------------------- DAILY RECOMMENDATION SLOTS (Minsol/Sunwoo) --------------------
    @Slot()
    def fetch_workout_songs(self):
        self.workout_results_window = WorkoutResultsWindow()                    # render window
        self.workout_results_window.show()                                      # show window

    @Slot()
    def open_house_cleaning_results_window(self):
        self.house_cleaning_results_window = HouseCleaningResultsWindow()       # render window
        self.house_cleaning_results_window.show()                               # show window

    # to do - meditation slot

    # to do - studying slot

    # to do - cooking slot

    # to do - party slot

    # to do - road trip slot

    # to do - gaming slot

    # to do - kids slot
    
    # -------------------- GENERAL RECOMMENDATIONS SLOTS --------------------
    @Slot()
    def submit_genre(self):
        genre = self.genre_le.text
        if not genre:                                                           # check if genre is empty
            self.genre_response_label.set_text("Please enter a valid genre.")   # show error
            return                                                              # so blank window doesnt open

        # open a new window to display results
        self.genre_results_window = windows.GenreResultsWindow(genre)
        self.genre_results_window.show()                                        # open the window displaying the genre's songs

    @Slot()
    def submit_artist(self):
        artist = self.artist_le.text
        if not artist:
            self.artist_response_label.setText("Please enter a valid artist name.")
            return                                                              # so blank window doesnt open

        # open new window to display artist results
        self.artist_results_window = windows.ArtistResultsWindow(artist)        # render window
        self.artist_results_window.show()                                       # show window

    @Slot()
    def submit_mood(self):
        mood = self.mood_dropdown.current_text
        if not mood:                                                            # so blank window doesnt open
            return
        # open a new window to display mood-based results
        self.mood_results_window = windows.MoodResultsWindow(mood)              # render window
        self.mood_results_window.show()                                         # show window

    @Slot()
    def submit_season(self):
        season = self.season_dropdown.current_text                              
        if not season:                                                          
            return                                                              # so blank window doesnt open
        # open a new window to display season-based results
        self.season_results_window = windows.SeasonResultsWindow(season)        # render window
        self.season_results_window.show()                                       # show window

    @Slot()
    def submit_region(self):
        region = self.region_dropdown.current_text
        if not region:
            return                                                              # so blank window doesnt open
        # open a new window to display region-based results
        self.region_results_window = windows.RegionResultsWindow(region)        # render window
        self.region_results_window.show()                                       # show window

    @Slot()
    def submit_weather(self):
        weather = self.weather_dropdown.current_text
        if not weather:
            return                                                              # so blank window doesnt open
        # open a new window to display weather-based results                    # render window
        self.weather_results_window = windows.WeatherResultsWindow(weather)     # show window
        self.weather_results_window.show()
    # ---------------------------------------------------------------------

# --------------------- FUNCTION CALLS ---------------------
app = QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())