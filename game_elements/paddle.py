import pygame
import constants
import time
from game_elements.bullet import Bullet

PADDLE_SPEED = constants.PADDLE_SPEED
PADDLE_STARTING_X = constants.PADDLE_STARTING_X
PADDLE_STARTING_Y = constants.PADDLE_STARTING_Y


class Paddle:
    """
    Represents the paddle object in the game.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_instance (Game): Instance of the main Game class, allowing access to
                    game state and components.
    width (int): The width of the paddle.
    height (int): The height of the paddle.
    x_pos (int): The x-coordinate of the top-left corner of the paddle.
    y_pos (int): The y-coordinate of the top-left corner of the paddle.
    gun_active (bool): Indicates whether the gun power-up is active or not.
    bullets (list): List containing instances of Bullet class representing
                    bullets fired by the paddle.
    gun_cooldown (bool): Indicates whether the gun is on cooldown or not.
    timer_active (bool): Indicates whether the cooldown timer is active or not.
    time_started (float): The time when the cooldown started.
    """

    def __init__(self, display, game_instance):
        """
        Initializes the Paddle object.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_instance (Game): Instance of the main Game class, allowing access
                        to game state and components.
        """
        self.display = display
        self.game_instance = game_instance
        self.width = 80
        self.height = 10
        self.x_pos = PADDLE_STARTING_X
        self.y_pos = PADDLE_STARTING_Y
        self.gun_active = False
        self.bullets = []
        self.gun_cooldown = False
        self.timer_active = False
        self.time_started = 0

    def draw_paddle(self):
        """
        Draws the paddle and any active bullets on the game window.
        """
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width + 10, self.height)
        pygame.draw.rect(
            self.display,
            "yellow",
            (self.x_pos, self.y_pos, self.width, self.height),
        )
        self.draw_gun()
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                bullet.move()

    def move_left(self):
        """
        Moves the paddle to the left if possible.
        """
        if self.x_pos > 0:
            self.x_pos -= PADDLE_SPEED

    def move_right(self):
        """
        Moves the paddle to the right if possible.
        """
        if self.x_pos < 1000:
            self.x_pos += PADDLE_SPEED

    def activate_gun(self):
        """
        Activates the gun power-up for the paddle.
        """
        self.gun_active = True

    def draw_gun(self):
        """
        Draws the gun power-up on the paddle if active.
        """
        self.paddle_middle = self.x_pos + (self.width / 2) - 5
        self.gun_height = 20
        gun_width = 10
        if self.gun_active == True:
            pygame.draw.rect(
                self.display,
                "red",
                (
                    self.paddle_middle,
                    self.y_pos - self.gun_height,
                    gun_width,
                    self.gun_height,
                ),
            )

    def shoot_gun(self):
        """
        Fires bullets from the paddle if the gun is active and not on cooldown.
        """
        if self.gun_active == True and self.gun_cooldown == False:

            gun_top = self.y_pos - (self.gun_height * 2)
            new_bullet = Bullet(
                self.display, self.paddle_middle, gun_top, self.game_instance
            )
            self.bullets.append(new_bullet)
            self.gun_cooldown = True
        if not self.timer_active:
            self.start_cooldown()
        else:
            self.check_cooldown()

    def start_cooldown(self):
        """
        Starts the cooldown timer for the gun.
        """
        self.timer_active = True
        self.time_started = time.time()

    def check_cooldown(self):
        """
        Checks if the gun is still on cooldown.
        """
        time_passed = time.time() - self.time_started
        if time_passed > 0.5:
            self.gun_cooldown = False
            self.timer_active = False

    def remove_gun(self):
        """
        Deactivates the gun power-up.
        """
        self.gun_active = False
