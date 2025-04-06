from settings import * 

#only ground
class NonCollisionSprites(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

#everything else
class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

#the gun
class Gun(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(0,1)

        super().__init__(groups)
        self.gun_surf = pygame.image.load("images/gun/gun.png").convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_direction * self.distance)
    
    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()
        print(self.player_direction)

    def update(self,_):
        self.get_direction  
        self.rect.center = self.player.rect.center + self.player_direction * self.distance 

