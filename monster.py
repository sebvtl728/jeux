import pygame 
import random
import animation

#création classe montre
class Monster(animation.AnimateSprite):
    
    def __init__(self, game):
        super().__init__('mummy')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        # self.image =pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)
        self.start_animation()
        
    def damage(self, amount):
        #infliger les degats
        if self.max_health - amount > amount:    
            self.health -= amount
        
        #Vérifier si les points de vie est égal a 0
        if self.health <= 0:
            #reaparaitre en nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            
            #verifier si la barre des commettes est bien charger !
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                
                #appel de la méthode de declanchement de comets
                self.game.comet_event.attemp_fall()
                
    def update_animation(self):
        self.animate(loop=True)
                
    def update_health_bar(self, surface):     
        #dessiner les bars de vie + couleurs + position
        pygame.draw.rect(surface, (240, 50, 9), [self.rect.x + 10, self.rect.y - 22, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 22, self.health, 5])
        
        
    def forward(self):
        #deplacement possible si pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Si le monstre entre en collision
        else:
             # infliger des degats (au joueur)
              self.game.player.damage(self.attack)