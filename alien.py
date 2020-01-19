import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ All the alien stuff resides here """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load(ai_game.get_image_path('alien.bmp'))
        self.rect = self.image.get_rect()

        # starting the alien at the top right
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the horizontal position of alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Returns True if the alien touches the edges. """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ Move the alien. """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
