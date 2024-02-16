import pygame


class InstructionsPage:
    """
    Represents the instructions screen

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_state_manager (GameStateManager): Instance of GameStateManager class
                                        managing the current window state.
    game_instance (Game): Instance of the main Game class, allowing access to
                                        game state and components.
    instruction_headers (pygame.font.Font): The font used for the headers on
                                        the instructions page.
    instruction_small_text (pygame.font.Font): The font used for the small text
                                        on the instructions page.
    """

    def __init__(self, display, game_state_manager, game_instance):
        """
        Initializes the InstructionsPage class.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_state_manager (GameStateManager): Instance of GameStateManager class managing the current window state.
        game_instance (Game): Instance of the main Game class, allowing access to game state and components.
        """
        self.display = display
        self.game_state_manager = game_state_manager
        self.game_instance = game_instance
        self.instruction_headers = pygame.font.SysFont("Arial", 30, bold=True)
        self.instruction_small_text = pygame.font.SysFont("Arial", 22, bold=True)

        # Load images
        # Boost images
        self.enlarge_paddle = pygame.image.load("images/enlarge_paddle.png")
        self.shrink_paddle = pygame.image.load("images/shrink_paddle.png")
        self.add_live = pygame.image.load("images/add_life.png")
        self.add_ball = pygame.image.load("images/add_ball.png")
        self.speed_up_ball = pygame.image.load("images/speed_up_ball.png")
        self.slow_down_ball = pygame.image.load("images/slow_down_ball.png")
        self.increase_points_gained = pygame.image.load(
            "images/increase_points_gained.png"
        )
        self.paddle_shooting = pygame.image.load("images/paddle_shoot.png")

        # Control images
        self.left_arrow = pygame.image.load("images/left_arrow.png")
        self.right_arrow = pygame.image.load("images/right_arrow.png")
        self.up_arrow = pygame.image.load("images/up_arrow.png")
        self.space_bar = pygame.image.load("images/space_bar.png")

    def run(self):
        """
        Fills the screen with a black background to overwrite previous elements,
        then calls the InstructionsPage.draw() method
        """
        self.display.fill("black")
        self.draw()

    def draw(self):
        """
        Creates the instruction page components.
        """
        # Boost legend
        # ------------------------------------------------------------------#
        boost_legend_header = self.instruction_headers.render(
            "Boost Legend", True, "white"
        )
        self.display.blit(boost_legend_header, (30, 30))

        # Enlarge Paddle
        # ------------------------------------------------------------------#
        self.display.blit(self.enlarge_paddle, (30, 80))
        enlarge_text = self.instruction_small_text.render(
            "Makes paddle bigger", True, "white"
        )
        self.display.blit(enlarge_text, (100, 90))

        # Shrink Paddle
        # ------------------------------------------------------------------#
        self.display.blit(self.shrink_paddle, (30, 130))
        shrink_text = self.instruction_small_text.render(
            "Makes paddle smaller", True, "white"
        )
        self.display.blit(shrink_text, (100, 140))

        # Add Live
        # ------------------------------------------------------------------#
        self.display.blit(self.add_live, (30, 180))
        add_live_text = self.instruction_small_text.render(
            "Gives the player an extra live", True, "white"
        )
        self.display.blit(add_live_text, (100, 190))

        # Add Ball
        # ------------------------------------------------------------------#
        self.display.blit(self.add_ball, (30, 230))
        add_ball_text = self.instruction_small_text.render(
            "Adds another active ball, 3 max", True, "white"
        )
        self.display.blit(add_ball_text, (100, 240))

        # Speed Up Ball
        # ------------------------------------------------------------------#
        self.display.blit(self.speed_up_ball, (530, 80))
        speed_up_text = self.instruction_small_text.render(
            "Makes the ball go faster", True, "white"
        )
        self.display.blit(speed_up_text, (600, 90))

        # Slow Up Ball
        # ------------------------------------------------------------------#
        self.display.blit(self.slow_down_ball, (530, 130))
        slow_down_text = self.instruction_small_text.render(
            "Makes the ball go slower", True, "white"
        )
        self.display.blit(slow_down_text, (600, 140))

        # Increase points gained
        # ------------------------------------------------------------------#
        self.display.blit(self.increase_points_gained, (530, 180))
        increase_points_text = self.instruction_small_text.render(
            "Increases points earned by 1.5", True, "white"
        )
        self.display.blit(increase_points_text, (600, 190))

        # Let Paddle Shoot
        # ------------------------------------------------------------------#
        self.display.blit(self.paddle_shooting, (530, 230))
        paddle_shooting_text = self.instruction_small_text.render(
            "Lets the paddle shoot upward", True, "white"
        )
        self.display.blit(paddle_shooting_text, (600, 240))

        # Controls
        # ------------------------------------------------------------------#
        controls_header = self.instruction_headers.render("Controls", True, "white")
        self.display.blit(controls_header, (30, 350))

        # Move Left
        # ------------------------------------------------------------------#
        self.display.blit(self.left_arrow, (30, 400))
        left_arrow_text = self.instruction_small_text.render(
            "Moves paddle to the left", True, "white"
        )
        self.display.blit(left_arrow_text, (100, 410))

        # Move Right
        # ------------------------------------------------------------------#
        self.display.blit(self.right_arrow, (30, 450))
        right_arrow_text = self.instruction_small_text.render(
            "Moves paddle to the right", True, "white"
        )
        self.display.blit(right_arrow_text, (100, 460))

        # Release Ball Off Paddle
        # ------------------------------------------------------------------#
        self.display.blit(self.up_arrow, (600, 400))
        up_arrow_text = self.instruction_small_text.render(
            "Releases the ball from the paddle", True, "white"
        )
        self.display.blit(up_arrow_text, (670, 410))

        # Shoot
        # ------------------------------------------------------------------#
        self.display.blit(self.space_bar, (570, 450))
        space_bar_text = self.instruction_small_text.render(
            "Lets the paddle shoot upwards", True, "white"
        )
        self.display.blit(space_bar_text, (670, 460))

        # Back Button
        # ------------------------------------------------------------------#
        pygame.draw.rect(self.display, "black", (450, 640, 120, 50))
        if (
            450 < self.game_instance.mouse[0] < 650
            and 640 < self.game_instance.mouse[1] < 710
        ):
            back_button_text = self.instruction_headers.render("Back", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.open_main_menu()
        else:
            back_button_text = self.instruction_headers.render("Back", True, "white")
        self.display.blit(back_button_text, (480, 647))

    def open_main_menu(self):
        """
        Sets the current game state to 'main menu' which causes the
        main menu to open.
        """
        self.game_state_manager.set_state("main menu")
