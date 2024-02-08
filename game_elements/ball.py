import pygame
import constants

SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
BALL_SPEED_X = constants.BALL_SPEED_X
BALL_SPEED_Y = constants.BALL_SPEED_Y
BALL_START_X = constants.BALL_START_X
BALL_START_Y = constants.BALL_START_Y


class Ball:
    def __init__(self, display, paddle, game_instance, level):
        self.display = display
        self.paddle = paddle
        self.game_instace = game_instance
        self.level = level

        self.ball_radius = 10
        self.on_paddle = True
        self.x_pos = BALL_START_X
        self.y_pos = BALL_START_Y
        self.x_speed = BALL_SPEED_X
        self.y_speed = BALL_SPEED_Y

    def draw_ball(self):
        pygame.draw.circle(
            self.display,
            "green",
            (self.x_pos, self.y_pos),
            self.ball_radius,
        )

        self.rect = pygame.Rect(
            self.x_pos, self.y_pos, self.ball_radius, self.ball_radius
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
                self.handle_missed_ball()

            # Detect collision with paddle
            if self.rect.colliderect(self.paddle):
                # Check if colliding from top of paddle
                if (
                    abs(self.rect.bottom - self.paddle.rect.top) < collision_treshold
                    and self.y_speed > 0
                ):
                    self.y_speed *= -1

            # Detect collision with blocks
            for brick in self.level.bricks:
                if self.rect.colliderect(brick.rect):
                    if (
                        abs(self.rect.left - brick.rect.right) < collision_treshold
                        and self.x_speed < 0
                    ):
                        self.x_speed *= -1
                        self.remove_brick(brick)
                    if (
                        abs(self.rect.right - brick.rect.left) < collision_treshold
                        and self.x_speed > 0
                    ):
                        self.x_speed *= -1
                        self.remove_brick(brick)
                    if (
                        abs((self.rect.top) - brick.rect.bottom) < collision_treshold
                        and self.y_speed < 0
                    ):
                        self.y_speed *= -1
                        self.remove_brick(brick)
                    if (
                        abs(self.rect.bottom - brick.rect.top) < collision_treshold
                        and self.y_speed > 0
                    ):
                        self.y_speed *= -1
                        self.remove_brick(brick)

            # Move the ball
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed

    def handle_missed_ball(self):
        self.game_instace.player_lives -= 1

        self.on_paddle = True
        self.x_pos = self.paddle.x_pos + 40
        self.y_pos = BALL_START_Y

    def remove_brick(self, brick):
        brick.width = 0
        brick.height = 0
        brick.rect.width = 0
        brick.rect.height = 0
        self.level.update_bricks(self.level.bricks)
