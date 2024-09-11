import pygame
import random
import sys
from setting import *
from sprites import *


# stav try:
# screen_grid = Grid(matrix=matrix_game)
# x = 1
# y = 1
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = pygame.sprite.Group()

    def matrix(self):
        matrix_game = [[0 for width in range(50)] for height in range(25)]

        for row in matrix_game:
            for id in row:
                if id == 0:
                    pass

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(COLOR_BG)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
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
        # self.all_sprites = pygame.sprite.Group
        #
        # GridBlock((0, 0), self.all_sprites)

        # self.all_sprites.update()
        #
        # self.screen.fill(COLOR_BG)
        # self.screen.blit(FLAG, (WIDTH - 80, HEIGHT - 95))
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
        # pygame.display.update()
    if __name__ == "__main__":
        game = Game()
        game.run()
