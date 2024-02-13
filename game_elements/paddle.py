import pygame
import constants
import time
from game_elements.bullet import Bullet

PADDLE_SPEED = constants.PADDLE_SPEED
PADDLE_STARTING_X = constants.PADDLE_STARTING_X
PADDLE_STARTING_Y = constants.PADDLE_STARTING_Y


class Paddle:
    def __init__(self, display, game_instance):
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
        if self.x_pos > 0:
            self.x_pos -= PADDLE_SPEED

    def move_right(self):
        if self.x_pos < 1000:
            self.x_pos += PADDLE_SPEED

    def activate_gun(self):
        self.gun_active = True

    def draw_gun(self):
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
        self.timer_active = True
        self.time_started = time.time()

    def check_cooldown(self):
        time_passed = time.time() - self.time_started
        if time_passed > 0.5:
            self.gun_cooldown = False
            self.timer_active = False
