import pygame
import sys
from settings import *
from levels import Level


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.state = "start"
        self.font = pygame.font.Font("assets\\Font.ttf", 100)
        self.font_small = pygame.font.Font("assets\\Font.ttf", 50)

        self.levels = level_list
        self.current_level = 1
        self.previous_level = 1
        self.level = Level(self.levels[self.current_level - 1], self.surface)

    def intro(self):
        text = self.font.render(game_name,False, "blue")
        menu = self.font_small.render("MENU", False, "blue")
        space = self.font_small.render("Press Space to Start Game", False, "blue")
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
        menu_rect = text.get_rect(center=(screen_width/2+18 0, screen_height/2+120))
        space_rect = text.get_rect(center=(screen_width/2-90, screen_height/2+170))
        self.surface.blit(text, text_rect)
        self.surface.blit(menu, menu_rect)
        self.surface.blit(space, space_rect)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.state = "level"
            self.current_level, self.previous_level = 1, 1

    def run(self, space_key):
        if self.state == "start":
            self.intro()
        elif self.state == "level":
            self.level.run(space_key)
