import pygame


class GameScreen:
    def __init__(self, display, game_state_manager, paddle, ball, level, game_instance):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.paddle = paddle
        self.ball = ball
        self.level = level
        self.game_instance = game_instance
        self.scoreboard_font = pygame.font.SysFont("Arial", 20, bold=True)

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        self.paddle.draw_paddle()
        self.ball.draw_ball()
        self.level.draw()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        level_text = self.scoreboard_font.render(
            f"Level: {self.level.current_level}", True, "white"
        )
        self.display.blit(level_text, (300, 10))

        lives_text = self.scoreboard_font.render(
            f"Lives: {self.game_instance.player_lives}", True, "white"
        )
        self.display.blit(lives_text, (450, 10))

        score_text = self.scoreboard_font.render(
            f"Score: {self.game_instance.player_score}", True, "white"
        )
        self.display.blit(score_text, (600, 10))
