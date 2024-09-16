from setting import *
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
running = True

is_win = False
is_lose = False
wait = False
read = False
write = False
last = 0
now = 0
save_flag = False

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
    location_x = random.randrange(0, WIDTH - (TILE_SIZE * 2), (TILE_SIZE * 2))
    location_y = random.randrange(0, HEIGHT, TILE_SIZE)
    if not (grass_list[i - 1][0] == location_x and grass_list[i - 1][1] == location_y):
        grass_list[i][0] = location_x
        grass_list[i][1] = location_y
        i += 1

i = 0
while i < 20:
    location_x = random.randrange(0, (WIDTH - (TILE_SIZE * 2)), (TILE_SIZE * 3))
    location_y = random.randrange(0, HEIGHT, TILE_SIZE)
    x = int(location_x / TILE_SIZE)
    y = int(location_y / TILE_SIZE)
    if matrix[y][x] != 'x':
        mine_list.append([])
        for j in range(3):
            matrix[y][x + j] = 'x'
            mine_list[i].append(x + j)
        mine_list[i].append(y)
        i += 1


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
            if read:
               pass
            else:
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
        # for row in matrix:
        #     print(row)
        # print()

    for save in range(9):
        if key[SAVE_KEYS_LIST[save]]:
            if len(time_last) == 0 and len(key_pressed) == 0:
                time_last.append(pygame.time.get_ticks())
                key_pressed.append(SAVE_KEYS_LIST[save])
                save_flag = True

    if save_flag and not key[key_pressed[0]]:
        now = pygame.time.get_ticks()
        if now - time_last[0] >= 1000:
            read = True
        else:
            write = True
        save_flag = False
        time_last.clear()
        key_pressed.clear()

    # for save in range(9):
    #     if key[SAVE_KEYS_LIST[save]]:
    #         pygame.time.wait(1000)
    #         if key[SAVE_KEYS_LIST[save]]:
    #             read = True
    #         else:
    #             write = True
    if write:
        file = open('memory.txt', 'w')
        file.write("grass location: \n")
        for grass in range(20):
            file.write(f"{grass_list[grass][0]}, {grass_list[grass][1]} \n")

        file.write('\n'"mine index: \n")
        for mine in range(20):
            file.write(f"({mine_list[mine][0]}, {mine_list[mine][1]} , {mine_list[mine][2]}), ({mine_list[mine][3]}) \n")

        file.write('\n'"player location: \n")
        file.write(f"{move_x} {move_y}")
        file.close()
        write = False
        print(")))))))))")

    elif read:
        file = open('memory.txt', 'r')
        print(file.readlines())
        file.close()
        read = False

    if read:
        file = open('memory.txt', 'r')
        player_location = file.read(46)
        player_location.split(' ')
        move_x = int(player_location[0])
        move_y = int(player_location[1])
        screen.blit(SOLDIER, (move_x, move_y))
        file.close()
        read = False
    else:
        screen.blit(SOLDIER, (move_x, move_y))
    screen.blit(FLAG, ((47 * TILE_SIZE), (21 * TILE_SIZE)))

    pygame.display.update()
