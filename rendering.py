import pygame
import math
from pygame import *
import random


def rendering(screen,player_pos,square_pos,font,score):
    pygame.draw.rect(screen,"green",pygame.Rect(player_pos.x,player_pos.y,20,20))
    pygame.draw.rect(screen,"red",pygame.Rect(square_pos[0],square_pos[1],20,20))
    screen.blit(font.render('Score:' + str(score), True, (255, 255, 255)), (20, 20))