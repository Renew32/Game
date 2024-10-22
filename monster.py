import pygame

# Cette classe va gerer la notion de monstre 
class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):

        super().__init__()
        self.game = game
        
        #permet de savoir le nombre de pdv du montre
        self.health = 100

        #sante maximum
        self.max_health = 100

        #nombre de pdv que chaque attacque du montre peut retirer au joueur
        self.attack = 5

        #permet d'affocher le montre
        self.image = pygame.image.load("assets/mummy.png")
        self.rect=self.image.get_rect()

        #pour positionner le monstre sur l'ecran
        self.rect.x = 1000
        self.rect.y = 540

        self.velocity = 0.55

    def update_health_bar(self,surface):
         #definir la couleur pour la jauge de vie (vert clair)
        bar_color = (111,210,46)

        #epaisseur et largeur de la jauge (bar)  de vie
        bar_position = [self.rect.x, self.rect.y, self.health, 5]

        #dessiner la bar de vie
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity

    #supprimer le monstre
    def remove(self):
        self.game.all_monsters.remove(self)