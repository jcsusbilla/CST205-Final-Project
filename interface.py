# CST 205
# TEAM 11483
# MUSIC RECOMMENDATION APP

# IMPORTS
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QLineEdit, QTextEdit, QPushButton, QSpacerItem, QSizePolicy
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import os
import api
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --------------------- GUI INTERFACE ---------------------

# set up spotify API credentials and authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="ccde7e87d847406385d72de3862c4027",
    client_secret="a49033b7c5ff4ec8951c6a96d60f4519",
    redirect_uri="http://localhost:8080",
    scope='user-library-read'
))

class GenreResultsWindow(QWidget):
    def __init__(self, genre):
        super().__init__()
        self.resize(600, 400)
        layout = QVBoxLayout()

        # header label
        results_label = QLabel(f"Top Artists and Songs for the {genre} Genre")
        layout.add_widget(results_label)

        # area to display results
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # get results
        self.fetch_and_display_results(genre)
        self.set_layout(layout)

    def fetch_and_display_results(self, genre):
        # fetch top 5 artists for specific genre and get their top 10 songs
        # step 1: search for artists in the given genre
        results = sp.search(q=f"genre:{genre}", type="artist", limit=5)             # only pull the first 5 artists
        artists = results.get("artists", {}).get("items", [])

        if not artists:
            self.results_text.set_text(f"No artists found for genre: {genre}.")
            return

        # step 2: get the top 10 songs for each artist
        output = []
        for artist in artists:
            artist_name = artist["name"]
            artist_id = artist["id"]
            output.append(f"Artist: {artist_name}")

            # fetch top 10 songs
            top_tracks = sp.artist_top_tracks(artist_id, country="US").get("tracks", [])
            for track in top_tracks[:10]:
                output.append(f"  - {track['name']}")

            output.append("")                                                   # add a blank line between artists

        # step 3: display result
        self.results_text.set_text("\n".join(output))

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # top horizontal box -- group box 1 and group box 2)
        top_hbox = QHBoxLayout()                                                # create horizontal box layout for the top
        group_box_1 = QGroupBox("Artist of the Day")                            # create group box 1
        group_box_2 = QGroupBox("Daily Recommendations")                        # create group box 2
        top_hbox.add_widget(group_box_1, stretch=1)                             # add group box 1 to the horizontal layout
        top_hbox.add_widget(group_box_2, stretch=1)                             # add group box 2 to the horizontal layout

        # bottom-left box -- playlist
        bottom_left_hbox = QVBoxLayout()                                        # create left vertical box
        group_box_3 = QGroupBox("Most Recent Playlist")                         # create group box 3
        bottom_left_hbox.add_widget(group_box_3)                                # add group box 3 to the left vertical box

        # buttons under the playlist box
        button_1 = QPushButton("Create Playlist")
        button_2 = QPushButton("View Playlists")
        bottom_left_hbox.add_widget(button_1)
        bottom_left_hbox.add_widget(button_2)

        # bottom right box -- music recommendation
        bottom_right_hbox = QVBoxLayout()                                       # create right vertical box
        group_box_4 = QGroupBox("Recommended")                                  # create group box 4
        group_box_4_layout = QVBoxLayout()                                      # create layout for elements inside the Group Box

        # genre entry boc with submit button
        genre_label = QLabel("Enter a Genre:")
        self.genre_le = QLineEdit()
        self.genre_le.minimum_width = 250
        genre_submit_btn = QPushButton("Submit Genre")
        self.genre_response_label = QLabel('')                                  # label for genre response
        genre_submit_btn.clicked.connect(self.submit_genre)

        # artist entry boc with submit button
        artist_label = QLabel("Enter an Artist:")
        self.artist_le = QLineEdit()
        self.artist_le.minimum_width = 250
        artist_submit_btn = QPushButton("Submit Artist")
        self.artist_response_label = QLabel('')                                 # label for artist response
        artist_submit_btn.clicked.connect(self.submit_artist)

        # Add Genre inputs and response to layout
        group_box_4_layout.add_widget(genre_label)
        group_box_4_layout.add_widget(self.genre_le)
        group_box_4_layout.add_widget(genre_submit_btn)
        group_box_4_layout.add_widget(self.genre_response_label)

        # Add Artist inputs and response to layout
        group_box_4_layout.add_widget(artist_label)
        group_box_4_layout.add_widget(self.artist_le)
        group_box_4_layout.add_widget(artist_submit_btn)
        group_box_4_layout.add_widget(self.artist_response_label)

        # Add remaining buttons with spacers
        mood_button = QPushButton("Mood")
        region_button = QPushButton("Region")
        weather_button = QPushButton("Weather")
        season_button = QPushButton("Season")

        group_box_4_layout.add_widget(mood_button)
        group_box_4_layout.add_spacer_item(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        group_box_4_layout.add_widget(region_button)
        group_box_4_layout.add_spacer_item(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        group_box_4_layout.add_widget(weather_button)
        group_box_4_layout.add_spacer_item(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        group_box_4_layout.add_widget(season_button)

        group_box_4.set_layout(group_box_4_layout)                              # assign layout to the group box
        bottom_right_hbox.add_widget(group_box_4)                               # add group box to the right vertical box

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

    @Slot()
    def submit_genre(self):
        genre = self.genre_le.text
        if not genre:                                                           # check if genre is empty
            self.genre_response_label.set_text("Please enter a valid genre.")   # show error
            return

        # open a new window to display results
        self.genre_results_window = GenreResultsWindow(genre)
        self.genre_results_window.show()

    @Slot()
    def submit_artist(self):
        artist = self.artist_le.text
        self.artist_response_label.set_text(f"Favorite Artist: {artist}")

# --------------------- FUNCTION CALLS ---------------------
app = QApplication([])
win = MyWindow()
win.show()
sys.exit(app.exec())