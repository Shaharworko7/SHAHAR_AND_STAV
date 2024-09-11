from setting import *

class GridBlock(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface(TILE_SIZE, TILE_SIZE)
        self.image.fill(COLOR_BG)
        self.rect = self.image.get_rect(top_left = pos)
