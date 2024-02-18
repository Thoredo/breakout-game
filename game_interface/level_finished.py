import pygame
import constants

BALL_START_Y = constants.BALL_START_Y


class LevelFinishedScreen:
    """
    Represents level finished screen.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_state_manager (GameStateManager): Instance of GameStateManager class
                    managing the current window state.
    game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
    level_done_font (pygame.font.Font): The font used for the level done text.
    stats_font (pygame.font.Font): The font used for the stats on screen.
    next_level_font (pygame.font.Font): The font used for the next level button.
    """

    def __init__(self, display, game_state_manager, game_instance):
        """
        Initializes the GameOverClass class.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_state_manager (GameStateManager): Instance of GameStateManager class
                    managing the current window state.
        game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
        """
        self.display = display
        self.game_state_manager = game_state_manager
        self.game_instance = game_instance
        self.level_done_font = pygame.font.SysFont("Arial", 90, bold=True)
        self.stats_font = pygame.font.SysFont("Arial", 30, bold=True)
        self.next_level_font = pygame.font.SysFont("Arial", 30, bold=True)

    def run(self):
        """
        Fills the screen with a black background to overwrite previous elements,
        then calls the LevelFinishedScreen.draw() method
        """
        self.display.fill("black")
        self.draw()

    def draw(self):
        """
        Creates the game over screen components
        """
        level_done_text = self.level_done_font.render("Level Done", True, "white")
        self.display.blit(level_done_text, (340, 200))

        final_level_text = self.stats_font.render(
            f"Level: {self.game_instance.level.current_level}", True, "white"
        )
        self.display.blit(final_level_text, (500, 370))

        final_score_text = self.stats_font.render(
            f"Score: {self.game_instance.player_score}", True, "white"
        )
        self.display.blit(final_score_text, (500, 420))

        pygame.draw.rect(self.display, "black", (470, 640, 120, 50))
        if (
            470 < self.game_instance.mouse[0] < 610
            and 640 < self.game_instance.mouse[1] < 710
        ):
            next_level_text = self.next_level_font.render("Next Level", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.start_next_level()
        else:
            next_level_text = self.next_level_font.render("Next Level", True, "white")
        self.display.blit(next_level_text, (500, 647))

    def start_next_level(self):
        """
        Starts the next levels.
        """

        # Create new level bricks
        self.game_instance.level.bricks = []
        self.game_instance.level.current_level += 1
        self.game_instance.level.create_bricks()

        # Reset ball location and direction
        self.game_instance.ball.back_on_paddle()
        self.game_instance.ball.reset_direction()

        # Remove active boosts and those on screen
        self.game_instance.boost_handler.remove_on_screen_boosts()
        self.game_instance.boost_handler.stop_active_boosts()

        self.game_instance.paddle.remove_bullets()

        # Remove extra balls from game
        for ball in self.game_instance.active_balls[1:]:
            self.game_instance.active_balls.remove(ball)

        self.game_state_manager.set_state("game")
