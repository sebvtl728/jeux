import pygame
from games import Game
pygame.init()




#Generer la fenetr de notre jeu...
pygame.display.set_caption("forest Game")
screen = pygame.display.set_mode((1080, 720))

#Importation du Bg
background = pygame.image.load('assets/bg.jpg')

#chargement du jeu
game = Game()
running = True

#boucle tant que cette condition est vrai

while running:
    #appliquer la fenetre du jeu
    screen.blit(background, (0,-200))
    
    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    
    # verifier si le joueur souhaite aller de gauche à droite 
    # print(game.pressed)
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
        
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    
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
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False