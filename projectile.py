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
        self.origin_image = self.image
        self.angle = 0
        
        
    def rotate(self):
        #rotation du projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self) 
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        #vérification des colisions entre le projectiles et les monstres
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #suppression d'un projectile
            self.remove()
            
            #infliger des dégats
            monster.damage(self.player.attack)
        
        #verification de la presence des projectiles hors écran
        if self.rect.x > 1080: 
           self.remove()
        
            
        