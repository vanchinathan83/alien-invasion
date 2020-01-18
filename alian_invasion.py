import sys
import os
import pygame
import pygame.sprite

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlianInvasion:
    """ Top Level class to maintain the game."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_bullets()
            self._update_screen()
            
            
    def _update_bullets(self):
        """ Updates the position of the bullet"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
            
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
                        
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.max_bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def get_image_path(self, image_name):
        return os.path.join(os.path.join(os.path.dirname(__file__), "images"), image_name)
            
if __name__ == '__main__':
    ai = AlianInvasion()
    ai.run_game()