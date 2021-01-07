import pygame
from comet import Comet

#création d'une classe pour l'evenement
class CometFallEvent:
    
    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.game = game
        
        #définir un groupe sprite pour le stockage des cometes
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    def is_full_loaded(self):
        return self.percent >= 100
    
    def rese_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        #faire apparaitre la premiere comette
        self.all_comets.add(Comet(self))
    
    def attemp_fall(self):
        #la jauge des comets est completment chargé
        if self.is_full_loaded():
            print('Pluie de cometes !!')
            self.meteor_fall()
            self.rese_percent()
        
    def update_bar(self, surface):
        #ajouter du pourcentage à la bar
        self.add_percent()
        
        #appel de la méthode de declanchement de comets
        self.attemp_fall()
        
        #barre noir en (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des x
            surface.get_height() -20, #axe Y
            surface.get_width(), #longueur de la fenetre
            10 #épaisseur de la barre
        ])
        #barre rouge (jauge)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #axe des x
            surface.get_height() -20, #axe Y
            (surface.get_width() / 100) * self.percent, #longueur de la fenetre
            10 #épaisseur de la barre
        ])
        