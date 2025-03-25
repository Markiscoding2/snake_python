import pygame
from pygame import *
import random
from game_data import GData
from player import Player
class Menu:
    def __init__(self, options, selected_options):
        self.options = options
        self.selected_options = selected_options
        self.selected_index = 0
        self.menu_showed = False
    
    def menu_rendering(self,gdata):
        currrent_menu_key = pygame.key.get_pressed()

        if currrent_menu_key[pygame.K_w] and self.selected_index > 0:
            self.selected_index-=1
        if currrent_menu_key[pygame.K_s] and self.selected_index < len(self.options)-1:
            self.selected_index+=1
        for i in range(len(self.options)):
            if i == self.selected_index:
                gdata.screen.blit(self.selected_options[i], (gdata.screen.get_width() / 2 - 196/2 , gdata.screen.get_height()/2 + 70 * i ))
            else:
                gdata.screen.blit(self.options[i], (gdata.screen.get_width() / 2 - 196/2 , gdata.screen.get_height()/2 + 70 * i ))
        if currrent_menu_key[pygame.K_RETURN]:
            self.menu_showed=True
        
        if self.selected_index == 1 and self.menu_showed == True:
            print("options")
        if self.selected_index== 2 and self.menu_showed == True:
            gdata.running = False
class GO_Menu:
    def __init__(self, options, selected_options):
        self.options = options
        self.selected_options = selected_options
        self.selected_index = 0
    
    def menu_rendering(self,gdata,player,main_menu):
        currrent_menu_key = pygame.key.get_pressed()
        if currrent_menu_key[pygame.K_w] and self.selected_index > 0:
            self.selected_index-=1
        if currrent_menu_key[pygame.K_s] and self.selected_index < len(self.options)-1:
            self.selected_index+=1
        for i in range(len(self.options)):
            if i == self.selected_index:
                gdata.screen.blit(self.selected_options[i], (gdata.screen.get_width() / 2 - 196/2 , gdata.screen.get_height()/2 + 70 * i ))
            else:
                gdata.screen.blit(self.options[i], (gdata.screen.get_width() / 2 - 196/2 , gdata.screen.get_height()/2 + 70 * i ))
        if currrent_menu_key[pygame.K_RETURN]:
            player.Dead = False
        
        if self.selected_index == 0 and player.Dead == False:
            main_menu.menu_showed = False
        if self.selected_index == 1 and player.Dead == False:
            gdata.running = False


def rendering(gdata,player,main_menu,GO_menu):
    pygame.draw.rect(gdata.screen,"red",pygame.Rect(player.Apple_Position[0],player.Apple_Position[1],40,40))
    pygame.draw.rect(gdata.screen,"green",pygame.Rect(player.Position.x,player.Position.y,40,40))
    if len(player.Segments) !=0 :
        for i in player.Segments:
            if i[0] == player.Position.x and i[1] == player.Position.y:
                player.Position.x = 800
                player.Position.y = 640
                player.Segments.clear()
                player.Score = 0
                player.Dead = True
                main_menu.menu_showed = False
            pygame.draw.rect(gdata.screen,"green",pygame.Rect(i[0],i[1],40,40))
    gdata.screen.blit(gdata.font.render('Score:' + str(player.Score), True, (255, 255, 255)), (20, 20))