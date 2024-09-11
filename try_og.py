# import pygame
# import random
# from sprites import *
from setting import *


# stav try:
# screen_grid = Grid(matrix=matrix_game)

class Game:
    matrix_game = [[0 for width in range(50)] for height in range(25)]

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("womp")
    clock = pygame.time.Clock()
    running = True

    while running:
        # for i in range(20):
        #     location_x = random.randint(0, 49)
        #     location_y = random.randint(0, 24)
        #     grass_loc = matrix_game[location_y][location_x] = screen.blit(grass, (2, 2))
            # screen.blit(grass_loc)
            # screen.blit(matrix_game[location_y][location_x], (location_x , location_y))
        screen.fill(COLOR_BG)
        screen.blit(FLAG, (WIDTH - 80, HEIGHT - 95))
        screen.blit(SOLDIER, (move_x, move_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and move_x < WIDTH - 70:
            move_x += 1
        if key[pygame.K_LEFT] and move_x > 1:
            move_x -= 1
        if key[pygame.K_UP] and move_y > 1:
            move_y -= 1
        if key[pygame.K_DOWN] and move_y < HEIGHT - 80:
            move_y += 1
        pygame.display.update()
