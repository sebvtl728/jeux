import pygame 
from player import Player
from comet_event import CometFallEvent
from monster import Monster
from monster import Mechant
from monster import SuperMechant

#création d'une classe pour representer le jeu
class Game:
    def __init__(self):
        # définir si le jeu a commancé
        self.is_playing = False
        
        # generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        
        #generer l'attaque des comets
        self.comet_event = CometFallEvent(self)
        
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
           
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mechant)
        self.spawn_monster(Mechant)
        self.spawn_monster(SuperMechant)
        
    def game_over(self):
        # reinitialisation du jeu pour une nouvelle partie
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        
        
    def update(self, screen):
        #appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
    
        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        
        #actualiser la barre d'attaque des comets
        self.comet_event.update_bar(screen)
        
        #actualisation de l'animation du joueur
        self.player.update_animation()
        
        #recuperation des projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
            
    
        # recuperation des monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
            
        #recuperation des commettes
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        #chargement des projectiles
        self.player.all_projectiles.draw(screen)
    
        #chargement des monstres
        self.all_monsters.draw(screen)
        
        #chargement des comettes
        self.comet_event.all_comets.draw(screen)
    
        # verifier si le joueur souhaite aller de gauche à droite 
        # print(game.pressed)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        
        #print(self.player.rect.x)
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self, mechant_class_name):
        self.all_monsters.add(mechant_class_name.__call__(self))