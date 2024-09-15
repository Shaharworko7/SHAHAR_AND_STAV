from setting import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("womp")
clock = pygame.time.Clock()
running = True
wait = False

matrix = [[0 for width in range(50)] for height in range(25)]

i = 0
while i < 20:
    grass_list.append(['', ''])
    location_x = random.randrange(0, WIDTH - (TILE_SIZE * 2), TILE_SIZE)
    location_y = random.randrange(0, HEIGHT, TILE_SIZE)
    if not (grass_list[i - 1][0] == location_x and grass_list[i - 1][1] == location_y):
        grass_list[i][0] = location_x
        grass_list[i][1] = location_y
        i += 1

i = 0
while i < 20:
    location_x = random.randrange(0, (WIDTH - (TILE_SIZE * 2)), TILE_SIZE)
    location_y = random.randrange(0, HEIGHT, TILE_SIZE)
    x = int(location_x / TILE_SIZE)
    y = int(location_y / TILE_SIZE)
    if matrix[y][x] != 'x':
        i += 1
        for j in range(3):
            matrix[y][x + j] = 'x'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        screen.fill(SQUARES_COLOR)
        for row in range(25):
            for col in range(50):
                pygame.draw.rect(screen, (COLOR_BG), [(TILE_SIZE) * col, (TILE_SIZE) * row, WIDTH, HEIGHT], 1)
        for row in range(GRID_HEIGHT):
            col = 0
            while col < GRID_WIDTH:
                if matrix[row][col] == 'x':
                    location_y = row * TILE_SIZE
                    location_x = col * TILE_SIZE
                    screen.blit(MINE, (location_x, location_y))
                    col += 2
                col += 1

        for row in matrix:
            print(row)
        wait = True
    elif wait:
        pygame.time.wait(1000)
        wait = False

    else:
        screen.fill(COLOR_BG)
        for row in range(20):
            screen.blit(GRASS, (grass_list[row][0], grass_list[row][1]))
        if key[pygame.K_RIGHT] and move_x < WIDTH - 55:
            move_x += TILE_SIZE
            pygame.time.wait(100)

            for row in matrix:
                print(row)
        if key[pygame.K_LEFT] and move_x > 1:
            move_x -= TILE_SIZE
            pygame.time.wait(100)

            for row in matrix:
                print(row)
        if key[pygame.K_UP] and move_y > 1:
            move_y -= TILE_SIZE
            pygame.time.wait(100)

            for row in matrix:
                print(row)
        if key[pygame.K_DOWN] and move_y < HEIGHT - 65:
            move_y += TILE_SIZE
            pygame.time.wait(100)

            for row in matrix:
                print(row)

        screen.blit(FLAG, (WIDTH - 50, HEIGHT - 66))
    screen.blit(SOLDIER, (move_x, move_y))

    pygame.display.update()
