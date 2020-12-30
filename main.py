import pygame
import math
from games import Game
pygame.init()




#Generer la fenetr de notre jeu...
pygame.display.set_caption("forest Game")
screen = pygame.display.set_mode((1080, 720))

#Importation du Bg
background = pygame.image.load('assets/bg.jpg')

#importation baniere accueil
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner,(500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#chargement du jeu
game = Game()
running = True

#boucle tant que cette condition est vrai

while running:
    #appliquer la fenetre du jeu
    screen.blit(background, (0,-200))
    
    #verifier si le jeu à commencé ou non
    if game.is_playing:
        #declancher les instructions de la partie
        game.update(screen)
        
    #verifier si le jeu n'a pas commencé
    else:
        #add ecran de bienvenue
        screen.blit(banner, banner_rect)
      
    #mettre à jour l'écran
    pygame.display.flip()
    
    # si le jour ferme cette fenetre 
    for event in pygame.event.get():
        
        # que l'énenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.QUI()
            print('fermeture du jeux')
            
        #detection de mouvement du joueur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #detecter si la touche espace pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False