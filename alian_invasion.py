import sys
import os
import pygame
import pygame.sprite
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlianInvasion:
    """ Top Level class to maintain the game."""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.scoreboard = Scoreboard(self)
        self._create_fleet()
        # Make the button
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_position()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _create_fleet(self):
        """ Create the fleet of aliens. """

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that can fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (9 * alien_height) -
            ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """ Check whether any of the aliens have touched the edges. """
        for alien in self.aliens.sprites():
                if alien.check_edges():
                    self._change_fleet_direction()
                    break

    def _change_fleet_direction(self):
        """ Move the fleet down and change direction. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """ Update the position of the aliens."""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """ Check whether the aliens have reached the bottom. """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """ Respond to the ship hit by an alien. """
        if self.stats.ships_left > 0:
            # Redude the number of ships
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            # clear the aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # recreate the fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            sleep(1)
        else:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False

    def _update_bullets(self):
        """ Updates the position of the bullet"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ check collisions and recreate fleet if done. """
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for collision in collisions.values():
                self.stats.score += self.settings.alien_points
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # using the sprite draw function
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        self.scoreboard.show_score()
        pygame.display.flip()
      
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Check whether the mouse button was clicked. """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()
            self.settings.initialize_dynamic_settings()
            # remove any remaining aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet
            self._create_fleet()
            self.ship.center_ship()
            self.stats.game_active = True
            pygame.mouse.set_visible(False)

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