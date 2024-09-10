import pygame

# stav try:
pygame.init()
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("womp")
clock = pygame.time.Clock()
running = True
color = (138, 193, 230)

while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if pygame.key.get_pressed() == :

        pygame.draw.circle(screen, (230, 138, 177), (700, 400), 200, 25)
    pygame.draw.rect(screen, (92, 189, 70), (100, 200, 100, 200))
    pygame.display.update()
