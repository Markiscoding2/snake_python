import pygame
from pygame import *
from game_data import GData
from player import Player


class Menu:
    def __init__(self, options, selected_options):
        self.options = options
        self.selected_options = selected_options

        self.NUMBER_OF_OPTIONS = len(self.options)
        self.NUMBER_OF_SELECTED_OPTIONS = len(self.selected_options)

        self.selected_index = 0
        self.menu_showed = False
        
        self.last_key_press = 0 
        self.key_delay = 200  
    def handle_input(self):
        current_time = pygame.time.get_ticks()
        currrent_menu_key = pygame.key.get_pressed()
        
        if current_time - self.last_key_press > self.key_delay:

            if currrent_menu_key[pygame.K_w] and self.selected_index > 0:
                self.selected_index -= 1
                self.last_key_press = current_time  # Update key press time

            if currrent_menu_key[pygame.K_s] and self.selected_index < len(self.options) - 1:
                self.selected_index += 1
                self.last_key_press = current_time  # Update key press time
            
            if currrent_menu_key[pygame.K_RETURN]:
                self.last_key_press = current_time  # Update key press time
        
        return currrent_menu_key
    def render_menu(self, gdata):
        for i in range(self.NUMBER_OF_OPTIONS):
            selected_image = self.selected_options[i]
            images = self.options[i]
            if i == self.selected_index:
                gdata.screen.blit(
                    selected_image,
                    (
                        gdata.S_WIDTH / 2 - gdata.BUTTONS_WIDTH / 2,
                        gdata.S_HEIGHT / 2 + 70 * i,
                    ),
                )
            else:
                gdata.screen.blit(
                    images,
                    (
                        gdata.S_WIDTH / 2 - gdata.BUTTONS_WIDTH / 2,
                        gdata.S_HEIGHT / 2 + 70 * i,
                    ),
                )
        
    def options_menu(self,gdata,main_menu):
        #idea: create 3 seperate difficulty images: easy,medium,hard, implement logic by adding some booleans checking which difficulty is chosen based on the current framerate
        #for the golden apple just check the current state and if true show under it
        #for the wall do the same
        current_menu_key = self.handle_input()
        self.render_menu(gdata)
        gdata.clock.tick(20)
        if current_menu_key[pygame.K_RETURN]:
            if self.selected_index == 0:
                gdata.difficulty += 5
                if gdata.difficulty > 30:
                    gdata.difficulty = 20
            elif self.selected_index == 1:
                gdata.solid_wall = not gdata.solid_wall
            elif self.selected_index == 2:
                gdata.golden_apple = not gdata.golden_apple
            elif self.selected_index == 3:
                gdata.options_showed = False
                main_menu.menu_showed = False
                self.selected_index = 2
            pygame.time.wait(200)




    def goprint_menu(self, player, gdata, main_menu):
        current_menu_key = self.handle_input()
        self.render_menu(gdata)
        if current_menu_key[pygame.K_RETURN]:
            player.dead = False  # Revive player
            pygame.time.wait(200)

        if not player.dead:
            if self.selected_index == 0:
                player.__init__()  # Reset Player
                main_menu.menu_showed = False  # Return to main menu
                gdata.music_playing = False
            elif self.selected_index == 1:
                gdata.running = False



    def print_menu(self, gdata):
        CURRENT_MENU_KEY = self.handle_input()
        self.render_menu(gdata)
        if CURRENT_MENU_KEY[pygame.K_RETURN]:
            self.menu_showed = True
            pygame.time.wait(200)


        if self.selected_index == 1 and self.menu_showed == True:
            gdata.options_showed = True
            self.menu_showed = False
        if self.selected_index == 2 and self.menu_showed == True:
            gdata.running = False
