import pygame
import math
from pygame import *
import random
<<<<<<< Updated upstream
<<<<<<< Updated upstream


#add teleportation when u hit the wall

#add a menu 



pygame.init()

screen = pygame.display.set_mode((1920,1080), FULLSCREEN)

pygame.display.set_caption("Snake")

screen.fill((0,0,0))

clock = pygame.time.Clock()

clock.tick(60)

running = True


player_pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
square_pos = Vector2(random.randrange(0,1920,20),random.randrange(0,1080,20))
other_player_segments = [] 
font = pygame.font.Font(None, 50)  # Use default font, size 50
score=0


last_pressed_keys = [0,0,0,0]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    score=mov_func.player_and_apple_movement(player_pos,square_pos,score,other_player_segments)    
    running = mov_func.current_direction(last_pressed_keys,player_pos,running,other_player_segments)
    rendering.rendering(screen,player_pos,square_pos,font,score,other_player_segments)
=======
from player import Player
from game_data import GData
from menu import *
#add teleportation when u hit the wall
#add classes
#refactor code
#add options
#fix WASTED text
#add sound
#add music
#add background
#fix menu issues and complete
        

=======
from player import Player
from game_data import GData
from menu import *
#add teleportation when u hit the wall
#add classes
#refactor code
#add options
#fix WASTED text
#add sound
#add music
#add background
#fix menu issues and complete
        

>>>>>>> Stashed changes
gdata = GData()
player = Player(gdata.screen)

game_over_menu = [
    pygame.image.load('imgsrc/game_over/restart.png'),
    pygame.image.load('imgsrc/game_over/quit.png')
]
slected_game_over = [
    pygame.image.load('imgsrc/game_over/restart_selected.png'),
    pygame.image.load('imgsrc/game_over/quit_selected.png')
]

options = [
    pygame.image.load('imgsrc/menu/start.png'),
    pygame.image.load('imgsrc/menu/options.png'),
    pygame.image.load('imgsrc/menu/quit.png')
]
slected_options = [
    pygame.image.load('imgsrc/menu/start_selected.png'),
    pygame.image.load('imgsrc/menu/options_selected.png'),
    pygame.image.load('imgsrc/menu/quit_selected.png')
]
main_menu = Menu(options,slected_options)
GO_menu = GO_Menu(game_over_menu,slected_game_over)

while gdata.running:
    gdata.clock.tick(10)
    pygame.display.flip()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gdata.running = False
    
    gdata.screen.fill("black")

    if main_menu.menu_showed == False and player.Dead == False:
        main_menu.menu_rendering(gdata)

    elif main_menu.menu_showed == False and player.Dead == True:
        GO_menu.menu_rendering(gdata,player,main_menu)
        
    else:
        player.Score = player.Eating() 
        gdata.running = player.Movement(gdata.running)
        rendering(gdata,player,main_menu,GO_menu)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes


    pygame.display.flip()
    clock.tick(10)
pygame.quit()