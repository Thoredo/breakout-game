import pygame
import constants

SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
BALL_SPEED_X = constants.BALL_SPEED_X
BALL_SPEED_Y = constants.BALL_SPEED_Y


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
