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

#import bouton de lancement de jeux
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33 + 10)
play_button_rect.y = math.ceil(screen.get_height() / 2)


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
        screen.blit(play_button, play_button_rect)
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