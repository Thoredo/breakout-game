import pygame
import constants

PLAYER_LIVES = constants.PLAYER_LIVES
PADDLE_STARTING_X = constants.PADDLE_STARTING_X
PADDLE_STARTING_Y = constants.PADDLE_STARTING_Y
BALL_START_X = constants.BALL_START_X
BALL_START_Y = constants.BALL_START_Y


class MainMenu:
    """
    Represents the main menu screen

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_state_manager (GameStateManager): Instance of GameStateManager class managing the current window state.
    game_instance (Game): Instance of the main Game class, allowing access to game state and components.
    menu_font (pygame.font.Font): The font used for rendering menu text.
    """

    def __init__(self, display, game_state_manager, game_instance):
        """
        Initializes the MainMenu class.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_state_manager (GameStateManager): Instance of GameStateManager class managing the current window state.
        game_instance (Game): Instance of the main Game class, allowing access to game state and components.
        """
        self.display = display
        self.gamestatemanager = game_state_manager
        self.game_instance = game_instance
        self.menu_font = pygame.font.SysFont("Arial", 30, bold=True)

        self.logo = pygame.image.load("images/logo.png")

    def run(self):
        """
        Fills the screen with a black background to overwrite previous elements,
        then calls the MainMenu.draw() method
        """
        self.display.fill("black")
        self.draw()

    def draw(self):
        """
        Creates the main menu components. Also handles user interaction with
        these buttons.
        """
        self.display.blit(self.logo, (273, 145))

        # Play Button
        pygame.draw.rect(self.display, "black", (490, 300, 100, 50))
        if (
            490 < self.game_instance.mouse[0] < 590
            and 300 < self.game_instance.mouse[1] < 350
        ):
            play_text = self.menu_font.render("Play", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.start_game()
        else:
            play_text = self.menu_font.render("Play", True, "white")
        self.display.blit(play_text, (515, 307))

        # Instructions button
        pygame.draw.rect(self.display, "black", (450, 360, 200, 50))
        if (
            450 < self.game_instance.mouse[0] < 650
            and 360 < self.game_instance.mouse[1] < 410
        ):
            instructions_text = self.menu_font.render("Instructions", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.open_instructions()
        else:
            instructions_text = self.menu_font.render("Instructions", True, "white")
        self.display.blit(instructions_text, (480, 366))

        # Quit Button
        pygame.draw.rect(self.display, "black", (490, 420, 100, 50))
        if (
            490 < self.game_instance.mouse[0] < 590
            and 420 < self.game_instance.mouse[1] < 470
        ):
            quit_text = self.menu_font.render("Quit", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.quit_game()
        else:
            quit_text = self.menu_font.render("Quit", True, "white")
        self.display.blit(quit_text, (515, 426))

    def open_instructions(self):
        """
        Sets the current game state to 'instructions' which causes the
        instructions page to open.
        """
        self.gamestatemanager.set_state("instructions")

    def quit_game(self):
        """
        Closes the game when the quit button in the menu gets clicked.
        """
        self.game_instance.is_running = False

    def start_game(self):
        """
        Sets the current game state to 'game' which causes the game to start.
        Also calls the method reset_game().
        """
        self.gamestatemanager.set_state("game")
        self.reset_game()

    def reset_game(self):
        """
        Resets all game elements when the play button gets pressed.
        """
        # Empty current bricks list
        self.game_instance.level.bricks = []

        # Reset stats
        self.game_instance.player_lives = PLAYER_LIVES
        self.game_instance.level.current_level = 1
        self.game_instance.player_score = 0

        # Create new bricks
        self.game_instance.level.create_bricks()

        # Move paddle back to center
        self.game_instance.paddle.x_pos = PADDLE_STARTING_X
        self.game_instance.paddle.y_pos = PADDLE_STARTING_Y

        # Move ball back to center
        self.game_instance.ball.x_pos = BALL_START_X
        self.game_instance.ball.y_pos = BALL_START_Y
