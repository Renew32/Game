import pygame
from projectile import Projectile

#creation de la classe ( 1er classe) du joueur
class Player(pygame.sprite.Sprite):


    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 0.75
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        #creation de la nouvelle instance de la classe Projectile
        self.all_projectile.add(Projectile(self))




    def move_right (self):

        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left (self):
        self.rect.x -= self.velocity