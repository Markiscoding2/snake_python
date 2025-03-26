import pygame
import random
from pygame import *


class Player:
    def __init__(self):
        self.GRID_SIZE = 40

        self.START_WIDTH = 800
        self.START_HEIGHT = 640
        
        self.X_BOUNDS = [1880 , 0]
        self.Y_BOUNDS = [1040 , 0]
 

        self.APPLE_WIDTH = 1920
        self.APPLE_HEIGHT = 1080

        self.Position = Vector2(self.START_WIDTH, self.START_HEIGHT)
        self.Current_Direction = [0,0,0,0]

        self.Segments = [] 
        self.Score = 0
        
        self.Dead = False
        self.Apple_Position = Vector2(
            random.randrange(self.GRID_SIZE,self.APPLE_WIDTH,self.GRID_SIZE),
            random.randrange(self.GRID_SIZE,self.APPLE_HEIGHT ,self.GRID_SIZE)
        )
        

    def add_segment(self):
        self.Segments.append([self.Position.x,self.Position.y])
    
    def Movement(self,gdata):

        current_pressed_key = pygame.key.get_pressed()

        LEFT=self.Current_Direction[1]
        RIGHT=self.Current_Direction[0]
        UP = self.Current_Direction[2]
        DOWN = self.Current_Direction[3]
        
        NUMBER_SEGMENTS=len(self.Segments)

        if current_pressed_key[pygame.K_ESCAPE]:
            gdata.running = False
        if current_pressed_key[pygame.K_a] and RIGHT == False or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_a]:
            self.Current_Direction[0] = True
            self.Current_Direction[1] = False
            self.Current_Direction[2] = False
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_d] and LEFT == False or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_d]:
            self.Current_Direction[0] = False
            self.Current_Direction[1] = True
            self.Current_Direction[2] = False
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_w] and DOWN == False or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_w]:     
            self.Current_Direction[0] = False
            self.Current_Direction[1] = False
            self.Current_Direction[2] = True
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_s] and UP == False or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_s]: 
            self.Current_Direction[0] = False
            self.Current_Direction[1] = False
            self.Current_Direction[2] = False
            self.Current_Direction[3] = True

        self_pos_changed = False
        old_plr_x=self.Position.x
        old_plr_y=self.Position.y
        
        if(RIGHT and self.Position.x > self.X_BOUNDS[1] ):
            self.Position.x -= self.GRID_SIZE
            self_pos_changed = True
        if(LEFT and self.Position.x < self.X_BOUNDS[0]):  
            self.Position.x += self.GRID_SIZE
            self_pos_changed = True
        if(UP and self.Position.y > self.Y_BOUNDS[1]):
            self.Position.y -= self.GRID_SIZE
            self_pos_changed = True
        if(DOWN and self.Position.y < self.Y_BOUNDS[0]):
            self.Position.y += self.GRID_SIZE
            self_pos_changed = True
        
        if self_pos_changed :
            if NUMBER_SEGMENTS != 0:
                for i in range(NUMBER_SEGMENTS - 1, 0, -1):
                    self.Segments[i] = self.Segments[i-1]
                self.Segments[0]=[old_plr_x,old_plr_y]

    

    def Eating(self):
        PLAYER_X = self.Position.x
        PLAYER_Y = self.Position.y
        APPLE_X = self.Apple_Position.x
        APPLE_Y = self.Apple_Position.y
        if PLAYER_X == APPLE_X and PLAYER_Y == APPLE_Y: 
            self.Apple_Position.x = random.randrange(self.GRID_SIZE,self.APPLE_WIDTH,self.GRID_SIZE)
            self.Apple_Position.y = random.randrange(self.GRID_SIZE,self.APPLE_HEIGHT,self.GRID_SIZE)
            self.Score+=1
            self.add_segment()

        