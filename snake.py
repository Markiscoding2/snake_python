import pygame
from pygame import *
from player import Player
from game_data import GData
from menu import *

# add background
# fix menu
# fix some logic
# refactor code
# add better sprites
# implement some easter eggs for dia
# add different soundtracks, and check when a soundtrack ends

gdata = GData()
player = Player()

game_over_menu_images = [
    pygame.image.load("src/game_over/restart.png"),
    pygame.image.load("src/game_over/quit.png"),
]

game_over_menu_selected_images = [
    pygame.image.load("src/game_over/restart_selected.png"),
    pygame.image.load("src/game_over/quit_selected.png"),
]

main_menu_images = [
    pygame.image.load("src/menu/main_menu/start.png"),
    pygame.image.load("src/menu/main_menu/options.png"),
    pygame.image.load("src/menu/quit.png"),
]
main_menu_selected_images = [
    pygame.image.load("src/menu/main_menu/start_selected.png"),
    pygame.image.load("src/menu/main_menu/options_selected.png"),
    pygame.image.load("src/menu/quit_selected.png"),
]

options_menu_images = [
    pygame.image.load("src/menu/options/difficulty_easy.png"),
    pygame.image.load("src/menu/options/no_walls.png"),
    pygame.image.load("src/menu/options/golden_apple.png"),
    pygame.image.load("src/menu/quit.png")
]
options_menu_selected_images = [
    pygame.image.load("src/menu/options/difficulty_easy_selected.png"),
    pygame.image.load("src/menu/options/no_walls_selected.png"),
    pygame.image.load("src/menu/options/golden_apple_selected.png"),
    pygame.image.load("src/menu/quit_selected.png")
]

main_menu = Menu(main_menu_images, main_menu_selected_images)
go_menu = Menu(game_over_menu_images, game_over_menu_selected_images)
options_menu_images = Menu(options_menu_images,options_menu_selected_images)
background_music = pygame.mixer.Sound("src\OST\ost.mp3")

while gdata.running:
    pygame.display.flip()
    gdata.clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gdata.running = False
    
    gdata.screen.fill("black")    
    if not main_menu.menu_showed:
        if not player.dead and not gdata.options_showed:
            main_menu.print_menu(gdata)
        elif player.dead:
            background_music.stop()
            go_menu.goprint_menu(player, gdata, main_menu)
        elif gdata.options_showed:
            options_menu_images.options_menu(gdata, main_menu)
    else:
        gdata.clock.tick(gdata.difficulty)
        if not gdata.music_playing:
            background_music.play()
            background_music.set_volume(0.1)
            gdata.music_playing = True
        player.Eating()
        player.Movement(gdata,main_menu)
        player.rendering(gdata, main_menu)


pygame.quit()
