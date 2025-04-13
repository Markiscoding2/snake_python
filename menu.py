import pygame
from pygame import *
from game_data import GData
from player import Player


def get_sprite(spritesheet,width,height):
    image = pygame.Surface((width,height)).convert_alpha
    image.blit(spritesheet,(0,0),(0,0),width,height)
    return image

class Button:
    def __init__(self,sprite,selected_sprite,x,y):

        self.button_pos = Vector2(x,y)

        self.width = sprite.get_width()
        self.height = sprite.get_height()

        self.image = pygame.transform.scale(sprite,(self.width,self.height))    
        self.selected_image = pygame.transform.scale(selected_sprite,(self.width,self.height))    
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self,gdata,offset,scale):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if self.rect.collidepoint(mouse_pos.x-offset.x,mouse_pos.y-offset.y*scale):
            gdata.screen.blit(
            self.selected_image,
                (
                    self.button_pos.x + offset.x,
                    self.button_pos.y + offset.y*scale
                ),
            )
            return
        gdata.screen.blit(
            self.image,
            (
                self.button_pos.x + offset.x,
                self.button_pos.y + offset.y*scale
            ),
        )


class Menu:
    def __init__(self, option):
        self.options = option

        self.NUMBER_OF_OPTIONS = len(self.options)

        self.selected_index = 0
        self.menu_showed = False
        
        self.last_key_press = 0 
        self.key_delay = 200  
    def handle_input(self):
        current_menu_key = pygame.key.get_pressed()
                    
        if current_menu_key[pygame.K_w] and self.selected_index > 0:
            self.selected_index -= 1
            pygame.time.wait(100)
        if current_menu_key[pygame.K_s] and self.selected_index < len(self.options) - 1:
            self.selected_index += 1
            pygame.time.wait(100)
        if current_menu_key[pygame.K_RETURN]:
            pygame.time.wait(100)
        return current_menu_key
    
    def render_menu(self, gdata):
        offset = Vector2(-196/2,70)
        for i in range(self.NUMBER_OF_OPTIONS):
            image = self.options[i]
            image.draw(gdata,offset,i)

    def change_buttons(self, gdata, choice):
        if choice == 0:
            if gdata.difficulty == 20:
                self.options[0].image = pygame.image.load("src/menu/options/difficulty_easy.png")
                self.options[0].selected_image = pygame.image.load("src/menu/options/difficulty_easy_selected.png")
            elif gdata.difficulty == 25:
                self.options[0].image = pygame.image.load("src/menu/options/difficulty_medium.png")
                self.options[0].selected_image = pygame.image.load("src/menu/options/difficulty_medium_selected.png")
            elif gdata.difficulty == 30:
                self.options[0].image = pygame.image.load("src/menu/options/difficulty_hard.png")
                self.options[0].selected_image = pygame.image.load("src/menu/options/difficulty_hard_selected.png")
        elif choice == 1:
            if gdata.solid_wall:
                self.options[1].image = pygame.image.load("src/menu/options/solid_walls.png")
                self.options[1].selected_image = pygame.image.load("src/menu/options/solid_walls_selected.png")
            else:
                self.options[1].image = pygame.image.load("src/menu/options/no_walls.png")
                self.options[1].selected_image = pygame.image.load("src/menu/options/no_walls_selected.png")
        elif choice == 2:
            if gdata.golden_apple:
                self.options[2].image = pygame.image.load("src/menu/options/golden_apple.png")
                self.options[2].selected_image = pygame.image.load("src/menu/options/golden_apple_selected.png")
            else:
                self.options[2].image = pygame.image.load("src/menu/options/no_golden_apple.png")
                self.options[2].selected_image = pygame.image.load("src/menu/options/no_golden_apple_selected.png")
    
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
