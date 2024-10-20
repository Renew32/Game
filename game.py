import pygame
from player import Player
from monster import Monster 

#creation de la classe (2e classe) Game
class Game():


    def __init__(self):
        #generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #sert a gerer l'ensemb;e des monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    # permet definir les colision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
    

    def spawn_monster(self):

        monster = Monster(self)

        #ajoute des montres a all_monsters
        self.all_monsters.add(monster)