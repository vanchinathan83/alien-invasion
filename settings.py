
class Settings:
    """ Contains all the settings for the game."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 10
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (255, 0, 0)
        self.max_bullets_allowed = 5
        self.alien_speed = 3.0
        self.fleet_drop_speed = 100
        self.ship_limit = 1
        # fleet direction : right = 1 and left = -1
        self.fleet_direction = 1
