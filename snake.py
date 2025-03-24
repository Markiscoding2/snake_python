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
        player.Eating() 
        player.Movement(gdata.running)
        rendering(gdata,player,main_menu,GO_menu)
    pygame.display.flip()
    gdata.clock.tick(20)

pygame.quit()