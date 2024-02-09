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
        self.game_instance = game_instance
        self.level = level

        self.ball_radius = 10
        self.on_paddle = True
        self.x_pos = BALL_START_X
        self.y_pos = BALL_START_Y
        self.x_speed = BALL_SPEED_X
        self.y_speed = BALL_SPEED_Y
        self.collision_treshold = 5

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
        if self.on_paddle == False:
            self.check_wall_collision()
            self.check_top_collision()
            self.check_bottom_collision()
            self.check_paddle_collision()
            self.check_collision_bricks()

            # Move the ball
            self.x_pos += self.x_speed
            self.y_pos += self.y_speed

    def handle_missed_ball(self):
        self.game_instance.player_lives -= 1

        self.on_paddle = True
        self.x_pos = self.paddle.x_pos + 40
        self.y_pos = BALL_START_Y

    def check_collision_bricks(self):
        # Detect collision with blocks
        for brick in self.level.bricks:
            if self.rect.colliderect(brick.rect):
                if self.brick_collision_left_right(brick):
                    self.x_speed *= -1
                    self.brick_collision(brick)
                if self.brick_collision_top_bottom(brick):
                    self.y_speed *= -1
                    self.brick_collision(brick)

    def brick_collision(self, brick):
        brick.health -= 1
        self.game_instance.player_score += 10
        if brick.health == 0:
            self.remove_brick(brick)
            self.game_instance.boost_handler.check_boost_spawn()

    def remove_brick(self, brick):
        brick.width = 0
        brick.height = 0
        brick.rect.width = 0
        brick.rect.height = 0
        self.level.update_bricks(self.level.bricks)

    def brick_collision_left_right(self, brick):
        return (
            abs(self.rect.left - brick.rect.right) < self.collision_treshold
            and self.x_speed < 0
        ) or (
            abs(self.rect.right - brick.rect.left) < self.collision_treshold
            and self.x_speed > 0
        )

    def brick_collision_top_bottom(self, brick):
        return (
            abs((self.rect.top) - brick.rect.bottom) < self.collision_treshold
            and self.y_speed < 0
        ) or (
            abs(self.rect.bottom - brick.rect.top) < self.collision_treshold
            and self.y_speed > 0
        )

    def check_wall_collision(self):
        if self.rect.left < self.ball_radius or self.rect.right > SCREEN_WIDTH:
            self.x_speed *= -1

    def check_top_collision(self):
        if self.rect.top < self.ball_radius:
            self.y_speed *= -1

    def check_bottom_collision(self):
        if self.rect.bottom > SCREEN_HEIGHT:
            self.handle_missed_ball()

    def check_paddle_collision(self):
        if self.rect.colliderect(self.paddle) and (
            abs(self.rect.bottom - self.paddle.rect.top) < self.collision_treshold
            and self.y_speed > 0
        ):
            self.y_speed *= -1
