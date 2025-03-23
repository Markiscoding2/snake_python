import pygame
import math
from pygame import *
import mov_func
import rendering
import random


#add teleportation when u hit the wall
#add the body of the snake
#add the colision between the body and the head 
#add a menu 



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

elements = [] 

last_pressed_keys = [0,0,0,0]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    score=mov_func.player_and_apple_movement(player_pos,square_pos,score,elements)    
    running = mov_func.current_direction(last_pressed_keys,player_pos,running,elements)
    rendering.rendering(screen,player_pos,square_pos,font,score,elements)


    pygame.display.flip()
    clock.tick(10)
pygame.quit()