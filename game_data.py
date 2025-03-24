import pygame
import random
from pygame import *

class GData:
    def __init__(self):    
        
        pygame.init()
        pygame.display.set_caption("Snake")
 
        self.screen = pygame.display.set_mode((1920,1080), FULLSCREEN)
        self.screen.fill((0,0,0))

        self.clock = pygame.time.Clock()
        self.clock.tick(10)

        self.running = True

        self.font = pygame.font.Font(None, 50)

        self.alg = 0
        self.menu_showed = False

