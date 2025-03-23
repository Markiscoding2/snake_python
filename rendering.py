import pygame
import math
from pygame import *
import random


def rendering(screen,player_pos,square_pos,font,score,elements):
    pygame.draw.rect(screen,"red",pygame.Rect(square_pos[0],square_pos[1],20,20))
    pygame.draw.rect(screen,"green",pygame.Rect(player_pos.x,player_pos.y,20,20))
    if len(elements) !=0 :
        for i in elements:
            if i[0] == player_pos.x and i[1] == player_pos.y:
                print("COLLISION with ")
                print(i)
            pygame.draw.rect(screen,"green",pygame.Rect(i[0],i[1],20,20))
    screen.blit(font.render('Score:' + str(score), True, (255, 255, 255)), (20, 20))