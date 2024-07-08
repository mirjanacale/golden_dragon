#imports
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect
import os
import random

BACKGROUND_COLOR = Qt.white
DRAGON_COLOR = Qt.red
GOLD_COLOR = Qt.yellow
SPACE_SIZE = 10
GAME_WIDTH = 800
GAME_HEIGHT = 500
HIGH_SCORE_FILE = 'high_score.txt'

class Dragon:
    def __init__(self):
        self.coordinates = [[400, 250], [390, 250], [380, 250]] 
        # initial coordinates of the dragon

class Gold:
    def __init__(self):
        self.coordinates = [random.randint(0, 790), random.randint(0, 490)]  
        # random initial coordinates of the gold








def next_turn():
    
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass




score = 0
direction = 'down'







