import pygame
import random
from collections import deque
from pygame import *

def swap(a, b):
    return b, a

class Player:
    def __init__(self):
        self.GRID_SIZE = 40

        self.START_X = 800
        self.START_Y = 640

        self.MAX_X = 1880
        self.MAX_Y = 1040

        self.apple_image = pygame.image.load("src/sprites/apple.png")
        self.golden_apple_image = pygame.image.load("src/sprites/golden_apple.png")
        self.golden_apple_active = False
        
        self.position = Vector2(self.START_X, self.START_Y)
        self.direction = Vector2(0, 0)

        self.body_segments = deque()
        self.golden_apple_positions = deque()
        
        self.score = 0

        self.dead = False
        self.apple_position = Vector2(
            random.randrange(self.GRID_SIZE, self.MAX_X, self.GRID_SIZE),
            random.randrange(self.GRID_SIZE, self.MAX_Y, self.GRID_SIZE),
        )

    def reset(self):
        self.__init__()

    def add_segment(self):
        self.body_segments.append([self.position.x, self.position.y])

    def Movement(self, game_data, main_menu):

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_ESCAPE]:
            game_data.running = False

        if pressed_keys[pygame.K_a] and self.direction.x == 0 and not pressed_keys[pygame.K_w] and not pressed_keys[pygame.K_s]:
            self.direction = Vector2(-1, 0)

        elif pressed_keys[pygame.K_d] and self.direction.x == 0 and not pressed_keys[pygame.K_w] and not pressed_keys[pygame.K_s]:
            self.direction = Vector2(1, 0)

        elif pressed_keys[pygame.K_w] and self.direction.y == 0:
            self.direction = Vector2(0, -1)

        elif pressed_keys[pygame.K_s] and self.direction.y == 0:
            self.direction = Vector2(0, 1)

        elif self.direction == Vector2(0, 0):
            return

        new_position = self.position + self.direction * self.GRID_SIZE

        if not game_data.solid_wall:
            if new_position.x < 0:
                new_position.x = self.MAX_X
            elif new_position.x > self.MAX_X:
                new_position.x = 0
                
            if new_position.y < 0:
                new_position.y = self.MAX_Y
            elif new_position.y > self.MAX_Y:
                new_position.y = 0
        
            if 0 <= new_position.x <= self.MAX_X and 0 <= new_position.y <= self.MAX_Y:
                old_position = self.position
                self.position = new_position

                if self.body_segments:
                    self.body_segments.appendleft(old_position)
                    self.body_segments.pop()
        else:
            if new_position.x <= 0 or new_position.x >= self.MAX_X or new_position.y <= 0 or new_position.y >= self.MAX_Y:
                self.is_dead = True
                main_menu.menu_showed = False
                self.position = (self.START_X, self.START_Y)
                self.body_segments.clear()
                self.score = 0
                return

            if 0 < new_position.x < self.MAX_X and 0 < new_position.y < self.MAX_Y:
                old_position = self.position
                self.position = new_position

                if self.body_segments:
                    self.body_segments.appendleft(old_position)
                    self.body_segments.pop()

    def Eating(self, game_data):
        if self.golden_apple_active:
            if self.position in self.golden_apple_positions:
                eating_sound = pygame.mixer.Sound("src/SFX/eating_SFX.mp3")
                eating_sound.play()
                self.golden_apple_positions.remove(self.position)
                self.score += 1
                self.add_segment()
                
            if len(self.golden_apple_positions) == 0:
                self.golden_apple_active = False
                self.golden_apple_positions.clear()

        if self.position == self.apple_position:
            eating_sound = pygame.mixer.Sound("src/SFX/eating_SFX.mp3")
            eating_sound.play()
            new_apple_position = Vector2(
                random.randrange(self.GRID_SIZE, self.MAX_X, self.GRID_SIZE),
                random.randrange(self.GRID_SIZE, self.MAX_Y, self.GRID_SIZE)
            )
            while new_apple_position in self.body_segments or new_apple_position == self.position:
                new_apple_position = Vector2(
                    random.randrange(self.GRID_SIZE, self.MAX_X, self.GRID_SIZE),
                    random.randrange(self.GRID_SIZE, self.MAX_Y, self.GRID_SIZE)
                )
            if game_data.golden_apple and not self.golden_apple_active:
                if random.randint(0, 49) == 0:
                    self.golden_apple_active = True
                    for _ in range(5):
                        self.golden_apple_positions.append(
                            Vector2(
                                random.randrange(self.GRID_SIZE, self.MAX_X, self.GRID_SIZE),
                                random.randrange(self.GRID_SIZE, self.MAX_Y, self.GRID_SIZE)
                            )
                        )      
            self.apple_position = new_apple_position
            self.score += 1
            self.add_segment()

    def rendering(self, game_data, main_menu):
        player_x, player_y = self.position

        grid_size = self.GRID_SIZE

        player_color = "green"
        
        if self.golden_apple_active:
            for golden_apple in self.golden_apple_positions:
                game_data.screen.blit(
                    self.golden_apple_image,
                    (
                        golden_apple.x,
                        golden_apple.y,
                    ),
                )
        game_data.screen.blit(
            self.apple_image,
            (
                self.apple_position.x,
                self.apple_position.y,
            ),
        )

        pygame.draw.rect(
            game_data.screen,
            player_color,
            pygame.Rect(player_x, player_y, grid_size, grid_size),
        )
        
        if self.position in self.body_segments:
            self.reset()
            game_data.reset()
            main_menu.menu_showed = False
            self.is_dead = True
            
        for segment in self.body_segments:
            pygame.draw.rect(
                game_data.screen,
                player_color,
                pygame.Rect(segment.x, segment.y, grid_size, grid_size),
            )
        game_data.screen.blit(
            game_data.font.render(f"Score: {self.score}", True, (255, 0, 0)),
            (grid_size, grid_size),
        )