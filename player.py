import pygame
import random
from collections import deque    
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
        self.direction = Vector2(0,0)

        self.Segments = deque() 
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
        NUMBER_SEGMENTS=len(self.Segments)

        if current_pressed_key[pygame.K_ESCAPE]:
            gdata.running = False
        if current_pressed_key[pygame.K_a] and self.direction.x == 0 or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_a]:
            self.direction = Vector2(-1,0)
        if current_pressed_key[pygame.K_d] and self.direction.x == 0 or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_d]:
            self.direction = Vector2(1,0)
        if current_pressed_key[pygame.K_w] and self.direction.y == 0 or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_w]:     
            self.direction = Vector2(0,-1)
        if current_pressed_key[pygame.K_s] and self.direction.y == 0 or NUMBER_SEGMENTS == 0 and current_pressed_key[pygame.K_s]: 
            self.direction = Vector2(0,1)
        
        if self.direction == Vector2(0,0):
            return
        
        new_position = self.Position + self.direction * self.GRID_SIZE

        if self.X_BOUNDS[1] < new_position.x < self.X_BOUNDS[0] and self.Y_BOUNDS[1] < new_position.y < self.Y_BOUNDS[0]:
            old_position = self.Position
            self.Position = new_position

            if self.Segments:
                self.Segments.appendleft(old_position)
                self.Segments.pop()


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

    def rendering(self,gdata,main_menu):
        PLAYER_X = self.Position.x
        PLAYER_Y = self.Position.y

        APPLE_X = self.Apple_Position.x
        APPLE_Y = self.Apple_Position.y

        GRID_SIZE = self.GRID_SIZE

        PLAYER_COLOR = "green"
        APPLE_COLOR = "red"
        
        SCORE_AS_STRING = str(self.Score)

        NUMBER_SEGMENTS=len(self.Segments)

        pygame.draw.rect(gdata.screen, APPLE_COLOR ,pygame.Rect(APPLE_X,APPLE_Y,GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(gdata.screen, PLAYER_COLOR ,pygame.Rect(PLAYER_X,PLAYER_Y,GRID_SIZE,GRID_SIZE))
        if NUMBER_SEGMENTS !=0 :
            for i in range(NUMBER_SEGMENTS):
                SEGMENT_X = self.Segments[i][0]
                SEGMENT_Y = self.Segments[i][1]
                if SEGMENT_X == PLAYER_X and SEGMENT_Y == PLAYER_Y:
                    self.Position.x = 800
                    self.Position.y = 640
                    self.Segments.clear()
                    self.Score = 0
                    self.Dead = True
                    main_menu.menu_showed = False
                    return
                pygame.draw.rect(gdata.screen,PLAYER_COLOR,pygame.Rect(SEGMENT_X,SEGMENT_Y,GRID_SIZE,GRID_SIZE))
        gdata.screen.blit(gdata.font.render('Score:' + SCORE_AS_STRING , True, (255, 255, 255)), (GRID_SIZE, GRID_SIZE))