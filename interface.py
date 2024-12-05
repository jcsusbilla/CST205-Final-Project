# CST 205
# TEAM 11483
# MUSIC RECOMMENDATION APP

# IMPORTS
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QLineEdit, QComboBox, QPushButton
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import os
import api

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
genre_to_search = "Reggae"  # Change the genre as needed
api.get_top_tracks_by_genre(genre_to_search)
# --------------------- GUI INTERFACE ---------------------

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # top horizontal box (group box 1)
        top_hbox = QHBoxLayout()                            # create horizontal box layout for the top
        group_box_1 = QGroupBox('Find Music')               # create Group Box 1
        top_hbox.add_widget(group_box_1)                    # add Group Box 1 to the horizontal layout

        # bottom two vertical boxes (group box 2 and group box 3)
        left_vbox = QVBoxLayout()                           # create left vertical box
        group_box_2 = QGroupBox('Most Recent Playlist')     # create Group Box 2
        left_vbox.add_widget(group_box_2)                   # add Group Box 2 to the left vertical box

        right_vbox = QVBoxLayout()                          # create right vertical box
        group_box_3 = QGroupBox('Recommended')              # create Group Box 3
        right_vbox.add_widget(group_box_3)                  # add Group Box 3 to the right vertical box

        # bottom horizontal layout (holds 2 vertical boxes)
        bottom_hbox = QHBoxLayout()
            # add left vertical box 
        bottom_hbox.add_layout(left_vbox)                   # PLAYLIST SECTION
            # add right vertical box                
        bottom_hbox.add_layout(right_vbox)                  # RECOMMENDED MUSIC

        # Add buttons to the left vertical box
        button_1 = QPushButton("Create Playlist")
        button_2 = QPushButton("View Playlists")
        left_vbox.add_widget(button_1)
        left_vbox.add_widget(button_2)

        # main layout (vertical: top horizontal, bottom horizontal)
        main_layout = QVBoxLayout()
            # add top horizontal layout 
        main_layout.add_layout(top_hbox)                    # SEARCH AREA
            # add bottom horizontal layout                    
        main_layout.add_layout(bottom_hbox)                 


        # Set layout of the window
        self.set_layout(main_layout)                        # set layout
        self.resize(1500, 800)                              # set window size
        self.window_title = "CST 205 FINAL PROJECT"         # set window title

    # @Slot() 
    # def open_win(self):
    #     i = self.dropdown.current_index                                 # save user manipulation selection
    #     user_input = self.line_edit.text                                # save user input search term
    #     self.new_win = NewWindow(my_list[i], user_input)                # open window
    #     self.new_win.show()

# --------------------- FUNCTION CALLS ---------------------
# app = QApplication([])
# win = MyWindow()
# win.show()
# sys.exit(app.exec())

