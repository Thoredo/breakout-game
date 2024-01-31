import pygame
import sys

WIDTH, HEIGHT = 1080, 720
FPS = 60
PADDLE_SPEED = 3


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.mouse = (0, 0)
        self.mouse_clicked = (False, False, False)

        pygame.font.init()

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.instructions = InstructionsPage(self.screen, self.game_state_manager)
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
                self.ball.start_position = self.paddle.x_pos + 40
        if keys[pygame.K_RIGHT]:
            self.paddle.move_right()
            if self.ball.on_paddle:
                self.ball.start_position = self.paddle.x_pos + 40


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


class InstructionsPage:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.instruction_headers = pygame.font.SysFont("Arial", 30, bold=True)
        self.instruction_small_text = pygame.font.SysFont("Arial", 22, bold=True)

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        # Boost legend
        # ------------------------------------------------------------------#
        boost_legend_header = self.instruction_headers.render(
            "Boost Legend", True, "white"
        )
        self.display.blit(boost_legend_header, (30, 30))

        # Enlarge Paddle
        # ------------------------------------------------------------------#
        enlarge_paddle = pygame.image.load("images/enlarge_paddle.png")
        self.display.blit(enlarge_paddle, (30, 80))
        enlarge_text = self.instruction_small_text.render(
            "Makes paddle bigger", True, "white"
        )
        self.display.blit(enlarge_text, (100, 90))

        # Shrink Paddle
        # ------------------------------------------------------------------#
        shrink_paddle = pygame.image.load("images/shrink_paddle.png")
        self.display.blit(shrink_paddle, (30, 130))
        shrink_text = self.instruction_small_text.render(
            "Makes paddle smaller", True, "white"
        )
        self.display.blit(shrink_text, (100, 140))

        # Add Live
        # ------------------------------------------------------------------#
        add_live = pygame.image.load("images/add_live.png")
        self.display.blit(add_live, (30, 180))
        add_live_text = self.instruction_small_text.render(
            "Gives the player an extra live", True, "white"
        )
        self.display.blit(add_live_text, (100, 190))

        # Add Ball
        # ------------------------------------------------------------------#
        add_ball = pygame.image.load("images/add_ball.png")
        self.display.blit(add_ball, (30, 230))
        add_ball_text = self.instruction_small_text.render(
            "Adds another active ball, 3 max", True, "white"
        )
        self.display.blit(add_ball_text, (100, 240))

        # Speed Up Ball
        # ------------------------------------------------------------------#
        speed_up_ball = pygame.image.load("images/speed_up_ball.png")
        self.display.blit(speed_up_ball, (530, 80))
        speed_up_text = self.instruction_small_text.render(
            "Makes the ball go faster", True, "white"
        )
        self.display.blit(speed_up_text, (600, 90))

        # Slow Up Ball
        # ------------------------------------------------------------------#
        slow_down_ball = pygame.image.load("images/slow_down_ball.png")
        self.display.blit(slow_down_ball, (530, 130))
        slow_down_text = self.instruction_small_text.render(
            "Makes the ball go slower", True, "white"
        )
        self.display.blit(slow_down_text, (600, 140))

        # Increase points gained
        # ------------------------------------------------------------------#
        increase_points_gained = pygame.image.load("images/increase_points_gained.png")
        self.display.blit(increase_points_gained, (530, 180))
        increase_points_text = self.instruction_small_text.render(
            "Increases points earned by 1.5", True, "white"
        )
        self.display.blit(increase_points_text, (600, 190))

        # Let Paddle Shoot
        # ------------------------------------------------------------------#
        paddle_shooting = pygame.image.load("images/paddle_shoot.png")
        self.display.blit(paddle_shooting, (530, 230))
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
        left_arrow = pygame.image.load("images/left_arrow.png")
        self.display.blit(left_arrow, (30, 400))
        left_arrow_text = self.instruction_small_text.render(
            "Moves paddle to the left", True, "white"
        )
        self.display.blit(left_arrow_text, (100, 410))

        # Move Right
        # ------------------------------------------------------------------#
        right_arrow = pygame.image.load("images/right_arrow.png")
        self.display.blit(right_arrow, (30, 450))
        right_arrow_text = self.instruction_small_text.render(
            "Moves paddle to the right", True, "white"
        )
        self.display.blit(right_arrow_text, (100, 460))

        # Release Ball Off Paddle
        # ------------------------------------------------------------------#
        up_arrow = pygame.image.load("images/up_arrow.png")
        self.display.blit(up_arrow, (600, 400))
        up_arrow_text = self.instruction_small_text.render(
            "Releases the ball from the paddle", True, "white"
        )
        self.display.blit(up_arrow_text, (670, 410))

        # Shoot
        # ------------------------------------------------------------------#
        space_bar = pygame.image.load("images/space_bar.png")
        self.display.blit(space_bar, (570, 450))
        space_bar_text = self.instruction_small_text.render(
            "Lets the paddle shoot upwards", True, "white"
        )
        self.display.blit(space_bar_text, (670, 460))

        # Back Button
        # ------------------------------------------------------------------#
        pygame.draw.rect(self.display, "black", (450, 640, 120, 50))
        if 450 < game_instance.mouse[0] < 650 and 640 < game_instance.mouse[1] < 710:
            instructions_text = self.instruction_headers.render("Back", True, "red")
            if game_instance.mouse_clicked[0] == True:
                self.open_main_menu()
        else:
            instructions_text = self.instruction_headers.render("Back", True, "white")
        self.display.blit(instructions_text, (480, 647))

    def open_main_menu(self):
        self.gamestatemanager.set_state("main menu")


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
        self.start_position = 540
        self.on_paddle = True
        self.x_pos = 540
        self.y_pos = 665

    def draw_ball(self):
        if self.on_paddle:
            pygame.draw.circle(
                self.display, "green", (self.start_position, self.y_pos), 10
            )
        else:
            pygame.draw.circle(self.display, "green", (self.x_pos, self.y_pos), 10)


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
    pygame.quit()
    sys.exit()
