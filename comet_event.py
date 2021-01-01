import pygame

#création d'une classe pour l'evenement
class CometFallEvent:
    
    #lors du chargement -> créer un compteur
    def __init__(self):
        self.percent = 0
        
    def add_percent(self):
        self.percent += 1
        
    def upload_bar(self, surface):
        #barre noir en (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des x
            surface.get_height(), #axe Y
            surface.get_width(), #longueur de la fenetre
            
        ])
        #barre rouge (jauge)
        
        