import pygame
import random


#creation classe de comete

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        #definir l'image de la commette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        
    def remove(self):
       self.comet_event.all_comets.remove(self) 
        
    def fall(self):
        self.rect.y += self.velocity
        
        #Les comettes ne tombes pas sur le sol
        if self.rect.y >=500:
            print('sol')
            #retirer la comette
            self.remove()