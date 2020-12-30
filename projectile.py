import pygame

# classe du projectille
class Projectile(pygame.sprite.Sprite):
    
    #définir le constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        
    def remove(self):
        self.player.all_projectiles.remove(self) 
        
    def move(self):
        self.rect.x += self.velocity
        
        #verification de la presence des projectiles
        if self.rect.x > 1080: 
           self.remove()
        
            
        