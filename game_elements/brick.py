import pygame


class Brick:
    def __init__(self, display, difficulty, x_pos, y_pos):
        self.display = display
        self.difficulty = difficulty
        self.width = 60
        self.height = 20
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = pygame.Rect(
            self.x_pos, self.y_pos, self.width + 10, self.height + 10
        )

    def draw(self):
        pygame.draw.rect(
            self.display,
            "blue",
            (self.x_pos, self.y_pos, self.width, self.height),
        )
