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

# -------------------------------- DAILY RECOMMENDATION WINDOWS --------------------------------
class HouseCleaningResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # Main layout
        layout = QVBoxLayout()
        cleaning_title_label = QLabel("50 House Cleaning Songs")
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
        workout_title_label = QLabel("50 Workout Songs")
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

class MeditationResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        meditation_title_label = QLabel("50 Meditation Songs")
        meditation_title_label.alignment = Qt.AlignCenter
        meditation_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(meditation_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_meditation_songs(self)
        self.set_layout(layout)

class StudyingResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        studying_title_label = QLabel("50 Studying Songs")
        studying_title_label.alignment = Qt.AlignCenter
        studying_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(studying_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_studying_songs(self)
        self.set_layout(layout)

class CookingResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        cooking_title_label = QLabel("50 Cooking Songs")
        cooking_title_label.alignment = Qt.AlignCenter
        cooking_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(cooking_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_cooking_songs(self)
        self.set_layout(layout)

class PartyResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        party_title_label = QLabel("50 Party Songs")
        party_title_label.alignment = Qt.AlignCenter
        party_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(party_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_party_songs(self)
        self.set_layout(layout)

class RoadTripResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        road_trip_title_label = QLabel("50 Road Trip Songs")
        road_trip_title_label.alignment = Qt.AlignCenter
        road_trip_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(road_trip_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_road_trip_songs(self)
        self.set_layout(layout)

class GamingResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        gaming_title_label = QLabel("50 Gaming Songs")
        gaming_title_label.alignment = Qt.AlignCenter
        gaming_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(gaming_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_gaming_songs(self)
        self.set_layout(layout)

class KidsResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 1000)

        # layout
        layout = QVBoxLayout()
        kids_title_label = QLabel("50 Kids Songs")
        kids_title_label.alignment = Qt.AlignCenter
        kids_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(kids_title_label)

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True
        layout.add_widget(self.results_text)

        # display results
        api.fetch_kids_songs(self)
        self.set_layout(layout)




# -------------------------------- GENERAL RECOMMENDATIONS WINDOWS --------------------------------
# WINDOW TO DISPLAY 50 SONGS BASED ON WEATHER
class WeatherResultsWindow(QWidget):
    def __init__(self, weather):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size

        # layout
        layout = QVBoxLayout()
        weather_title_label = QLabel(f"50 Songs for {weather} Weather")
        weather_title_label.alignment = Qt.AlignCenter                                      # align to the center
        weather_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")          # set text style
        layout.add_widget(weather_title_label)                                              # add widget to layout

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout

        # display results
        api.weather_results(self, weather)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON REGION
class RegionResultsWindow(QWidget):
    def __init__(self, region):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size

        # layout
        layout = QVBoxLayout()
        region_title_label = QLabel(f"50 Songs for {region}")
        region_title_label.alignment = Qt.AlignCenter                                       # align to the center
        region_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")           # set text style
        layout.add_widget(region_title_label)                                               # add widget to layout

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout

        # display results
        api.region_results(self, region)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON SEASON
class SeasonResultsWindow(QWidget):
    def __init__(self, season):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size

        # Main layout
        layout = QVBoxLayout()
        season_title_label = QLabel(f"50 Songs for {season}")
        season_title_label.alignment = Qt.AlignCenter                                       # align to the center
        season_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")           # set text style
        layout.add_widget(season_title_label)                                               # add widget to layout

        # Text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout

        # Fetch and display results
        api.season_results(self, season)
        self.set_layout(layout)

# WINDOW TO DISPLAY 50 SONGS BASED ON MOOD
class MoodResultsWindow(QWidget):
    def __init__(self, mood):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size

        # layout
        layout = QVBoxLayout()
        mood_title_label = QLabel(f"50 Songs for {mood} Mood")  
        mood_title_label.alignment = Qt.AlignCenter                                         # align to the center
        mood_title_label.set_style_sheet("font-size: 40px; font-weight: bold;")             # set text style
        layout.add_widget(mood_title_label)                                                 # add widget to layout

        # text area for song list
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout

        # display results
        api.mood_results(self, mood)
        self.set_layout(layout)

# WINDOW TO DISPLAY SPECIFIED ARTIST AND THEIR TOP 10 SONGS. ALSO SHOW AN IMAGE AND ALBUMS
class ArtistResultsWindow(QWidget):
    def __init__(self, artist):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size

        # main layout
        layout = QVBoxLayout()
        artist = artist.title()                                                             # make sure it is always capitalized
        artist_name_label = QLabel(f"{artist}")
        artist_name_label.alignment = Qt.AlignCenter                                        # align to the center
        artist_name_label.set_style_sheet("font-size: 75px; font-weight: bold;")            # set text style
        layout.add_widget(artist_name_label)                                                # add widget to layout
        
        # artist image placeholder
        self.image_label = QLabel()                                                         # initialize the image label here
        self.image_label.alignment = Qt.AlignCenter                                         # align to the center
        layout.add_widget(self.image_label)                                                 # add widget to layout

        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout

        self.set_layout(layout)                                                             # set layout

        # display artist info
        api.artist_results(self, artist)

# WINDOW TO DISPLAY GENRE'S TOP 5 ARTISTS AND EACH ARTIST TOP 10 SONGS
class GenreResultsWindow(QWidget):  
    def __init__(self, genre):
        super().__init__()
        self.resize(800, 1000)                                                              # set window size
        layout = QVBoxLayout()                                                              # init layout
        genre = genre.title()                                                               # make sure it is always capitalized

        # HEADER / WINDOW TITLE
        genre_results_label = QLabel(f"Top Artists and Songs for the {genre} Genre")
        genre_results_label.alignment = Qt.AlignCenter
        genre_results_label.set_style_sheet("font-size: 40px; font-weight: bold;")
        layout.add_widget(genre_results_label)                                              # add widget to layout

        # area to display results
        self.results_text = QTextEdit()
        self.results_text.read_only = True                                                  # set to read only
        layout.add_widget(self.results_text)                                                # add widget to layout
        self.results_text.alignment = Qt.AlignCenter                                        # align to the center

        # get results
        api.genre_results(self, genre)
        self.set_layout(layout)