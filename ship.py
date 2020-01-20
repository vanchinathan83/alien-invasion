import pygame
import os
from pygame.sprite import Sprite

class Ship(Sprite):
    """ All the ship related actions and attributes"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load(self.get_image_path("ship.bmp"))
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed

    def center_ship(self):
        """ Center the ship after hit. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def get_image_path(self, image_name):
        return os.path.join(os.path.join(os.path.dirname(__file__), "images"), image_name)

    def blitme(self):
        self.screen.blit(self.image, self.rect)