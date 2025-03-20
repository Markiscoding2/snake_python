import pygame
import math
from pygame import *
import mov_func
import rendering
import random


pygame.init()

screen = pygame.display.set_mode((1920,1080), FULLSCREEN)

pygame.display.set_caption("Snake")

screen.fill((0,0,0))

clock = pygame.time.Clock()

clock.tick(60)

running = True


player_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
square_pos = Vector2(random.randrange(0,1920,20),random.randrange(0,1080,20))

last_pressed_keys = [0,0,0,0]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    mov_func.player_and_apple_movement(player_pos,square_pos)
    
    rendering.rendering(screen,player_pos,square_pos)

    current_pressed_key = pygame.key.get_pressed()
    
    if current_pressed_key[pygame.K_ESCAPE]:
        running = False
    
    mov_func.current_direction(last_pressed_keys,current_pressed_key)

    pygame.display.flip()

    if(last_pressed_keys[0]):
        player_pos.x -= 20
    if(last_pressed_keys[1]):  
        player_pos.x += 20
    if(last_pressed_keys[2]):
        player_pos.y -= 20
    if(last_pressed_keys[3]):
        player_pos.y += 20
        

    clock.tick(10)

pygame.quit()