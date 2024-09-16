from setting import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True

is_win = False
is_lose = False
wait = False

X = 800
Y = 400
font = pygame.font.Font(None, 100)
lose_text = font.render("YOU LOSE!", True, (255, 255, 255))
win_text = font.render("YOU WIN!", True, (255, 255, 255))
textRect = lose_text.get_rect()
textRect.center = (X // 2, Y // 2)

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

for row in range(21, 25):
    for col in range(47, 50):
        matrix[row][col] = 'flag'

# game loop:
while running:
    if is_lose or is_win:
        pygame.time.wait(3000)
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if wait:
        pygame.time.wait(1000)
        wait = False

    else:
        screen.fill(COLOR_BG)
        for row in range(20):
            screen.blit(GRASS, (grass_list[row][0], grass_list[row][1]))

        # player move right:
        if key[pygame.K_RIGHT] and move_x < WIDTH - 33:
            move_x += TILE_SIZE
            player_left_col += 1
            player_right_col += 1
            if (matrix[player_rows["player_feet_row"]][player_left_col] != 'x'
                    and matrix[player_rows["player_feet_row"]][player_right_col] != 'x'):
                for i in range(3):
                    if (matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_left_col] == 'flag'
                            or matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_right_col] == 'flag'):
                        is_win = True

                if not is_win and (matrix[player_rows["player_feet_row"]][player_left_col] != 'flag'
                                   and matrix[player_rows["player_feet_row"]][player_right_col] != 'flag'):
                    matrix[player_rows["player_feet_row"]][player_left_col] = 'P'
                    matrix[player_rows["player_feet_row"]][player_right_col] = 'P'
            else:
                is_lose = True
            pygame.time.wait(100)

        # player move left:
        if key[pygame.K_LEFT] and move_x > 1:
            move_x -= TILE_SIZE
            player_left_col -= 1
            player_right_col -= 1
            if (matrix[player_rows["player_feet_row"]][player_left_col] != 'x'
                    and matrix[player_rows["player_feet_row"]][player_right_col] != 'x'):
                for i in range(3):
                    if (matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_left_col] == 'flag'
                            or matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_right_col] == 'flag'):
                        is_win = True

                if not is_win and (matrix[player_rows["player_feet_row"]][player_left_col] != 'flag'
                                   and matrix[player_rows["player_feet_row"]][player_right_col] != 'flag'):
                    matrix[player_rows["player_feet_row"]][player_left_col] = 'P'
                    matrix[player_rows["player_feet_row"]][player_right_col] = 'P'
            else:
                is_lose = True
            pygame.time.wait(100)

        # player move up:
        if key[pygame.K_UP] and move_y > 1:
            move_y -= TILE_SIZE
            for i in range(4):
                player_rows[PLAYER_DICT_K_LIST[i]] -= 1
            if (matrix[player_rows["player_feet_row"]][player_left_col] != 'x'
                    and matrix[player_rows["player_feet_row"]][player_right_col] != 'x'):
                for i in range(3):
                    if (matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_left_col] == 'flag'
                            or matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_right_col] == 'flag'):
                        is_win = True

                if not is_win and (matrix[player_rows["player_feet_row"]][player_left_col] != 'flag'
                                   and matrix[player_rows["player_feet_row"]][player_right_col] != 'flag'):
                    matrix[player_rows["player_feet_row"]][player_left_col] = 'P'
                    matrix[player_rows["player_feet_row"]][player_right_col] = 'P'
            else:
                is_lose = True
            pygame.time.wait(100)

        # player move down:
        if key[pygame.K_DOWN] and move_y < HEIGHT - 65:
            move_y += TILE_SIZE
            for i in range(4):
                player_rows[PLAYER_DICT_K_LIST[i]] += 1
            if (matrix[player_rows["player_feet_row"]][player_left_col] != 'x'
                    and matrix[player_rows["player_feet_row"]][player_right_col] != 'x'):
                for i in range(3):
                    if (matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_left_col] == 'flag'
                            or matrix[player_rows[PLAYER_DICT_K_LIST[i]]][player_right_col] == 'flag'):
                        is_win = True

                if not is_win and (matrix[player_rows["player_feet_row"]][player_left_col] != 'flag'
                                   and matrix[player_rows["player_feet_row"]][player_right_col] != 'flag'):
                    matrix[player_rows["player_feet_row"]][player_left_col] = 'P'
                    matrix[player_rows["player_feet_row"]][player_right_col] = 'P'
            else:
                is_lose = True
            pygame.time.wait(100)

    if is_lose or is_win or key[pygame.K_RETURN]:
        screen.fill(SQUARES_COLOR)
        for row in range(25):
            for col in range(50):
                pygame.draw.rect(screen, COLOR_BG, [TILE_SIZE * col, TILE_SIZE * row, WIDTH, HEIGHT], 1)
        for row in range(GRID_HEIGHT):
            col = 0
            while col < GRID_WIDTH:
                if matrix[row][col] == 'x':
                    location_y = row * TILE_SIZE
                    location_x = col * TILE_SIZE
                    screen.blit(MINE, (location_x, location_y))
                    col += 2
                col += 1
        if is_lose:
            screen.blit(lose_text, textRect)
        elif is_win:
            screen.blit(win_text, textRect)
        else:
            wait = True
        for row in matrix:
            print(row)
        print()

    screen.blit(FLAG, ((47 * TILE_SIZE), (21 * TILE_SIZE)))
    screen.blit(SOLDIER, (move_x, move_y))

    pygame.display.update()