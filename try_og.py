from setting import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("womp")
clock = pygame.time.Clock()
running = True
wait = False
i = 0

matrix = [[0 for width in range(50)] for height in range(25)]
player_start = matrix[0][0] = 1

while i < 20:
    location_x = random.randrange(0, WIDTH - (TILE_SIZE * 2), TILE_SIZE)
    location_y = random.randrange(0, HEIGHT - (TILE_SIZE * 2), TILE_SIZE)
    x = int(location_x / TILE_SIZE)
    y = int(location_y / TILE_SIZE)
    if matrix[y][x] != 'g':
        matrix[y][x] = 'g'
        i += 1

i = 0
while i < 20:
    location_x = random.randrange(0, WIDTH - (TILE_SIZE * 3), TILE_SIZE)
    location_y = random.randrange(0, HEIGHT - (TILE_SIZE * 3), TILE_SIZE)
    x = int(location_x / TILE_SIZE)
    y = int(location_y / TILE_SIZE)
    if matrix[y][x] != 'x':
        # matrix[y][x] = 'x'
        i += 1
        for j in range(3):
            if x != GRID_WIDTH - 1:
                matrix[y][x + j] = 'x'
            else:
                matrix[y][x - j] = 'x'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if matrix[row][col] == 'x':
                    location_y = row * TILE_SIZE
                    location_x = col * TILE_SIZE
                    screen.blit(MINE, (location_x, location_y))
        wait = True
    elif wait:
        pygame.time.wait(1000)
        wait = False

    else:
        screen.fill(COLOR_BG)
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                if matrix[row][col] == 'g':
                    location_y = row * TILE_SIZE
                    location_x = col * TILE_SIZE
                    screen.blit(GRASS, (location_x, location_y))
        if key[pygame.K_RIGHT] and move_x < WIDTH - 55:
            move_x += TILE_SIZE
            pygame.time.wait(100)
        if key[pygame.K_LEFT] and move_x > 1:
            move_x -= TILE_SIZE
            pygame.time.wait(100)
        if key[pygame.K_UP] and move_y > 1:
            move_y -= TILE_SIZE
            pygame.time.wait(100)
        if key[pygame.K_DOWN] and move_y < HEIGHT - 65:
            move_y += TILE_SIZE
            pygame.time.wait(100)

    screen.blit(FLAG, (WIDTH - 50, HEIGHT - 66))
    screen.blit(SOLDIER, (move_x, move_y))

    # pygame.time.wait(1000)

    pygame.display.update()
