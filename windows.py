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