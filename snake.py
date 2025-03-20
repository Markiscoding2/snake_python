import pygame
import math
from pygame import *
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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # check for escape key to quit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()