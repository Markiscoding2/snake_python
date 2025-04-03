import pygame
from pygame import *
from player import Player
from game_data import GData
from menu import *

# add teleportation when u hit the wall
# add options
# fix WASTED text
# add sound
# add music
# add background


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

main_menu_images = [
    pygame.image.load("src/menu/start.png"),
    pygame.image.load("src/menu/options.png"),
    pygame.image.load("src/menu/quit.png"),
]
selected_options = [
    pygame.image.load("src/menu/start_selected.png"),
    pygame.image.load("src/menu/options_selected.png"),
    pygame.image.load("src/menu/quit_selected.png"),
]

options_menu = [
    pygame.image.load("src/menu/difficulty.png"),
    pygame.image.load("src/menu/solid_walls.png"),
    pygame.image.load("src/menu/golden_apple.png"),
    pygame.image.load("src/menu/quit.png")
]
selected_options_menu = [
    pygame.image.load("src/menu/difficulty_selected.png"),
    pygame.image.load("src/menu/solid_walls_selected.png"),
    pygame.image.load("src/menu/golden_apple_selected.png"),
    pygame.image.load("src/menu/quit_selected.png")
]

main_menu = Menu(main_menu_images, selected_options)
go_menu = Menu(game_over_menu, selected_game_over)
options_menu = Menu(options_menu,selected_options_menu)
game_ost = pygame.mixer.Sound("src\OST\ost.mp3")

test = True

while gdata.running:
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gdata.running = False
    gdata.screen.fill("black")

    if main_menu.menu_showed == False and player.dead == False and gdata.options_showed==False:
        gdata.clock.tick(0)
        main_menu.print_menu(gdata)

    elif main_menu.menu_showed == False and player.dead == True:
        gdata.clock.tick(0)
        game_ost.stop()
        go_menu.goprint_menu(player, gdata, main_menu)
        if test == False:
            game_ost.stop()
            test = True
    elif main_menu.menu_showed == False and gdata.options_showed == True:
        gdata.clock.tick(0)
        options_menu.options_menu(gdata,main_menu)
    else:
        gdata.clock.tick(gdata.difficulty)
        if test:
            game_ost.play()
            game_ost.set_volume(0.1)
            test = False
        #gdata.screen.blit(pygame.image.load('src\grid\grid.png'), (0,0))
        player.Eating()
        player.Movement(gdata)
        player.rendering(gdata, main_menu)
    pygame.display.flip()

pygame.quit()
