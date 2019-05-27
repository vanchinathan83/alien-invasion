
class Settings:
    """ Contains all the settings for the game."""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 10
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.max_bullets_allowed = 3
        
        