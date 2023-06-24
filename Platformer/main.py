import pygame as py
from settings import *
from Game import Game
import sys

py.init()

screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption(game_name)

clock = py.time.Clock()

game = Game(screen)

background = py.image.load("assets\\BG.png").convert()

while True:
    space = False

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if (event.key == py.K_UP) or (event.key == py.K_SPACE) or (event.key == py.K_s):
                space = True


    screen.fill('black')
    screen.blit(background, (0, 0))
    game.run(space)
    py.display.update()
    clock.tick(FrameRate)
