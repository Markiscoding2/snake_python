import pygame
import random
from pygame import *


class Player:
    def __init__(self,screen):
        self.Position = Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.Segments = [] 
        self.Score = 0
        self.Dead = False
        self.Current_Direction = [0,0,0,0]
        self.Apple_Position = Vector2(random.randrange(0,1920,20),random.randrange(0,1080,20))

    def add_segment(self):
        self.Segments.append([self.Position.x,self.Position.y])
    
    def Movement(self,running):
        current_pressed_key = pygame.key.get_pressed()
        
        if current_pressed_key[pygame.K_ESCAPE]:
            running = False
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
        if(self.Current_Direction[0] and self.Position.x > 20 ):
            self.Position.x -= 20
            self_pos_changed = True
        if(self.Current_Direction[1] and self.Position.x < 1900):  
            self.Position.x += 20
            self_pos_changed = True
        if(self.Current_Direction[2] and self.Position.y > 20):
            self.Position.y -= 20
            self_pos_changed = True
        if(self.Current_Direction[3] and self.Position.y < 1060):
            self.Position.y += 20
            self_pos_changed = True
        
        if self_pos_changed :
            if len(self.Segments) != 0:
                for i in range(len(self.Segments) - 1, 0, -1):
                    self.Segments[i] = self.Segments[i-1]
                self.Segments[0]=[old_plr_x,old_plr_y]

    

    def Eating(self):
        if self.Position.x == self.Apple_Position[0] and self.Position.y == self.Apple_Position[1]: 
            self.Apple_Position[0] = random.randrange(20,1900,20)
            self.Apple_Position[1] = random.randrange(20,1060,20)
            self.Score+=1
            self.add_segment()
        