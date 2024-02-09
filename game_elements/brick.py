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
        # fmt: off
        self.colors = ["blue", "red", "green", "purple", "yellow", "pink", 
                       "orange", "cyan", "magenta", "lime", "turquoise", 
                       "maroon", "teal", "gold", "silver"]
        # fmt: on

    def draw(self):
        if self.difficulty < len(self.colors):
            pygame.draw.rect(
                self.display,
                self.colors[self.difficulty - 1],
                (self.x_pos, self.y_pos, self.width, self.height),
            )
        else:
            self.difficulty = self.difficulty % len(self.colors)
            pygame.draw.rect(
                self.display,
                self.colors[self.difficulty - 1],
                (self.x_pos, self.y_pos, self.width, self.height),
            )
