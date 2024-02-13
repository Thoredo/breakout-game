import pygame


class Bullet:
    def __init__(self, display, x_pos, y_pos):
        self.display = display
        self.x_pos = x_pos
        self.y_pos = y_pos
        pygame.draw.rect(
            self.display,
            "white",
            (self.x_pos, self.y_pos, 4, 4),
        )

    def move(self):
        self.y_pos -= 2
        pygame.draw.rect(
            self.display,
            "white",
            (self.x_pos, self.y_pos, 4, 6),
        )
