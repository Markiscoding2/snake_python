import pygame
from pygame import *
import random
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

    def handle_input(self):
        currrent_menu_key = pygame.key.get_pressed()

        if currrent_menu_key[pygame.K_w] and self.selected_index > 0:
            self.selected_index -= 1

        if (
            currrent_menu_key[pygame.K_s]
            and self.selected_index < len(self.options) - 1
        ):
            self.selected_index += 1
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

    def goprint_menu(self, player, gdata, main_menu):
        current_menu_key = self.handle_input()
        self.render_menu(gdata)

        if current_menu_key[pygame.K_RETURN]:
            player.dead = False  # Revive player

        if not player.dead:
            if self.selected_index == 0:
                player.__init__()  # Reset Player
                main_menu.menu_showed = False  # Return to main menu
            elif self.selected_index == 1:
                gdata.running = False



    def print_menu(self, gdata):
        CURRENT_MENU_KEY = self.handle_input()
        self.render_menu(gdata)

        if CURRENT_MENU_KEY[pygame.K_RETURN]:
            self.menu_showed = True
        
        if self.selected_index == 1 and self.menu_showed == True:
            print("options")
        if self.selected_index == 2 and self.menu_showed == True:
            gdata.running = False
