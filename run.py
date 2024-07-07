#imports
import os
import random
import argparse



GAME_WIDTH = 800
GAME_HEIGHT = 500
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
DRAGON_COLOR = "#00FF00"
GOLD_COLOR = "#ffD700"
BACKGROUND_COLOR = "#000000"
HIGH_SCORE_FILE = "high_score.txt"


class Dragon:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        start_x = GAME_WIDTH // 2
        start_y = GAME_HEIGHT // 2
        # Loop through the number of body parts and add the coordinates of each body part to the list
        for i in range(0, BODY_PARTS):
            y = start_y + i * SPACE_SIZE
            
            self.coordinates.append([start_x, y])
    
    

class Gold:
     def __init__(self):
        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE
        self.coordinates = [x, y]

    
    

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







