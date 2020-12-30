import pygame 
from player import Player

#création d'une classe pour representer le jeu
class Game:
    def __init__(self):
        # generer le joueur
        self.player = Player()
        self.pressed = {}
