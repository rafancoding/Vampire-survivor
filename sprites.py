from settings import *
from math import atan2,degrees 

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
        #connection to player
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(0,1)

        #gun setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join("images/gun/gun.png")).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_direction * self.distance)
    
    #getting direction
    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()

    def rotate_gun(self):
        angle =  degrees(atan2(self.player_direction.x,self.player_direction.y)) - 90
        if self.player_direction.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surf,angle,1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf,abs(angle),1)
            self.image = pygame.transform.flip(self.image,False,True)

    #update
    def update(self,_):
        self.get_direction()
        self.rotate_gun()  
        self.rect.center = self.player.rect.center + self.player_direction * self.distance 

#the bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self,surf,pos,direction,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

        self.direction = direction
        self.speed = 1200

        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000


    def update(self,dt):
        self.rect.center += self.direction * self.speed * dt

        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()

#enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self,groups,pos,frames,collision_sprites,player):
        super().__init__(groups)
        self.player = player

        #image variables
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.animation_speed = 6

        #rects
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-20,-40)

        #collision sprites
        self.collision_sprites = collision_sprites

        #movement variables
        self.direction = pygame.Vector2()
        self.speed = 350
    
    def animate(self,dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]



    def update(self,dt):
        #self.move(dt)
        self.animate(dt)

            



        


