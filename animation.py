import pygame

#classe qui gere les animations
class AnimateSprite(pygame.sprite.Sprite):
    #definir les evenements à la création des entités
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False
    
    #methode de demargage d'animation
    def start_animation(self):
        self.animation = True
            
    #definir une methode pour animer le sprite
    def animate(self, loop=False):
        
        #verification si l'animation est active
        if self.animation:
        
            #passer à l'image suivante
            self.current_image += 1
            
            #verifier la fin de l'animation
            if self.current_image >= len(self.images):
                
                #revenir au debut de l'animation
                self.current_image = 0
                
                #verification si animation n'est pas en mode boocle
                if loop is False:
                    
                    #desactivation de l'animation
                    self.animation = False
                
            #modification de l'image précedente par la suivante
            self.image = self.images[self.current_image]
        

#definir une fonction pour charger les images sprite
def load_animation_images(sprite_name):
    #chargement de l'animation
    images = []
    
    #chemin du dossier
    path = (f"assets/{sprite_name}/{sprite_name}")
    
    #boucle sur les images
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        
    #renvoyer le contenu des images    
    return images


#definir un dictionnaire qui va contenir les images chargées de chaques sprites
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}