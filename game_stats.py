
class GameStats:
    """ Track stats of alien invasion. """

    def __init__(self, ai_game):
        """ Init stats. """
        self.settings = ai_game.settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """ Init the game. """
        self.ships_left = self.settings.ship_limit
