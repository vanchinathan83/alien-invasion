
class GameStats:
    """ Track stats of alien invasion. """

    def __init__(self, ai_game):
        """ Init stats. """
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """ Init the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
