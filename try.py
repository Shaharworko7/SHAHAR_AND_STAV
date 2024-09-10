import pygame

# stav try:
pygame.init()
screen = pygame.display.set_mode((750,375))
pygame.display.set_caption("womp")
clock = pygame.time.Clock()
running = True
color = (138, 193, 230)
x = 1
y = 1
flag = pygame.image.load("C:\\Users\\jbt\\Desktop\\pixil-frame-0.png")
soilder = pygame.image.load("C:\\Users\\jbt\\Desktop\\pixil-frame-e.png")


while running:
    screen.fill(color)
    screen.blit(flag, (670, 280))
    screen.blit(soilder, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and x < 685:
        x += 1
    if key[pygame.K_LEFT] and x > 1:
        x -= 1
    if key[pygame.K_UP] and y > 1:
        y -= 1
    if key[pygame.K_DOWN] and y < 275:
        y += 1
    pygame.display.update()
