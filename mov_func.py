import pygame
import math
from pygame import *


def movement(keys2,keys):
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