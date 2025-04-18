import pygame
from pygame import *
from player import Player
from game_data import GData
from menu import *

# add background
# fix some logic
# refactor code
# add better sprites
# implement some easter eggs for dia
# add different soundtracks, and check when a soundtrack ends

gdata = GData()
player = Player(gdata)

main_menu_background = pygame.image.load("src/menu/main_menu/background.png")

main_menu = Menu(create_menu(gdata.main_menu_data,gdata))
gameover_menu = game_over_menu(create_menu(gdata.game_over_menu_data,gdata))
option_menu = options_menu(create_menu(gdata.options_menu_data,gdata))


pygame.mixer.music.load("src/OST/ost.mp3")
pygame.mixer.music.set_volume(0.1)

while gdata.running:
    pygame.display.flip()
    gdata.clock.tick(60)
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gdata.running = False
    
    gdata.screen.fill("black")
    if not main_menu.menu_showed:
        gdata.screen.blit(main_menu_background, (0, 0)) 
        if not player.dead and not gdata.options_showed:
            main_menu.print_menu(gdata,events)

        elif player.dead:
            pygame.mixer.music.pause()
            gdata.music_playing = False
            gameover_menu.print_menu(player, gdata, main_menu,events)

        elif gdata.options_showed:
            option_menu.print_menu(gdata, main_menu,events)

        
    else:
        if not gdata.music_playing:
            pygame.mixer.music.play(-1)
            gdata.music_playing = True
        gdata.clock.tick(gdata.difficulty)
        player.Eating(gdata)
        player.Movement(gdata,main_menu)
        player.rendering(gdata, main_menu)


pygame.quit()
