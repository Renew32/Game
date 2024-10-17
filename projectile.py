import pygame
from pygame.sprite import Group


#definir la classer qui va gerer le projectile du joueur

class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de la classe
    def __init__(self, player) :
        super().__init__()
        self.player = player
        self.velocity = 1.075
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self,player):
        """if self.rect.x == player.rect.x:
            if player"""

        self.rect.x += self.velocity
        self.rotate()
        #verifier si le projectile n'est plus sur l'ecran
        if self.rect.x > 1080:
            self.remove()


    def rotate(self):
        #tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
