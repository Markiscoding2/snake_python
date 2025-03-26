import pygame
from pygame import *
from player import Player
from game_data import GData
from menu import *
#add teleportation when u hit the wall
#add classes
#add options
#fix WASTED text
#add sound
#add music
#add background
#fix menu issues and complete
        

gdata = GData()
player = Player()

game_over_menu = [
    pygame.image.load('imgsrc/game_over/restart.png'),
    pygame.image.load('imgsrc/game_over/quit.png')
]
selected_game_over = [
    pygame.image.load('imgsrc/game_over/restart_selected.png'),
    pygame.image.load('imgsrc/game_over/quit_selected.png')
]

options = [
    pygame.image.load('imgsrc/menu/start.png'),
    pygame.image.load('imgsrc/menu/options.png'),
    pygame.image.load('imgsrc/menu/quit.png')
]
selected_options = [
    pygame.image.load('imgsrc/menu/start_selected.png'),
    pygame.image.load('imgsrc/menu/options_selected.png'),
    pygame.image.load('imgsrc/menu/quit_selected.png')
]
main_menu = MENU(options, selected_options)
GO_menu = MENU(game_over_menu, selected_game_over)

while gdata.running:
    gdata.clock.tick(10)
    pygame.display.flip()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gdata.running = False
    
    gdata.screen.fill("black")

    if main_menu.menu_showed == False and player.Dead == False:
        main_menu.print_menu(gdata)

    elif main_menu.menu_showed == False and player.Dead == True:
        GO_menu.goprint_menu(player,gdata,main_menu)
        
    else:
        gdata.screen.blit(pygame.image.load('imgsrc\grid\grid.png'), (0,0))
        player.Eating() 
        player.Movement(gdata)
        player.rendering(gdata,main_menu)
    pygame.display.flip()

pygame.quit()