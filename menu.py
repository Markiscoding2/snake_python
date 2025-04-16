import pygame
from pygame import *
from game_data import GData
from player import Player


def get_sprite(spritesheet,width,height):
    image = pygame.Surface((width,height)).convert_alpha()
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
    def draw(self,gdata,events):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if self.rect.collidepoint(mouse_pos.x,mouse_pos.y):

            gdata.screen.blit(
            self.selected_image,
                (
                    self.button_pos.x,
                    self.button_pos.y 
                ),
            )

            for event in events:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    return True
                
            return False
        gdata.screen.blit(
            self.image,
            (
                self.button_pos.x,
                self.button_pos.y 
            ),
        )
        return False

def load_button(image_path,image_path_selected,x,y):
    return Button(
        pygame.image.load(image_path),
        pygame.image.load(image_path_selected),
        x,
        y
    )

def create_menu(button_image_pairs, gdata):
    button_arr = []
    center_x = gdata.S_WIDTH / 2 - 196/2
    start_y = gdata.S_HEIGHT / 2

    for i, (img, selected_img) in enumerate(button_image_pairs):
        y = start_y + i * 70
        button_arr.append(load_button(img, selected_img, center_x, y))

    return button_arr
class Menu:
    def __init__(self, all_buttons):

        self.buttons = all_buttons
        self.NUMBER_OF_OPTIONS = len(self.buttons)
        self.selected_index = 0
        self.menu_showed = False

    def render_menu(self, gdata,events):
        for i in range(self.NUMBER_OF_OPTIONS):
            image = self.buttons[i]
            if image.draw(gdata,events):
                return i
        return -1
    
    def change_buttons(self, gdata, choice):
        difficulty_map = {
            20 : "difficulty_easy",
            25 : "difficulty_medium",
            30 : "difficulty_hard"
        }
        difficulty_image = f"src/menu/options/{difficulty_map[gdata.difficulty]}.png"
        difficulty_image_selected = f"src/menu/options/{difficulty_map[gdata.difficulty]}_selected.png"
        
        solid_wall_map = {
            True : "solid_walls",
            False : "no_walls"
        }
        
        solid_wall_image = f"src/menu/options/{solid_wall_map[gdata.solid_wall]}.png"
        solid_wall_image_selected = f"src/menu/options/{solid_wall_map[gdata.solid_wall]}_selected.png"

        golden_apple_map = {
            True : "golden_apple",
            False : "no_golden_apple"
        }
        golden_apple_image = f"src/menu/options/{golden_apple_map[gdata.golden_apple]}.png"
        golden_apple_image_selected = f"src/menu/options/{golden_apple_map[gdata.golden_apple]}_selected.png"

        if choice == 0:
            self.buttons[0].image = pygame.image.load(difficulty_image)
            self.buttons[0].selected_image = pygame.image.load(difficulty_image_selected)
        elif choice == 1:
            self.buttons[1].image = pygame.image.load(solid_wall_image)
            self.buttons[1].selected_image = pygame.image.load(solid_wall_image_selected)
        elif choice == 2:
            self.buttons[2].image = pygame.image.load(golden_apple_image)
            self.buttons[2].selected_image = pygame.image.load(golden_apple_image_selected)
    
    def options_menu(self,gdata,main_menu,events):
        self.selected_index = self.render_menu(gdata,events)

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

    def goprint_menu(self, player, gdata, main_menu,events):
        self.selected_index = self.render_menu(gdata,events)

        if self.selected_index != -1:
            player.dead = False  

        if not player.dead:
            if self.selected_index == 0:
                player.__init__() 
                main_menu.menu_showed = False  
                gdata.music_playing = False
            elif self.selected_index == 1:
                gdata.running = False



    def print_menu(self, gdata, events):
        self.selected_index = self.render_menu(gdata,events)

        if self.selected_index != -1:
            self.menu_showed = True


        if self.selected_index == 1 and self.menu_showed == True:
            gdata.options_showed = True
            self.menu_showed = False
        if self.selected_index == 2 and self.menu_showed == True:
            gdata.running = False
