import pygame

#création d'une classe pour l'evenement
class CometFallEvent:
    
    #lors du chargement -> créer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
    def update_bar(self, surface):
        
        #ajouter du pourcentage à la bar
        self.add_percent()
        
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
        