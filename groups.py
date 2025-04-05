from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def draw(self,target_pos):
        self.offset.x = -target_pos[0]
        for sprite in self:
            self.display_surf.blit(sprite.image,sprite.rect.topleft + self.offset) 