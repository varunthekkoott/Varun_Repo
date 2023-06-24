import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size, image):
        super().__init__()
        self.type = image
        self.image = pygame.transform.scale((pygame.image.load(f"assets\\Tiles\\{image}.png")).convert_alpha(), (size, size))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self,x_shift):
        self.rect.x += x_shift
