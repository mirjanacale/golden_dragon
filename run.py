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
        
    def drawGame(self, qp):
        """
        Draws the game on the QPainter object.

        Args:
            qp (QPainter): The QPainter object used to draw the game.
        """
        
        qp.setBrush(QBrush(QColor(BACKGROUND_COLOR)))
        qp.drawRect(0, 0, 800, 500)

        qp.setBrush(QBrush(QColor(DRAGON_COLOR)))
        for x, y in self.dragon.coordinates:
            qp.drawRect(x, y, SPACE_SIZE, SPACE_SIZE)

        qp.setBrush(QBrush(QColor(GOLD_COLOR)))
        qp.drawRect(self.gold.coordinates[0], self.gold.coordinates[1], SPACE_SIZE, SPACE_SIZE)
        
    def keyPressEvent(self, e):
        print("Key pressed:", e.key())
        if e.key() == Qt.Key_Up:
            self.direction = "up"
            print("Direction set to 'up'.")
        elif e.key() == Qt.Key_Down:
            self.direction = "down"
            print("Direction set to 'down'.")
        elif e.key() == Qt.Key_Left:
            self.direction = "left"
            print("Direction set to 'left'.")
        elif e.key() == Qt.Key_Right:
            self.direction = "right"
            print("Direction set to 'right'.")
            
        #Call the nextTurn function
        self.nextTurn()
        print("Next turn called.")
        
    def nextTurn(self):
         """
        Updates the game state for the next turn.

        This method moves the dragon in the specified direction and handles gold collection and collision detection.
        """
         x, y = self.dragon.coordinates[0]

         direction_offsets = {
            "up": (0, -SPACE_SIZE),
            "down": (0, SPACE_SIZE),
            "left": (-SPACE_SIZE, 0),
            "right": (SPACE_SIZE, 0),
        }
        
         movement_offset = direction_offsets.get(self.direction)
         if not movement_offset:
            print(f"Invalid direction: {self.direction}. Ignoring this turn.")
            return

         x += movement_offset[0]
         y += movement_offset[1]
         self.dragon.coordinates.insert(0, [x, y])

         if x == self.gold.coordinates[0] and y == self.gold.coordinates[1]:
            self.score += 1
            print(f"Score: {self.score}")
            self.gold = Gold()
            print("Gold collected. New gold coordinates:", self.gold.coordinates)
         else:
            self.dragon.coordinates.pop()

         if self.checkCollisions():
            self.gameOver()
            return

         self.update()

        
        









    





