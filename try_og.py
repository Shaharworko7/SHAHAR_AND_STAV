# import pygame
# import random
# from setting import *
from sprites import *

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
        screen.blit(FLAG, (670, 280))
        screen.blit(SOLDIER, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and x < 680:
            x += 1
        if key[pygame.K_LEFT] and x > 1:
            x -= 1
        if key[pygame.K_UP] and y > 1:
            y -= 1
        if key[pygame.K_DOWN] and y < 295:
            y += 1
        pygame.display.update()
