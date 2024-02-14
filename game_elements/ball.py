import pygame
import constants
from game_elements.sounds import Sound

SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
BALL_SPEED_X = constants.BALL_SPEED_X
BALL_SPEED_Y = constants.BALL_SPEED_Y
BALL_START_X = constants.BALL_START_X
BALL_START_Y = constants.BALL_START_Y
POINTS_PER_HIT = constants.POINTS_PER_HIT


class Ball:
    """
    Represents the ball in the game.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    paddle (Paddle): The paddle object.
    game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
    level (Level): The current level object.
    ball_radius (int): The radius of the ball.
    on_paddle (bool): Indicates whether the ball is on the paddle or not.
    x_pos (int): The x-coordinate position of the ball.
    y_pos (int): The y-coordinate position of the ball.
    x_speed (int): The speed of the ball in the horizontal direction.
    y_speed (int): The speed of the ball in the vertical direction.
    collision_treshold (int): The threshold for collision detection.
    points_gained (int): The points gained when hitting a brick.
    rect (pygame.Rect): The rectangular area representing the ball.
    sound (Sound): Instance of the Sound class.
    """

    def __init__(
        self,
        display,
        paddle,
        game_instance,
        level,
        ball_speed_x=BALL_SPEED_X,
        ball_speed_y=BALL_SPEED_Y,
        x_pos=BALL_START_X,
        y_pos=BALL_START_Y,
        on_paddle=True,
    ):
        """
        Initializes the Ball object.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        paddle (Paddle): The paddle object.
        game_instance (Game): Instance of the main Game class, allowing access to game state and components.
        level (Level): The current level object.
        ball_speed_x (int): The initial speed of the ball in the horizontal direction.
        ball_speed_y (int): The initial speed of the ball in the vertical direction.
        x_pos (int): The initial x-coordinate position of the ball.
        y_pos (int): The initial y-coordinate position of the ball.
        on_paddle (bool): Indicates whether the ball is on the paddle or not.
        """
        self.display = display
        self.paddle = paddle
        self.game_instance = game_instance
        self.level = level

        self.ball_radius = 10
        self.on_paddle = on_paddle
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = ball_speed_x
        self.y_speed = ball_speed_y
        self.collision_treshold = 5
        self.points_gained = POINTS_PER_HIT
        self.rect = pygame.Rect(
            self.x_pos, self.y_pos, self.ball_radius, self.ball_radius
        )
        self.sound = Sound()

    def draw_ball(self):
        """
        Draws the ball on the screen.
        """
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
        """
        Moves the ball on the screen based on its speed and direction.
        """
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
        """
        Handles the case when the ball misses the paddle.
        """
        self.game_instance.player_lives -= 1
        self.back_on_paddle()
        self.game_instance.boost_handler.remove_on_screen_boosts()
        self.game_instance.boost_handler.stop_active_boosts()
        self.paddle.remove_bullets()

    def check_collision_bricks(self):
        """
        Checks collision between the ball and bricks.
        """
        for brick in self.level.bricks:
            if self.rect.colliderect(brick.rect):
                if self.brick_collision_left_right(brick):
                    self.x_speed *= -1
                    self.brick_collision(brick)
                if self.brick_collision_top_bottom(brick):
                    self.y_speed *= -1
                    self.brick_collision(brick)

    def brick_collision(self, brick):
        """
        Handles the collision between the ball and a brick.

        Parameters
        ----------
        brick (Brick): The brick object collided with.
        """
        brick.health -= 1
        self.game_instance.player_score += self.points_gained
        self.game_instance.boost_handler.check_boost_spawn(brick)
        self.sound.play_hit_brick()

        if brick.health == 0:
            self.remove_brick(brick)
            self.sound.play_break_brick()
        else:
            self.sound.play_hit_brick()

        self.game_instance.check_victory()

    def remove_brick(self, brick):
        """
        Removes the brick from the level.

        Parameters
        ----------
        brick (Brick): The brick object to be removed.
        """
        brick.width = 0
        brick.height = 0
        brick.rect.width = 0
        brick.rect.height = 0
        self.level.update_bricks(self.level.bricks)

    def brick_collision_left_right(self, brick):
        """
        Checks left-right collision with a brick.

        Parameters
        ----------
        brick (Brick): The brick object.

        Returns
        -------
        bool: True if left-right collision, False otherwise.
        """
        return (
            abs(self.rect.left - brick.rect.right) < self.collision_treshold
            and self.x_speed < 0
        ) or (
            abs(self.rect.right - brick.rect.left) < self.collision_treshold
            and self.x_speed > 0
        )

    def brick_collision_top_bottom(self, brick):
        """
        Checks top-bottom collision with a brick.

        Parameters
        ----------
        brick (Brick): The brick object.

        Returns
        -------
        bool: True if top-bottom collision, False otherwise.
        """
        return (
            abs((self.rect.top) - brick.rect.bottom) < self.collision_treshold
            and self.y_speed < 0
        ) or (
            abs(self.rect.bottom - brick.rect.top) < self.collision_treshold
            and self.y_speed > 0
        )

    def check_wall_collision(self):
        """
        Checks collision with the walls of the screen.
        """
        if self.rect.left < self.ball_radius or self.rect.right > SCREEN_WIDTH:
            self.x_speed *= -1

    def check_top_collision(self):
        """
        Checks collision with the top wall of the screen.
        """
        if self.rect.top < self.ball_radius:
            self.y_speed *= -1

    def check_bottom_collision(self):
        """
        Checks collision with the bottom wall of the screen.
        """
        if self.rect.bottom > SCREEN_HEIGHT:
            if len(self.game_instance.active_balls) > 1:
                self.game_instance.active_balls.remove(self)
            else:
                self.handle_missed_ball()
                self.reset_direction()

    def check_paddle_collision(self):
        """
        Checks collision with the paddle.
        """
        if self.rect.colliderect(self.paddle) and (
            abs(self.rect.bottom - self.paddle.rect.top) < self.collision_treshold
            and self.y_speed > 0
        ):
            self.y_speed *= -1
            self.sound.play_hit_paddle()

    def back_on_paddle(self):
        """
        Puts the ball back on the paddle.
        """
        self.game_instance.active_balls[0].on_paddle = True
        self.game_instance.active_balls[0].x_pos = self.paddle.x_pos + 40
        self.game_instance.active_balls[0].y_pos = BALL_START_Y

    def reset_direction(self):
        """
        Resets the balls direction to move north east.
        """
        self.game_instance.active_balls[0].x_speed = 3
        self.game_instance.active_balls[0].y_speed = -3
