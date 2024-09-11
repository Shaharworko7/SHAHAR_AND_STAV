import pygame
import random
from setting import *

# stav try:
matrix_game = [[0 for height in range(25)] for width in range(50)]
# screen_grid = Grid(matrix=matrix_game)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True
x = 1
y = 1
flag = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-0.png")
soldier = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-e.png")
grass = pygame.image.load("C:\\Users\\jbt\\Desktop\\pygame_grapics\\pixil-frame-green.png")

while running:
    # for i in range(20):
    #     location_x = random.randint(0, 50)
    #     location_y = random.randint(0, 25)
    #     matrix_game[location_y][location_x] = grass
    #     screen.blit(matrix_game[location_y][location_x], 1,1)
    screen.fill(COLOR_BG)

    screen.blit(flag, (670, 280))
    screen.blit(soldier, (x, y))
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
