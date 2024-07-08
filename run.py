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
        
class DragonGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        # Initialize the user interface
        print("Initializing UI...")

        # Set the geometry of the window
        self.setGeometry(300, 300, 800, 500)
        print("Geometry set.")

        # Set the window title
        self.setWindowTitle('Dragon Game')
        print("Window title set.")

        # Create a new dragon
        self.dragon = Dragon()
        print("Dragon created.")

        # Create a new piece of gold
        self.gold = Gold()
        print("Gold created.")

        # Initialize the score to 0
        self.score = 0
        print("Score initialized to 0.")

        # Load the high score from file
        self.high_score = self.load_high_score()
        print("High score loaded.")

        # Set the initial direction of the dragon to up
        self.direction = "up"
        print("Direction set to 'up'.")

        # Show the window
        self.show()
        print("UI shown.")

        # Print a message to indicate that the UI has been initialized
        print("UI initialization complete.")
    
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawGame(qp)
        qp.end()    
    
        









    

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass




score = 0
direction = 'down'







