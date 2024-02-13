import pygame


class Brick:
    """
    Represents a brick object in the game.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    difficulty (int): The difficulty level of the brick.
    width (int): The width of the brick.
    height (int): The height of the brick.
    x_pos (int): The x-coordinate of the top-left corner of the brick.
    y_pos (int): The y-coordinate of the top-left corner of the brick.
    health (int): The health points of the brick based on the difficulty.
    rect (pygame.Rect): The rectangular area occupied by the brick.
    colors (list): List of colors for different difficulty levels.
    """

    def __init__(self, display, difficulty, x_pos, y_pos):
        """
        Initializes the Brick object.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        difficulty (int): The difficulty level of the brick.
        x_pos (int): The x-coordinate of the top-left corner of the brick.
        y_pos (int): The y-coordinate of the top-left corner of the brick.
        """
        self.display = display
        self.difficulty = difficulty
        self.width = 60
        self.height = 20
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = self.difficulty
        self.rect = pygame.Rect(
            self.x_pos, self.y_pos, self.width + 10, self.height + 10
        )
        # fmt: off
        self.colors = ["blue", "red", "green", "purple", "yellow", "pink", 
                       "orange", "cyan", "magenta", "lime", "turquoise", 
                       "maroon", "teal", "gold", "silver"]
        # fmt: on

    def draw(self):
        """
        Draws the brick on the game window based on its difficulty level.
        """
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
