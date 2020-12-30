import pygame
pygame.init()


#Generer la fenetr de notre jeu...
pygame.display.set_caption("forest Game")
screen = pygame.display.set_mode((1080, 720))

#Importation du Bg
background = pygame.image.load('assets/bg.jpg')

running = True

#boucle tant que cette condition est vrai

while running:
    screen.blit(background, (0,-200))
    pygame.display.flip()
    
    # si le jour ferme cette fenetre 
    for event in pygame.event.get():
        
        # que l'énenement est fermeture de fenetre
        if event.type == pygame.quit:
            running = False
            pygame.quit()
            print('fermeture du jeux')