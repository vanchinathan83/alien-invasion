import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ All the alien stuff resides here """
    
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load(ai_game.get_image_path('alien.bmp'))
        self.rect = self.image.get_rect()
        
        # starting the alien at the top right
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # store the horizontal position of alien
        self.x = float(self.rect.x)
        
