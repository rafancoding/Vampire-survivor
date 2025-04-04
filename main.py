from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
import os

from random import randint

#literal game
class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("vampire survivor")
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.map()

        #sprites
        self.player = Player((400,300),self.all_sprites,self.collision_sprites)

    def map(self):
        map = load_pygame(("data/maps/world.tmx"))
        for obj in map.get_layer_by_name("Objects"):
            CollisionSprites((obj.x,obj.y),obj.image,(self.all_sprites,self.collision_sprites))

        for x,y,image in map.get_layer_by_name("Ground").tiles():
            NonCollisionSprites((x,y),image,self.all_sprites)
       

    def run(self):
        while self.running:

            #dt
            dt = self.clock.tick() / 1000

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #update
            self.all_sprites.update(dt)

            #draw
            self.display_surface.fill("black")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":            
    game = Game()     
    game.run()            
            
        

            
    


    
