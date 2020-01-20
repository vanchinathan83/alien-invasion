import pygame.font


class Scoreboard:
    """ Scoreboard for the game. """

    def __init__(self, ai_game):
        """ Intialize scoreboard. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        level_str = "Level:" + str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_high_score(self):
        """ Turn the high score into a image. """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("High Score:" + high_score_str, True,
            self.text_color, self.settings.bg_color)

        # High score goes at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """ Turn the score into a image. """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score:" + score_str, True, self.text_color,
            self.settings.bg_color)

        # Display the score board
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def check_high_score(self):
        """ check for new high scores. """
        if self.stats.high_score < self.stats.score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """ Score display. """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
