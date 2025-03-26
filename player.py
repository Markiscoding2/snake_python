import pygame
import random
from collections import deque
from pygame import *


class Player:
    def __init__(self):
        self.GRID_SIZE = 40

        self.START_WIDTH = 800
        self.START_HEIGHT = 640

        self.X_BOUNDS = [1880, 0]
        self.Y_BOUNDS = [1040, 0]

        self.APPLE_WIDTH = 1880
        self.APPLE_HEIGHT = 1040

        self.position = Vector2(self.START_WIDTH, self.START_HEIGHT)
        self.direction = Vector2(0, 0)

        self.segments = deque()
        self.score = 0

        self.dead = False
        self.apple_position = Vector2(
            random.randrange(self.GRID_SIZE, self.APPLE_WIDTH, self.GRID_SIZE),
            random.randrange(self.GRID_SIZE, self.APPLE_HEIGHT, self.GRID_SIZE),
        )

    def add_segment(self):
        self.segments.append([self.position.x, self.position.y])

    def Movement(self, gdata):

        current_pressed_key = pygame.key.get_pressed()
        nr_segments = len(self.segments)

        if current_pressed_key[pygame.K_ESCAPE]:
            gdata.running = False

        if current_pressed_key[pygame.K_a] and self.direction.x == 0:
            self.direction = Vector2(-1, 0)

        if current_pressed_key[pygame.K_d] and self.direction.x == 0:
            self.direction = Vector2(1, 0)

        if current_pressed_key[pygame.K_w] and self.direction.y == 0:

            self.direction = Vector2(0, -1)

        if current_pressed_key[pygame.K_s] and self.direction.y == 0:
            self.direction = Vector2(0, 1)

        if self.direction == Vector2(0, 0):
            return

        new_position = self.position + self.direction * self.GRID_SIZE

        if self.X_BOUNDS[1] < new_position.x < self.X_BOUNDS[0] and self.Y_BOUNDS[1] < new_position.y < self.Y_BOUNDS[0]:
            old_position = self.position
            self.position = new_position

            if self.segments:
                self.segments.appendleft(old_position)
                self.segments.pop()

    def Eating(self):
        EATING_SFX = pygame.mixer.Sound("src\SFX\eating_SFX.mp3")

        if self.position == self.apple_position:

            EATING_SFX.play()
            self.apple_position = Vector2(
                random.randrange(self.GRID_SIZE, self.APPLE_WIDTH, self.GRID_SIZE),
                random.randrange(self.GRID_SIZE, self.APPLE_WIDTH, self.GRID_SIZE),
            )
            self.score += 1
            self.add_segment()

    def rendering(self, gdata, main_menu):
        PLAYER_X, PLAYER_Y = self.position

        APPLE_X, APPLE_Y = self.apple_position

        GRID_SIZE = self.GRID_SIZE

        PLAYER_COLOR = "green"
        APPLE_COLOR = "red"

        pygame.draw.rect(
            gdata.screen,
            APPLE_COLOR,
            pygame.Rect(APPLE_X, APPLE_Y, GRID_SIZE, GRID_SIZE),
        )
        pygame.draw.rect(
            gdata.screen,
            PLAYER_COLOR,
            pygame.Rect(PLAYER_X, PLAYER_Y, GRID_SIZE, GRID_SIZE),
        )
        for segment in self.segments:  # pentru fiecare segment in segmentele jucatorului
            if segment == self.position :  # daca segmentul este in pozitia jucatorului atunci jucatorul moare
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
