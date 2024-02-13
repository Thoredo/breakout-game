import pygame


class Bullet:
    def __init__(self, display, x_pos, y_pos, game_instance):
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
        self.y_pos -= 2
        self.rect = pygame.Rect((self.x_pos, self.y_pos, 4, 4))
        pygame.draw.rect(
            self.display,
            "white",
            (self.x_pos, self.y_pos, 4, 6),
        )
        self.detect_collision()

    def detect_collision(self):
        for brick in self.game_instance.level.bricks:
            if self.rect.colliderect(brick):
                try:
                    self.game_instance.paddle.bullets.remove(self)
                    self.game_instance.ball.brick_collision(brick)
                except ValueError:
                    pass
