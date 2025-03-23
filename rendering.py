import pygame
import math
from pygame import *
import random


def rendering(screen,player_pos,square_pos,font,score,other_player_segments):
    pygame.draw.rect(screen,"red",pygame.Rect(square_pos[0],square_pos[1],20,20))
    pygame.draw.rect(screen,"green",pygame.Rect(player_pos.x,player_pos.y,20,20))
    if len(other_player_segments) !=0 :
        for i in other_player_segments:
            if i[0] == player_pos.x and i[1] == player_pos.y:
                player_pos.x = screen.get_width() / 2
                player_pos.y = screen.get_height() / 2
                other_player_segments.clear()
                score = 0
            pygame.draw.rect(screen,"green",pygame.Rect(i[0],i[1],20,20))
    screen.blit(font.render('Score:' + str(score), True, (255, 255, 255)), (20, 20))