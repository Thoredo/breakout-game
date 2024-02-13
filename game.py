import pygame
import constants
from game_interface.game_state_manager import GameStateManager
from game_interface.instructions_page import InstructionsPage
from game_interface.game_screen import GameScreen
from game_interface.main_menu import MainMenu
from game_interface.game_over_screen import GameOverScreen
from game_elements.paddle import Paddle
from game_elements.ball import Ball
from game_elements.level import Level
from game_elements.boosts import BoostHandler

SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
FPS = constants.FPS
PLAYER_LIVES = constants.PLAYER_LIVES


class Game:
    """
    Handles the games GUI

    Attributes
    ----------
    screen(pygame.display): Creates the pygame window.
    clock(pygame.clock): Pygame clock used for controlling frame rate.
    is_running(bool): Used to see if the entire game / window is active.
    mouse(tuple): Used to see where in the screen the mouse is.
    mouse_clicked(tuple): Used to see the status of the 3 mouse buttons.
    player_lives(int): Keeps track of the number of lives the player has.
    player_score(int): Keeps track of the players score.
    current_level(int): Keeps track of what level the player is in.
    active_balls(list): List of active balls on screen
    game_state_manager(GameStateManager): Instance of GameStateManager class
                                        manages the current window of the game.
    main_menu(MainMenu): Instance for the main menu screen.
    instructions(Instructions): Instance for the instructions screen.
    game_over_screen(GameOverScreen): Instance for the game over screen.
    paddle(Paddle): Instance of the paddle object.
    level(Level): Instance of the level object.
    ball(Ball): Instance of the ball object.
    boost_handler(BoostHandler): Instance of the boost handler object.
    game_screen(GameScreen): Instance for the game screen.
    """

    def __init__(self):
        """
        Initializes the Game class.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.mouse = (0, 0)
        self.mouse_clicked = (False, False, False)
        self.player_lives = PLAYER_LIVES
        self.player_score = 0
        self.current_level = 1
        self.active_balls = []

        pygame.font.init()

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager, self)
        self.instructions = InstructionsPage(self.screen, self.game_state_manager, self)
        self.game_over_screen = GameOverScreen(
            self.screen, self.game_state_manager, self
        )
        self.paddle = Paddle(self.screen, self)
        self.level = Level(self.screen, self.current_level)
        self.ball = Ball(self.screen, self.paddle, self, self.level)
        self.active_balls.append(self.ball)
        self.boost_handler = BoostHandler(self.screen, self)
        self.game_screen = GameScreen(
            self.screen,
            self.game_state_manager,
            self.paddle,
            self.ball,
            self.level,
            self,
        )

        self.states = {
            "main menu": self.main_menu,
            "instructions": self.instructions,
            "game": self.game_screen,
            "game over": self.game_over_screen,
        }

    def run(self):
        """
        Contains while loop that runs all game mechanics.
        Calls handle_events and handle_key_presses.
        Calls the move method of each active balls.
        Calls run method of the currently active page.
        Gets the current mouse position.
        Gets status of what mouse buttons are clicked.
        """
        while self.is_running:
            self.handle_events()
            self.handle_key_presses()
            for ball in self.active_balls:
                ball.move()
            self.clock.tick(FPS)
            self.states[self.game_state_manager.get_state()].run()
            self.mouse = pygame.mouse.get_pos()
            self.mouse_clicked = pygame.mouse.get_pressed()
            pygame.display.update()

    def handle_events(self):
        """
        Closes the game when the player presses the close button.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def handle_key_presses(self):
        """
        Handles the keys the player presses.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
            if self.active_balls[0].on_paddle:
                self.active_balls[0].x_pos = self.paddle.x_pos + 40
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
            if self.active_balls[0].on_paddle:
                self.active_balls[0].x_pos = self.paddle.x_pos + 40
        if keys[pygame.K_UP]:
            self.active_balls[0].on_paddle = False
        if keys[pygame.K_SPACE]:
            self.paddle.shoot_gun()
