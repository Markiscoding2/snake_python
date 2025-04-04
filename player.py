import pygame
import random
from collections import deque
from pygame import *


class Player:
    def __init__(self):
        self.GRID_SIZE = 40

        self.START_WIDTH = 800
        self.START_HEIGHT = 640

        self.X_BOUNDS = 1880
        self.Y_BOUNDS = 1040

        self.apple_sprite = pygame.image.load("src/sprites/apple.png")

        self.position = Vector2(self.START_WIDTH, self.START_HEIGHT)
        self.direction = Vector2(0, 0)

        self.segments = deque()
        self.score = 0

        self.dead = False
        self.apple_position = Vector2(
            random.randrange(self.GRID_SIZE, self.X_BOUNDS, self.GRID_SIZE),
            random.randrange(self.GRID_SIZE, self.Y_BOUNDS, self.GRID_SIZE),
        )

    def add_segment(self):
        self.segments.append([self.position.x, self.position.y])

    def Movement(self, gdata,main_menu):

        current_pressed_key = pygame.key.get_pressed()
        if current_pressed_key[pygame.K_ESCAPE]:
            gdata.running = False


        if current_pressed_key[pygame.K_a] and self.direction.x == 0 and not current_pressed_key[pygame.K_w] and not current_pressed_key[pygame.K_s] :
            self.direction = Vector2(-1, 0)

        if current_pressed_key[pygame.K_d] and self.direction.x == 0 and not current_pressed_key[pygame.K_w] and not current_pressed_key[pygame.K_s]:
            self.direction = Vector2(1, 0)

        if current_pressed_key[pygame.K_w] and self.direction.y == 0:

            self.direction = Vector2(0, -1)

        if current_pressed_key[pygame.K_s] and self.direction.y == 0:
            self.direction = Vector2(0, 1)

        if self.direction == Vector2(0, 0):
            return

        new_position = self.position + self.direction * self.GRID_SIZE

        if not gdata.solid_wall:
            if new_position.x < 0:
                new_position.x = self.X_BOUNDS
            elif new_position.x > self.X_BOUNDS:
                new_position.x = 0
                
            if new_position.y < 0:
                new_position.y = self.Y_BOUNDS
            elif new_position.y > self.Y_BOUNDS:
                new_position.y = 0
        
            if 0 <= new_position.x <= self.X_BOUNDS and 0 <= new_position.y <= self.Y_BOUNDS:
                old_position = self.position
                self.position = new_position

                if self.segments:
                    self.segments.appendleft(old_position)
                    self.segments.pop()
        else:
            if new_position.x <= 0 or new_position.x >= self.X_BOUNDS or new_position.y <= 0 or new_position.y >= self.Y_BOUNDS:
                self.dead = True
                main_menu.menu_showed = False
                self.position = (800, 640)
                self.segments.clear()
                self.score = 0
                return

            if 0 < new_position.x < self.X_BOUNDS and 0 < new_position.y < self.Y_BOUNDS:
                old_position = self.position
                self.position = new_position

                if self.segments:
                    self.segments.appendleft(old_position)
                    self.segments.pop()


    def Eating(self):

        if self.position == self.apple_position:
            EATING_SFX = pygame.mixer.Sound("src\SFX\eating_SFX.mp3")
            EATING_SFX.play()
            axy = Vector2(
                random.randrange(self.GRID_SIZE, self.X_BOUNDS, self.GRID_SIZE),
                random.randrange(self.GRID_SIZE, self.Y_BOUNDS, self.GRID_SIZE)
            )
            while any(segment == axy for segment in self.segments):
                axy = Vector2(
                    random.randrange(self.GRID_SIZE, self.X_BOUNDS, self.GRID_SIZE),
                    random.randrange(self.GRID_SIZE, self.Y_BOUNDS, self.GRID_SIZE),
                )
            

            self.apple_position = Vector2(
                random.randrange(self.GRID_SIZE, self.X_BOUNDS, self.GRID_SIZE),
                random.randrange(self.GRID_SIZE, self.Y_BOUNDS, self.GRID_SIZE),
            )
            self.score += 1
            self.add_segment()

    def rendering(self, gdata, main_menu):
        PLAYER_X, PLAYER_Y = self.position

        # APPLE_X, APPLE_Y = self.apple_position

        GRID_SIZE = self.GRID_SIZE

        PLAYER_COLOR = "green"

        gdata.screen.blit(
            self.apple_sprite,
            (
                self.apple_position.x,
                self.apple_position.y,
            ),
        )
        pygame.draw.rect(
            gdata.screen,
            PLAYER_COLOR,
            pygame.Rect(PLAYER_X, PLAYER_Y, GRID_SIZE, GRID_SIZE),
        )
        for segment in self.segments:  # pentru fiecare segment in segmentele jucatorului
            
            if segment == self.position:  # daca segmentul este in pozitia jucatorului atunci jucatorul moare
                self.position = (800, 640)
                self.segments.clear()
                self.score = 0
                self.dead = True
                main_menu.menu_showed = False
                return
            pygame.draw.rect(
                gdata.screen,
                PLAYER_COLOR,
                pygame.Rect(segment.x, segment.y, GRID_SIZE, GRID_SIZE),
            )
        gdata.screen.blit(
            gdata.font.render(f"Score: {self.score}", True, (255, 0, 0)),
            (GRID_SIZE, GRID_SIZE),
        )
