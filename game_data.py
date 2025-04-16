import pygame
import random
from pygame import *


class GData:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Snake")

        self.game_over_menu_data = [
            ("src/game_over/restart.png", "src/game_over/restart_selected.png"),
            ("src/game_over/quit.png", "src/game_over/quit_selected.png")
        ]

        self.main_menu_data = [
            ("src/menu/main_menu/start.png", "src/menu/main_menu/start_selected.png"),
            ("src/menu/main_menu/options.png", "src/menu/main_menu/options_selected.png"),
            ("src/menu/quit.png", "src/menu/quit_selected.png")
        ]

        self.options_menu_data = [
            ("src/menu/options/difficulty_easy.png", "src/menu/options/difficulty_easy_selected.png"),
            ("src/menu/options/no_walls.png", "src/menu/options/no_walls_selected.png"),
            ("src/menu/options/no_golden_apple.png", "src/menu/options/no_golden_apple_selected.png"),
            ("src/menu/quit.png", "src/menu/quit_selected.png")
        ]


        
        self.screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
        self.screen.fill((0, 0, 0))

        self.S_WIDTH = self.screen.get_width()
        self.S_HEIGHT = self.screen.get_height()
        
        self.BUTTONS_WIDTH = 196

        self.options_showed = False
        self.difficulty = 20
        self.solid_wall = False
        self.golden_apple = False
        self.music_playing = False

        
        self.clock = pygame.time.Clock()
        self.clock.tick(self.difficulty)
        self.running = True

        self.font = pygame.font.Font(None, 50)

        self.alg = 0
        self.menu_showed = False
    def reset(self):
        self.__init__()
