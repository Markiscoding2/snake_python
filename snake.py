import pygame
from pygame import *
from player import Player
from game_data import GData
from menu import *

# add teleportation when u hit the wall
# add classes
# add options
# fix WASTED text
# add sound
# add music
# add background
# fix menu issues and complete


gdata = GData()
player = Player()

game_over_menu = [
    pygame.image.load("src/game_over/restart.png"),
    pygame.image.load("src/game_over/quit.png"),
]
selected_game_over = [
    pygame.image.load("src/game_over/restart_selected.png"),
    pygame.image.load("src/game_over/quit_selected.png"),
]

options = [
    pygame.image.load("src/menu/start.png"),
    pygame.image.load("src/menu/options.png"),
    pygame.image.load("src/menu/quit.png"),
]
selected_options = [
    pygame.image.load("src/menu/start_selected.png"),
    pygame.image.load("src/menu/options_selected.png"),
    pygame.image.load("src/menu/quit_selected.png"),
]
main_menu = Menu(options, selected_options)
GO_menu = Menu(game_over_menu, selected_game_over)

game_ost = pygame.mixer.Sound("src\OST\ost.mp3")

test = True

while gdata.running:

    gdata.clock.tick(10)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gdata.running = False
    gdata.screen.fill("black")

    if main_menu.menu_showed == False and player.dead == False:
        main_menu.print_menu(gdata)

    elif main_menu.menu_showed == False and player.dead == True:
        game_ost.stop()
        GO_menu.goprint_menu(player, gdata, main_menu)
        if test == False:
            game_ost.stop()
            test = True

    else:
        if test:
            game_ost.play()
            game_ost.set_volume(0.1)
            test = False
        # gdata.screen.blit(pygame.image.load('src\grid\grid.png'), (0,0))
        player.Eating()
        player.Movement(gdata)
        player.rendering(gdata, main_menu)
    pygame.display.flip()

pygame.quit()
