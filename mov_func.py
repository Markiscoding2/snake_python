import pygame
import math
from pygame import *
import random

def current_direction(last_pressed_keys,player_pos):
    current_pressed_key = pygame.key.get_pressed()
    
    if current_pressed_key[pygame.K_ESCAPE]:
        running = False
        pygame.quit()
    if current_pressed_key[pygame.K_a]:
        last_pressed_keys[0] = True
        last_pressed_keys[1] = False
        last_pressed_keys[2] = False
        last_pressed_keys[3] = False
    elif current_pressed_key[pygame.K_d]:
        last_pressed_keys[0] = False
        last_pressed_keys[1] = True
        last_pressed_keys[2] = False
        last_pressed_keys[3] = False
    elif current_pressed_key[pygame.K_w]:    
        last_pressed_keys[0] = False
        last_pressed_keys[1] = False
        last_pressed_keys[2] = True
        last_pressed_keys[3] = False
    elif current_pressed_key[pygame.K_s]:
        last_pressed_keys[0] = False
        last_pressed_keys[1] = False
        last_pressed_keys[2] = False
        last_pressed_keys[3] = True
    if(last_pressed_keys[0]):
        player_pos.x -= 20
    if(last_pressed_keys[1]):  
        player_pos.x += 20
    if(last_pressed_keys[2]):
        player_pos.y -= 20
    if(last_pressed_keys[3]):
        player_pos.y += 20
    
def player_and_apple_movement(player_pos,square_pos,score):
    if player_pos.x == square_pos[0] and player_pos.y == square_pos[1]: 
        square_pos[0] = random.randrange(0,1920,20)
        square_pos[1] = random.randrange(0,1080,20)
        score+=1
    return score
        