import pygame
from pygame import *
from player_class import Player
from game_data import GData
from menu import *

# add background
# fix some logic
# refactor code
# add better sprites
# implement some easter eggs for dia
# add different soundtracks, and check when a soundtrack ends

gdata = GData()
player = Player()

main_menu_background = pygame.image.load("src/menu/main_menu/background.png")

main_menu = Menu(create_menu(gdata.main_menu_data,gdata))
game_over_menu = game_over_menu(create_menu(gdata.game_over_menu_data,gdata))
options_menu = options_menu(create_menu(gdata.options_menu_data,gdata))
exit_button = load_button("src\sprites\exit_button.png","src\sprites\exit_button_selected.png",1920-50,0)
background_music = pygame.mixer.Sound("src\OST\ost.mp3")

read_high_score = open("high_score.txt","r")
player.high_score = read_high_score.read()
read_high_score.close

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
            background_music.stop()
            game_over_menu.print_menu(player, gdata, main_menu,events)
        elif gdata.options_showed:
            options_menu.print_menu(gdata, main_menu,events)
    else:
        gdata.clock.tick(gdata.difficulty)
        if not gdata.music_playing:
            background_music.play()
            background_music.set_volume(0.1)
            gdata.music_playing = True
        player.Eating(gdata)
        player.Movement(gdata,main_menu)
        player.rendering(gdata, main_menu,exit_button,events)

if player.score > int(player.high_score):
    write_high_score = open("high_score.txt","w")
    write_high_score.write(f"{player.score}")
    write_high_score.close
pygame.quit()
