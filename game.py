import pygame
from player import Player

#creation de la classe (2e classe) Game
class Game():


    def __init__(self):
        #generer le joueur
        self.player = Player()
        self.pressed = {}