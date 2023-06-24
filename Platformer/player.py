import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Loading the image and making it into the proper dimensions
        self.image = pygame.Surface((32, 64))  # pygame.transform.scale((pygame.image.load("assets\\player.png")).convert_alpha(), (64, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = player_speed
        self.gravity = player_gravity
        self.jump_speed = -(player_jump_height)
        self.current_double_jumps = 0

    def get_input(self, space_key):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if space_key:
            if self.current_double_jumps < double_jumps:
                self.current_double_jumps += 1
                self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self, space_key):
        self.get_input(space_key)

