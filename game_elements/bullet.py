import pygame


class Bullet:
    """
    Represents a bullet object in the game.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    x_pos (int): The x-coordinate of the bullet.
    y_pos (int): The y-coordinate of the bullet.
    game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
    rect (pygame.Rect): The rectangular area occupied by the bullet.
    """

    def __init__(self, display, x_pos, y_pos, game_instance):
        """
        Initializes the Bullet object.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        x_pos (int): The x-coordinate of the bullet.
        y_pos (int): The y-coordinate of the bullet.
        game_instance (Game): Instance of the main Game class, allowing access
                        to game state and components.
        """
        self.display = display
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.game_instance = game_instance
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 4, 4))
        pygame.draw.rect(
            self.display,
            "white",
            (self.x_pos, self.y_pos, 4, 4),
        )

    def move(self):
        """
        Moves the bullet upwards and checks for collisions.
        """
        self.y_pos -= 2
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 4, 4))
        pygame.draw.rect(
            self.display,
            "white",
            (self.x_pos, self.y_pos, 4, 6),
        )
        self.detect_collision()

    def detect_collision(self):
        """
        Detects collision between the bullet and bricks.
        """
        for brick in self.game_instance.level.bricks:
            if self.rect.colliderect(brick):
                try:
                    self.game_instance.paddle.bullets.remove(self)
                    self.game_instance.ball.brick_collision(brick)
                except ValueError:
                    pass
