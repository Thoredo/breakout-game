import pygame
import constants
from game_interface.game_state_manager import GameStateManager
from game_interface.instructions_page import InstructionsPage
from game_interface.game_screen import GameScreen
from game_interface.main_menu import MainMenu
from game_elements.paddle import Paddle
from game_elements.ball import Ball
from game_elements.level import Level


SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
FPS = constants.FPS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.mouse = (0, 0)
        self.mouse_clicked = (False, False, False)

        pygame.font.init()

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager, self)
        self.instructions = InstructionsPage(self.screen, self.game_state_manager, self)
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.screen, self.paddle)
        self.level = Level(1)
        self.game_screen = GameScreen(
            self.screen, self.game_state_manager, self.paddle, self.ball
        )

        self.states = {
            "main menu": self.main_menu,
            "instructions": self.instructions,
            "game": self.game_screen,
        }

    def run(self):
        while self.is_running:
            self.handle_events()
            self.handle_key_presses()
            self.ball.move()
            self.clock.tick(FPS)
            self.states[self.game_state_manager.get_state()].run()
            self.mouse = pygame.mouse.get_pos()
            self.mouse_clicked = pygame.mouse.get_pressed()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def handle_key_presses(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.move_left()
            if self.ball.on_paddle:
                self.ball.x_pos = self.paddle.x_pos + 40
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
            if self.ball.on_paddle:
                self.ball.x_pos = self.paddle.x_pos + 40
        if keys[pygame.K_UP]:
            self.ball.on_paddle = False
