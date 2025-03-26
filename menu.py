import pygame
from pygame import *
import random
from game_data import GData
from player import Player
class MENU:
    def __init__(self, options, selected_options):
        self.options = options
        self.selected_options = selected_options

        self.NUMBER_OF_OPTIONS = len(self.options)
        self.NUMBER_OF_SELECTED_OPTIONS = len(self.selected_options)

        self.selected_index = 0
        self.menu_showed = False
    def handle_input(self):
        currrent_menu_key = pygame.key.get_pressed()

        if currrent_menu_key[pygame.K_w] and self.selected_index > 0:
            self.selected_index-=1
        
        if currrent_menu_key[pygame.K_s] and self.selected_index < len(self.options)-1:
            self.selected_index+=1
        return currrent_menu_key 
    
    def render_menu(self,gdata):
        for i in range(self.NUMBER_OF_OPTIONS):
            selected_image = self.selected_options[i]
            images = self.options[i]
            if i == self.selected_index:
                gdata.screen.blit(selected_image, (gdata.S_WIDTH / 2 - gdata.BUTTONS_WIDTH / 2 , gdata.S_HEIGHT / 2 + 70 * i ))
            else:
                gdata.screen.blit(images, (gdata.S_WIDTH / 2 - gdata.BUTTONS_WIDTH / 2 , gdata.S_HEIGHT / 2 + 70 * i ))
    
    def goprint_menu(self, player, gdata, main_menu):
        """Handles Game Over menu logic."""
        current_menu_key = self.handle_input()
        self.render_menu(gdata)

        if current_menu_key[pygame.K_RETURN]:
            player.Dead = False  # Revive player

        if not player.Dead:
            if self.selected_index == 0:
                main_menu.menu_showed = False  # Return to main menu
            elif self.selected_index == 1:
                gdata.running = False 
            
    def print_menu(self,gdata):
        CURRENT_MENU_KEY = self.handle_input()
        self.render_menu(gdata)

        if CURRENT_MENU_KEY[pygame.K_RETURN]:
            self.menu_showed=True
        
        if self.selected_index == 1 and self.menu_showed == True:
            print("options")
        if self.selected_index== 2 and self.menu_showed == True:
            gdata.running = False
    

    

def rendering(gdata,player,main_menu):
    PLAYER_X = player.Position.x
    PLAYER_Y = player.Position.y

    APPLE_X = player.Apple_Position.x
    APPLE_Y = player.Apple_Position.y

    GRID_SIZE = player.GRID_SIZE

    PLAYER_COLOR = "green"
    APPLE_COLOR = "red"
    
    SCORE_AS_STRING = str(player.Score)

    NUMBER_SEGMENTS=len(player.Segments)

    pygame.draw.rect(gdata.screen, APPLE_COLOR ,pygame.Rect(APPLE_X,APPLE_Y,GRID_SIZE,GRID_SIZE))
    pygame.draw.rect(gdata.screen, PLAYER_COLOR ,pygame.Rect(PLAYER_X,PLAYER_Y,GRID_SIZE,GRID_SIZE))
    if NUMBER_SEGMENTS !=0 :
        for i in player.Segments:
            SEGMENT_X = i[0]
            SEGMENT_Y = i[1]
            if SEGMENT_X == PLAYER_X and SEGMENT_Y == PLAYER_Y:
                player.Position.x = 800
                player.Position.y = 640
                player.Segments.clear()
                player.Score = 0
                player.Dead = True
                main_menu.menu_showed = False
            pygame.draw.rect(gdata.screen,PLAYER_COLOR,pygame.Rect(SEGMENT_X,SEGMENT_Y,GRID_SIZE,GRID_SIZE))
    gdata.screen.blit(gdata.font.render('Score:' + SCORE_AS_STRING , True, (255, 255, 255)), (GRID_SIZE, GRID_SIZE))