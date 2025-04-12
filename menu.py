import pygame
from pygame import *
from game_data import GData
from player import Player


def get_sprite(spritesheet,width,height):
    image = pygame.Surface((width,height)).convert_alpha
    image.blit(spritesheet,(0,0),(0,0),width,height)
    return image

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
        current_menu_key = pygame.key.get_pressed()
        
        if current_time - self.last_key_press > self.key_delay:
            
            if current_menu_key[pygame.K_w] and self.selected_index > 0:
                self.selected_index -= 1
                self.last_key_press = current_time  
                pygame.time.wait(100)
            if current_menu_key[pygame.K_s] and self.selected_index < len(self.options) - 1:
                self.selected_index += 1
                self.last_key_press = current_time  
                pygame.time.wait(100)
            if current_menu_key[pygame.K_RETURN]:
                self.last_key_press = current_time  
                pygame.time.wait(100)
        return current_menu_key
    
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
    
    def change_buttons(self, gdata, choice):
        if choice == 0:
            if gdata.difficulty == 20:
                self.options[0] = pygame.image.load("src/menu/options/difficulty_easy.png")
                self.selected_options[0] = pygame.image.load("src/menu/options/difficulty_easy_selected.png")
            elif gdata.difficulty == 25:
                self.options[0] = pygame.image.load("src/menu/options/difficulty_medium.png")
                self.selected_options[0] = pygame.image.load("src/menu/options/difficulty_medium_selected.png")
            elif gdata.difficulty == 30:
                self.options[0] = pygame.image.load("src/menu/options/difficulty_hard.png")
                self.selected_options[0] = pygame.image.load("src/menu/options/difficulty_hard_selected.png")
        elif choice == 1:
            if gdata.solid_wall:
                self.options[1] = pygame.image.load("src/menu/options/solid_walls.png")
                self.selected_options[1] = pygame.image.load("src/menu/options/solid_walls_selected.png")
            else:
                self.options[1] = pygame.image.load("src/menu/options/no_walls.png")
                self.selected_options[1] = pygame.image.load("src/menu/options/no_walls_selected.png")
        elif choice == 2:
            if gdata.golden_apple:
                self.options[2] = pygame.image.load("src/menu/options/golden_apple.png")
                self.selected_options[2] = pygame.image.load("src/menu/options/golden_apple_selected.png")
            else:
                self.options[2] = pygame.image.load("src/menu/options/no_golden_apple.png")
                self.selected_options[2] = pygame.image.load("src/menu/options/no_golden_apple_selected.png")
    
    def options_menu(self,gdata,main_menu):
        current_menu_key = self.handle_input()
        self.render_menu(gdata)
        if current_menu_key[pygame.K_RETURN]:
            pygame.time.wait(200)
            if self.selected_index == 0:
                gdata.difficulty += 5
                if gdata.difficulty > 30:
                    gdata.difficulty = 20
                self.change_buttons(gdata, 0)
            elif self.selected_index == 1:
                gdata.solid_wall = not gdata.solid_wall
                self.change_buttons(gdata, 1)
            elif self.selected_index == 2:
                gdata.golden_apple = not gdata.golden_apple
                self.change_buttons(gdata, 2)
            elif self.selected_index == 3:
                gdata.options_showed = False
                main_menu.menu_showed = False
                self.selected_index = 2





    def goprint_menu(self, player, gdata, main_menu):
        current_menu_key = self.handle_input()
        self.render_menu(gdata)
        if current_menu_key[pygame.K_RETURN]:
            player.dead = False  
            pygame.time.wait(100)

        if not player.dead:
            if self.selected_index == 0:
                player.__init__() 
                main_menu.menu_showed = False  
                gdata.music_playing = False
            elif self.selected_index == 1:
                gdata.running = False



    def print_menu(self, gdata):
        CURRENT_MENU_KEY = self.handle_input()
        self.render_menu(gdata)
        if CURRENT_MENU_KEY[pygame.K_RETURN]:
            self.menu_showed = True
            pygame.time.wait(100)


        if self.selected_index == 1 and self.menu_showed == True:
            gdata.options_showed = True
            self.menu_showed = False
        if self.selected_index == 2 and self.menu_showed == True:
            gdata.running = False
