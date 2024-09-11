import pygame
import random
from setting import *

# stav try:
# screen_grid = Grid(matrix=matrix_game)

x = 1
y = 1

class Game:
    x = 1
    y = 1
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def matrix(self):
        matrix_game = [[0 for height in range(25)] for width in range(50)]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # def draw_grid(self):
            #     for i in range(0, WIDTH, TILE_SIZE):
            #         pygame.draw.line(self.screen, (0,0,0), (i, 0), (i, HEIGHT))
            #     for j in range(0, HEIGHT, TILE_SIZE):
            #         pygame.draw.line(self.screen, (0,0,0), (0, j), (WIDTH, j))
            # for i in range(20):
            #     location_x = random.randint(0, 50)
            #     location_y = random.randint(0, 25)
            #     matrix_game[location_y][location_x] = GRASS
            #     screen.blit(matrix_game[location_y][location_x], 1,1)
            self.all_sprites = pygame.sprite.Group
            self.all_sprites.update()

            self.screen.fill(COLOR_BG)
            self.screen.blit(FLAG, (WIDTH - 80, HEIGHT - 95))
            # self.screen.blit(SOLDIER, (x, y))
            #
            # key = pygame.key.get_pressed()
            # if key[pygame.K_RIGHT] and x < WIDTH - 70:
            #     x += 1
            # if key[pygame.K_LEFT] and x > 1:
            #     x -= 1
            # if key[pygame.K_UP] and y > 1:
            #     y -= 1
            # if key[pygame.K_DOWN] and y < HEIGHT - 80:
            #     y += 1
            pygame.display.update()
        pygame.quit()
