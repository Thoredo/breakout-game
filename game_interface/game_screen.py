import pygame


class GameScreen:
    """
    Represents the game screen

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_state_manager (GameStateManager): Instance of GameStateManager class
                    managing the current window state.
    game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
    paddle(Paddle): Instance of the paddle object.
    level(Level): Instance of the level object.
    ball(Ball): Instance of the ball object.
    scoreboard_font (pygame.font.Font): The font used for the scoreboard text.
    """

    def __init__(self, display, game_state_manager, paddle, ball, level, game_instance):
        """
        Initializes the GameScreen class.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_state_manager (GameStateManager): Instance of GameStateManager class managing the current window state.
        game_instance (Game): Instance of the main Game class, allowing access to game state and components.
        paddle(Paddle): Instance of the paddle object.
        level(Level): Instance of the level object.
        ball(Ball): Instance of the ball object.
        """
        self.display = display
        self.game_state_manager = game_state_manager
        self.game_instance = game_instance
        self.paddle = paddle
        self.ball = ball
        self.level = level
        self.scoreboard_font = pygame.font.SysFont("Arial", 20, bold=True)

    def run(self):
        """
        Fills the screen with a black background to overwrite previous elements,
        then calls the GameScreen.draw() method
        """
        self.display.fill("black")
        self.draw()

    def draw(self):
        """
        Draws the following components onto the screen:
        - paddle
        - all active balls
        - the bricks belonging to the level
        - any active boosts

        Also calls game_over_check()
        """
        self.paddle.draw_paddle()
        for ball in self.game_instance.active_balls:
            ball.draw_ball()
        self.level.draw()
        self.draw_scoreboard()
        self.game_over_check()
        self.game_instance.boost_handler.draw()

    def draw_scoreboard(self):
        """
        Draws all scoreboard components.
        """
        level_text = self.scoreboard_font.render(
            f"Level: {self.game_instance.level.current_level}", True, "white"
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

    def game_over_check(self):
        """
        Sets the game state to game over once the player is out of lives.
        """
        if self.game_instance.player_lives == 0:
            self.game_state_manager.set_state("game over")
