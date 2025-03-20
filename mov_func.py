import pygame
import math
from pygame import *
import random

def current_direction(keys2,keys):
    if keys[pygame.K_a]:
        keys2[0] = True
        keys2[1] = False
        keys2[2] = False
        keys2[3] = False
    elif keys[pygame.K_d]:
        keys2[0] = False
        keys2[1] = True
        keys2[2] = False
        keys2[3] = False
    elif keys[pygame.K_w]:    
        keys2[0] = False
        keys2[1] = False
        keys2[2] = True
        keys2[3] = False
    elif keys[pygame.K_s]:
        keys2[0] = False
        keys2[1] = False
        keys2[2] = False
        keys2[3] = True

def player_and_apple_movement(player_pos,square_pos):
    if player_pos.x == square_pos[0] and player_pos.y == square_pos[1]: 
        square_pos[0] = random.randrange(0,1920,20)
        square_pos[1] = random.randrange(0,1080,20)