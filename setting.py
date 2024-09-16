import pygame

WIDTH = 800
HEIGHT = 400

TITLE = "soldier game :D"
COLOR_BG = (73, 128, 55)
SQUARES_COLOR = (33, 40, 43)
TILE_SIZE = 16
GRID_WIDTH = int(WIDTH / TILE_SIZE)
GRID_HEIGHT = int(HEIGHT / TILE_SIZE)

grass_list = []
mine_list = []

player_rows = {
    "player_body_row1": 0,
    "player_body_row2": 1,
    "player_body_row3": 2,
    "player_feet_row": 3
}

PLAYER_DICT_K_LIST = ["player_body_row1", "player_body_row2", "player_body_row3", "player_feet_row"]

player_left_col = 0
player_right_col = 1

SAVE_KEYS_LIST = [
    pygame.K_1,
    pygame.K_2,
    pygame.K_3,
    pygame.K_4,
    pygame.K_5,
    pygame.K_6,
    pygame.K_7,
    pygame.K_8,
    pygame.K_9,
]

time_last = []
key_pressed = []

move_x = 1
move_y = 1

# stav graphics
FLAG = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-flag.png")
FLAG = pygame.transform.scale(FLAG, (48, 64))

SOLDIER = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-33.png")
SOLDIER = pygame.transform.scale(SOLDIER, (32, 64))

GRASS = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-green.png")
GRASS = pygame.transform.scale(GRASS, (32, 16))

MINE = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_graphics\\pixil-frame-0.png")
MINE = pygame.transform.scale(MINE, (48, 16))

