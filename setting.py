import pygame

WIDTH = 800
HEIGHT = 400
FPS = 60
TITLE = "womp"
COLOR_BG = (95, 158, 47)
TILE_SIZE = 16
GRID_WIDTH = int(WIDTH / TILE_SIZE)
GRID_HEIGHT = int(HEIGHT / TILE_SIZE)

move_x = 1
move_y = 1

# stav graphics
FLAG = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-0.png")
SOLDIER = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-e.png")
GRASS = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-green.png")


