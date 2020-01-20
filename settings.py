
class Settings:
    """ Contains all the settings for the game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (255, 0, 0)
        self.max_bullets_allowed = 10
        self.fleet_drop_speed = 10
        self.ship_limit = 3

        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize the setting that can change. """
        self.ship_speed = 10
        self.bullet_speed = 10.0
        self.alien_speed = 5.0
        self.alien_points = 50

        # fleet direction : right = 1 and left = -1
        self.fleet_direction = 1

    def increase_speed(self):
        """ Increase speed settings. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)

