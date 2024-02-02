import pygame
import sys
from game_interface.game_state_manager import GameStateManager
from game_interface.instructions_page import InstructionsPage

SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
FPS = 60
PADDLE_SPEED = 4
BALL_SPEED_X = 4
BALL_SPEED_Y = -4


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
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.instructions = InstructionsPage(self.screen, self.game_state_manager, self)
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.screen, self.paddle)
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


class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.menu_font = pygame.font.SysFont("Arial", 30, bold=True)

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        logo = pygame.image.load("images/logo.png")
        self.display.blit(logo, (273, 145))

        # Play Button
        pygame.draw.rect(self.display, "black", (490, 300, 100, 50))
        if 490 < game_instance.mouse[0] < 590 and 300 < game_instance.mouse[1] < 350:
            play_text = self.menu_font.render("Play", True, "red")
            if game_instance.mouse_clicked[0] == True:
                self.start_game()
        else:
            play_text = self.menu_font.render("Play", True, "white")
        self.display.blit(play_text, (515, 307))

        # Instructions button
        pygame.draw.rect(self.display, "black", (450, 360, 200, 50))
        if 450 < game_instance.mouse[0] < 650 and 360 < game_instance.mouse[1] < 410:
            instructions_text = self.menu_font.render("Instructions", True, "red")
            if game_instance.mouse_clicked[0] == True:
                self.open_instructions()
        else:
            instructions_text = self.menu_font.render("Instructions", True, "white")
        self.display.blit(instructions_text, (480, 366))

        # Quit Button
        pygame.draw.rect(self.display, "black", (490, 420, 100, 50))
        if 490 < game_instance.mouse[0] < 590 and 420 < game_instance.mouse[1] < 470:
            quit_text = self.menu_font.render("Quit", True, "red")
            if game_instance.mouse_clicked[0] == True:
                self.quit_game()
        else:
            quit_text = self.menu_font.render("Quit", True, "white")
        self.display.blit(quit_text, (515, 426))

    def open_instructions(self):
        self.gamestatemanager.set_state("instructions")

    def quit_game(self):
        game_instance.is_running = False

    def start_game(self):
        self.gamestatemanager.set_state("game")


class GameScreen:
    def __init__(self, display, game_state_manager, paddle, ball):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.paddle = paddle
        self.ball = ball

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        self.paddle.draw_paddle()
        self.ball.draw_ball()


class Paddle:
    def __init__(self, display):
        self.display = display
        self.width = 80
        self.height = 10
        self.x_pos = 500
        self.y_pos = 680

    def draw_paddle(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pygame.draw.rect(
            self.display,
            "yellow",
            (self.x_pos, self.y_pos, self.width, self.height),
        )

    def move_left(self):
        if self.x_pos > 0:
            self.x_pos -= PADDLE_SPEED

    def move_right(self):
        if self.x_pos < 1000:
            self.x_pos += PADDLE_SPEED


class Ball:
    def __init__(self, display, paddle):
        self.display = display
        self.paddle = paddle

        self.ball_radius = 10
        self.on_paddle = True
        self.x_pos = 540
        self.y_pos = 670
        self.x_speed = BALL_SPEED_X
        self.y_speed = BALL_SPEED_Y

    def draw_ball(self):
        self.rect = pygame.Rect(
            self.x_pos, self.y_pos, self.ball_radius, self.ball_radius
        )

        pygame.draw.circle(
            self.display,
            "green",
            (self.x_pos, self.y_pos),
            self.ball_radius,
        )

    def move(self):
        collision_treshold = 5

        if self.on_paddle == False:
            # Check for collision with walls
            if self.rect.left < self.ball_radius or self.rect.right > SCREEN_WIDTH:
                self.x_speed *= -1

            # Check for collision with top of screen
            if self.rect.top < self.ball_radius:
                self.y_speed *= -1

            # Check for collision with bottom of screen
            if self.rect.bottom > SCREEN_HEIGHT:
                print("game over")

            # Detect collision with paddle
            if self.rect.colliderect(self.paddle):
                # Check if colliding from top of paddle
                if (
                    abs(self.rect.bottom - self.paddle.rect.top) < collision_treshold
                    and self.y_speed > 0
                ):
                    self.y_speed *= -1

            # Move the ball
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed


if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
    pygame.quit()
    sys.exit()
