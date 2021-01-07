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
       
       #verifier si le nombre de commettes est égale a 0
       if len(self.comet_event.all_comets) == 0:
           print('fin des comettes')
           
           #remettre la bar a zero
           self.comet_event.reset_percent()
           
           #retour des momies apres commettes
           self.comet_event.game.spawn_monster()
           self.comet_event.game.spawn_monster()
           self.comet_event.game.spawn_monster()
           
        
    def fall(self):
        self.rect.y += self.velocity
        
        #Les comettes ne tombes pas sur le sol
        if self.rect.y >=500:
            print('sol')
            #retirer la comette
            self.remove()
            
        #verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self,self.comet_event.game.all_players
        ):
            print('joueur touché !')
            
            #retirer la comette
            self.remove()
            
            #verifier si il n'y a plus de comettes dans le jeu
            if len(self.comet_event.all_comets) == 0:
                print('l\'evenement commette est terminer')
                
                #remettre la jauge de au maximum
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
            #impacter 20 points de degats au joueur
            self.comet_event.game.player.damage(20)