import pygame
import constants

PADDLE_SPEED = constants.PADDLE_SPEED
PADDLE_STARTING_X = constants.PADDLE_STARTING_X
PADDLE_STARTING_Y = constants.PADDLE_STARTING_Y


class Paddle:
    def __init__(self, display):
        self.display = display
        self.width = 80
        self.height = 10
        self.x_pos = PADDLE_STARTING_X
        self.y_pos = PADDLE_STARTING_Y

    def draw_paddle(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + 10, self.height)
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
