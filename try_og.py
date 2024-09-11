from setting import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("womp")
clock = pygame.time.Clock()
running = True
is_finished = False

matrix = [[0 for width in range(50)] for height in range(25)]
player_start = matrix[0][0] = 1

for i in range(20):
    location_x = random.randrange(0, WIDTH, TILE_SIZE)
    location_y = random.randrange(0, HEIGHT, TILE_SIZE)
    x = int(location_x / TILE_SIZE)
    y = int(location_y / TILE_SIZE)
    matrix[y][x] = 'x'

while running:
    screen.fill(COLOR_BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if matrix[row][col] == 'x':
                screen.blit(GRASS, ((row * TILE_SIZE), (col * TILE_SIZE)))
    screen.blit(FLAG, (WIDTH - 55, HEIGHT - 65))
    screen.blit(SOLDIER, (move_x, move_y))
    key = pygame.key.get_pressed()
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
    pygame.display.update()
