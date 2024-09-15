import pygame

WIDTH = 800
HEIGHT = 400
MARGIN = 1
TITLE = "womp"
COLOR_BG = (73, 128, 55)
SQUARES_COLOR = (33, 40, 43)
TILE_SIZE = 16
GRID_WIDTH = int(WIDTH / TILE_SIZE)
GRID_HEIGHT = int(HEIGHT / TILE_SIZE)
grass_list = []


move_x = 1
move_y = 1

# stav graphics
FLAG = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-flag.png")
SOLDIER = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-33.png")
GRASS = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-green.png")
MINE = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-0.png")


