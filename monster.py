import pygame 

#création classe montre
class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image =pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2
        
    def update_health_bar(self, surface):
        #couleur jauge de vie
        bar_color = (111, 210,46)
        
        #couleur jauge arriere
        back_bar_color = (240, 50, 9)
            
        #position jauge + largeur et epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 22, self.health, 5]
        
        #definir la position de la jauge arriere 
        back_bar_position = [self.rect.x + 10, self.rect.y - 22, self.max_health, 5]
        
        #dessiner la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
        
    def forward(self):
        #deplacement possible si pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity