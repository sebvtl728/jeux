import pygame
pygame.init()

#création d'une classe pour representer le jeu
class Game:
    def __init__(self):
        # generer le joueur
        self.player = Player()

#création d'une classe pour representer le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

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
    
    #mettre à jour l'écran
    pygame.display.flip()
    
    # si le jour ferme cette fenetre 
    for event in pygame.event.get():
        
        # que l'énenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.QUI()
            print('fermeture du jeux')