import pygame
import math
from pygame import *
import random

def current_direction(last_pressed_keys,player_pos,running,other_player_segments):
    current_pressed_key = pygame.key.get_pressed()
    
    if current_pressed_key[pygame.K_ESCAPE]:
        running = False
    if current_pressed_key[pygame.K_a] and last_pressed_keys[1] == False or len(other_player_segments) == 0 and current_pressed_key[pygame.K_a]:
        last_pressed_keys[0] = True
        last_pressed_keys[1] = False
        last_pressed_keys[2] = False
        last_pressed_keys[3] = False
    if current_pressed_key[pygame.K_d] and last_pressed_keys[0] == False or len(other_player_segments) == 0 and current_pressed_key[pygame.K_d]:
        last_pressed_keys[0] = False
        last_pressed_keys[1] = True
        last_pressed_keys[2] = False
        last_pressed_keys[3] = False
    if current_pressed_key[pygame.K_w] and last_pressed_keys[3] == False or len(other_player_segments) == 0 and current_pressed_key[pygame.K_w]:     
        last_pressed_keys[0] = False
        last_pressed_keys[1] = False
        last_pressed_keys[2] = True
        last_pressed_keys[3] = False
    if current_pressed_key[pygame.K_s] and last_pressed_keys[2] == False or len(other_player_segments) == 0 and current_pressed_key[pygame.K_s]: 
        last_pressed_keys[0] = False
        last_pressed_keys[1] = False
        last_pressed_keys[2] = False
        last_pressed_keys[3] = True

    player_pos_changed = False
    old_plr_x=player_pos.x
    old_plr_y=player_pos.y
    if(last_pressed_keys[0] and player_pos.x > 20 ):
        player_pos.x -= 20
        player_pos_changed = True
    if(last_pressed_keys[1] and player_pos.x < 1900):  
        player_pos.x += 20
        player_pos_changed = True
    if(last_pressed_keys[2] and player_pos.y > 20):
        player_pos.y -= 20
        player_pos_changed = True
    if(last_pressed_keys[3] and player_pos.y < 1060):
        player_pos.y += 20
        player_pos_changed = True
    
    if player_pos_changed :
        if len(other_player_segments) != 0:
            for i in range(len(other_player_segments) - 1, 0, -1):
                other_player_segments[i] = other_player_segments[i-1]
            other_player_segments[0]=[old_plr_x,old_plr_y]

    
    return running
    
def player_and_apple_movement(player_pos,square_pos,score,other_player_segments):
    if player_pos.x == square_pos[0] and player_pos.y == square_pos[1]: 
        square_pos[0] = random.randrange(20,1900,20)
        square_pos[1] = random.randrange(20,1060,20)
        score+=1
        other_player_segments.append([player_pos.x,player_pos.y])
    return score
        