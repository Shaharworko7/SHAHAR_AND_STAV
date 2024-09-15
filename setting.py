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

player_rows = {
    "player_body_row1": 0,
    "player_body_row2": 1,
    "player_body_row3": 2,
    "player_feet_row": 3
}

player_left_col = 0
player_right_col = 1


move_x = 1
move_y = 1

# stav graphics
FLAG = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-flag.png")
SOLDIER = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-33.png")
GRASS = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-green.png")
MINE = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-0.png")


