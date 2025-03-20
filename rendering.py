import pygame
import math
from pygame import *
import random


def rendering(screen,player_pos,square_pos):
    pygame.draw.rect(screen,"green",pygame.Rect(player_pos.x,player_pos.y,20,20))
    pygame.draw.rect(screen,"red",pygame.Rect(square_pos[0],square_pos[1],20,20))
