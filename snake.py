import pygame
import math
from pygame import *
import mov_func


#initialize pygame
pygame.init()
screen = pygame.display.set_mode((1920,1080), FULLSCREEN)
#set the title of the window
pygame.display.set_caption("Snake")
#set the background color
screen.fill((0,0,0))
#set the fps
clock = pygame.time.Clock()
clock.tick(60)
running = True

dt = 0 #delta time / the difference in time since the last frame
player_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
last_pressed_keys = [0,0,0,0]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # check for escape key to quit
    screen.fill("black")
    pygame.draw.rect(screen,"green",pygame.Rect(player_pos.x,player_pos.y,20,20))
    current_pressed_key = pygame.key.get_pressed()
    if current_pressed_key[pygame.K_ESCAPE]:
        running = False
    
    mov_func.movement(last_pressed_keys,current_pressed_key)

    pygame.display.flip()

    if(last_pressed_keys[0]):
        player_pos.x -= 5
    if(last_pressed_keys[1]):  
        player_pos.x += 5
    if(last_pressed_keys[2]):
        player_pos.y -= 5
    if(last_pressed_keys[3]):
        player_pos.y += 5
        

    dt = clock.tick(30)/1000  # limits FPS to 60

pygame.quit()