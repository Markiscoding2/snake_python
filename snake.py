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

font = pygame.font.Font(None, 50)  # Use default font, size 50
score=0

last_pressed_keys = [0,0,0,0]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    score=mov_func.player_and_apple_movement(player_pos,square_pos,score)

    rendering.rendering(screen,player_pos,square_pos,font,score)
    
    running = mov_func.current_direction(last_pressed_keys,player_pos,running)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()