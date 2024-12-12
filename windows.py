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

# --------------------- JC's Windows ---------------------
