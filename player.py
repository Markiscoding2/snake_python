import pygame
import random
from pygame import *


class Player:
    def __init__(self,screen):
        self.GRID_SIZE = 40
        self.Position = Vector2(800, 640)
        self.Segments = [] 
        self.Score = 0
        self.Dead = False
        self.Current_Direction = [0,0,0,0]
        self.Apple_Position = Vector2(random.randrange(self.GRID_SIZE,1920,40),random.randrange(self.GRID_SIZE,1080 ,40))
        

    def add_segment(self):
        self.Segments.append([self.Position.x,self.Position.y])
    
    def Movement(self,gdata):
        current_pressed_key = pygame.key.get_pressed()
        
        if current_pressed_key[pygame.K_ESCAPE]:
            gdata.running = False
        if current_pressed_key[pygame.K_a] and self.Current_Direction[1] == False or len(self.Segments) == 0 and current_pressed_key[pygame.K_a]:
            self.Current_Direction[0] = True
            self.Current_Direction[1] = False
            self.Current_Direction[2] = False
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_d] and self.Current_Direction[0] == False or len(self.Segments) == 0 and current_pressed_key[pygame.K_d]:
            self.Current_Direction[0] = False
            self.Current_Direction[1] = True
            self.Current_Direction[2] = False
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_w] and self.Current_Direction[3] == False or len(self.Segments) == 0 and current_pressed_key[pygame.K_w]:     
            self.Current_Direction[0] = False
            self.Current_Direction[1] = False
            self.Current_Direction[2] = True
            self.Current_Direction[3] = False
        if current_pressed_key[pygame.K_s] and self.Current_Direction[2] == False or len(self.Segments) == 0 and current_pressed_key[pygame.K_s]: 
            self.Current_Direction[0] = False
            self.Current_Direction[1] = False
            self.Current_Direction[2] = False
            self.Current_Direction[3] = True

        self_pos_changed = False
        old_plr_x=self.Position.x
        old_plr_y=self.Position.y
        if(self.Current_Direction[0] and self.Position.x > 0 ):
            self.Position.x -= self.GRID_SIZE
            self_pos_changed = True
        if(self.Current_Direction[1] and self.Position.x < 1880):  
            self.Position.x += self.GRID_SIZE
            self_pos_changed = True
        if(self.Current_Direction[2] and self.Position.y > 0):
            self.Position.y -= self.GRID_SIZE
            self_pos_changed = True
        if(self.Current_Direction[3] and self.Position.y < 1040):
            self.Position.y += self.GRID_SIZE
            self_pos_changed = True
        
        if self_pos_changed :
            if len(self.Segments) != 0:
                for i in range(len(self.Segments) - 1, 0, -1):
                    self.Segments[i] = self.Segments[i-1]
                self.Segments[0]=[old_plr_x,old_plr_y]

    

    def Eating(self):
        if self.Position.x == self.Apple_Position[0] and self.Position.y == self.Apple_Position[1]: 
            self.Apple_Position[0] = random.randrange(self.GRID_SIZE,1920,40)
            self.Apple_Position[1] = random.randrange(self.GRID_SIZE,1080,40)
            self.Score+=1
            self.add_segment()
        