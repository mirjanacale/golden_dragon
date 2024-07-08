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

        This method moves the dragon in the specified direction, handles gold collection, and detects collisions.
        """
        
        # Get the current coordinates of the dragon
        x, y = self.dragon.coordinates[0]

        # Define the direction offsets for each possible direction
        direction_offsets = {
            "up": (0, -SPACE_SIZE),
            "down": (0, SPACE_SIZE),
            "left": (-SPACE_SIZE, 0),
            "right": (SPACE_SIZE, 0),
        }
        
        # Get the movement offset for the current direction
        movement_offset = direction_offsets.get(self.direction)
        
        # If the direction is invalid, ignore this turn
        if not movement_offset:
            print(f"Invalid direction: {self.direction}. Ignoring this turn.")
            return

        # Update the dragon's coordinates
        x += movement_offset[0]
        y += movement_offset[1]
        self.dragon.coordinates.insert(0, [x, y])

        # Check if the dragon has collected gold
        if x == self.gold.coordinates[0] and y == self.gold.coordinates[1]:
            self.score += 1
            print(f"Score: {self.score}")
            self.gold = Gold()  # Generate a new piece of gold
            print("Gold collected. New gold coordinates:", self.gold.coordinates)
        else:
            self.dragon.coordinates.pop()  # Remove the last dragon coordinate

        # Check for collisions and end the game if necessary
        if self.checkCollisions():
            self.gameOver()
            return

        # Update the game display
        self.update()
        
    def checkCollisions(self):
         """
        Check for collisions between the dragon and the game boundaries or other body parts.

        This method checks if the dragon has moved outside the game boundaries or collided with any
        of its own body parts. It returns True if a collision is detected, indicating that the game
        should end. Otherwise, it returns False.

        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        
         x, y = self.dragon.coordinates[0]

         if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True

         for body_part in self.dragon.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

         return False
     
    def gameOver(self):
        print("GAME OVER")
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score(self.high_score)
        print("High Score:", self.high_score)
     

        
        









    





