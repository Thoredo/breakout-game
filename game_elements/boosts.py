import random
import pygame
import time
import constants
from game_elements.ball import Ball

EXTEND_TYPE = "extend paddle"
SHRINK_TYPE = "shrink paddle"
FASTER_TYPE = "faster ball"
SLOWER_TYPE = "slower ball"
LIFE_TYPE = "extra life"
POINTS_TYPE = "point boost"
BALL_TYPE = "extra ball"
SHOOT_TYPE = "paddle shoots"
SPEED_BOOSTS_NUMBER = constants.SPEED_BOOSTS_NUMBER


class BoostHandler:
    def __init__(self, display, game_instance):
        self.display = display
        self.game_instance = game_instance
        self.on_screen_boosts = []
        self.active_boosts = []

    def check_boost_spawn(self, brick):
        spawn_number = random.randint(1, 10000)
        if spawn_number < 1500:
            self.select_boost_type(brick)

    def select_boost_type(self, brick):
        boost_type_number = random.randint(1, 1000)

        if boost_type_number <= 150:
            self.spawn_boost(EXTEND_TYPE, "enlarge_paddle", brick)
        elif 150 < boost_type_number <= 300:
            self.spawn_boost(SHRINK_TYPE, "shrink_paddle", brick)
        elif 300 < boost_type_number <= 450:
            self.spawn_boost(FASTER_TYPE, "speed_up_ball", brick)
        elif 450 < boost_type_number <= 600:
            self.spawn_boost(SLOWER_TYPE, "slow_down_ball", brick)
        elif 600 < boost_type_number <= 750:
            self.spawn_boost(SHOOT_TYPE, "paddle_shoot", brick)
        elif 750 < boost_type_number <= 900:
            self.spawn_boost(POINTS_TYPE, "increase_points_gained", brick)
        elif 900 < boost_type_number <= 950:
            self.spawn_boost(BALL_TYPE, "add_ball", brick)
        elif 950 < boost_type_number <= 1000:
            self.spawn_boost(LIFE_TYPE, "add_life", brick)

    def draw(self):
        if len(self.on_screen_boosts) > 0:
            for boost in self.on_screen_boosts:
                boost_rect = self.draw_boost(boost)

                # Remove boost once its out of the screen
                if boost["y_pos"] == 720:
                    self.on_screen_boosts.remove(boost)

                self.boost_collision_paddle(boost_rect, boost)

                boost["y_pos"] += 2

        self.check_timer()

    def spawn_boost(self, type, image, brick):
        boost_type = type
        boost_image = f"images/{image}.png"
        boost_info = {
            "type": boost_type,
            "image": boost_image,
            "x_pos": brick.x_pos,
            "y_pos": brick.y_pos,
        }
        self.on_screen_boosts.append(boost_info)

    def draw_boost(self, boost):
        new_boost = pygame.image.load(boost["image"])
        self.display.blit(new_boost, (boost["x_pos"], boost["y_pos"]))
        return pygame.Rect(boost["x_pos"], boost["y_pos"], 80, 10)

    def boost_collision_paddle(self, boost_rect, boost):
        # Detect Collision with paddle
        if boost_rect.colliderect(self.game_instance.paddle):
            self.activate_boost(boost)
            self.on_screen_boosts.remove(boost)

    def activate_boost(self, boost):
        if boost["type"] == EXTEND_TYPE:
            self.start_extend_boost(boost)
        elif boost["type"] == SHRINK_TYPE:
            self.start_shrink_boost(boost)
        elif boost["type"] == FASTER_TYPE:
            self.start_faster_boost(boost)
        elif boost["type"] == SLOWER_TYPE:
            self.start_slower_boost(boost)
        elif boost["type"] == LIFE_TYPE and self.game_instance.player_lives < 5:
            self.start_life_boost()
        elif boost["type"] == POINTS_TYPE:
            self.start_points_boost(boost)
        elif boost["type"] == BALL_TYPE:
            self.start_ball_boost()

    def boost_timer(self, boost):
        time_started = time.time()
        self.active_boosts.append(
            {"time started": time_started, "boost": boost, "time passed": 0}
        )

    def check_timer(self):
        for boost in self.active_boosts:
            boost["time passed"] = time.time() - boost["time started"]
            if boost["time passed"] > 30:
                self.active_boosts.remove(boost)
                self.deactivate_boost(boost["boost"])

    def deactivate_boost(self, boost):
        if boost["type"] == EXTEND_TYPE:
            self.stop_extend_boost()
        elif boost["type"] == SHRINK_TYPE:
            self.stop_shrink_boost()
        elif boost["type"] == FASTER_TYPE:
            self.stop_faster_boost()
        elif boost["type"] == SLOWER_TYPE:
            self.stop_slower_boost()
        elif boost["type"] == POINTS_TYPE:
            self.stop_points_boost()

    def start_extend_boost(self, boost):
        self.game_instance.paddle.width += 30
        self.boost_timer(boost)

    def stop_extend_boost(self):
        self.game_instance.paddle.width -= 30

    def start_shrink_boost(self, boost):
        self.game_instance.paddle.width -= 15
        self.boost_timer(boost)

    def stop_shrink_boost(self):
        self.game_instance.paddle.width += 15

    def start_faster_boost(self, boost):
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
        self.boost_timer(boost)

    def stop_faster_boost(self):
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER

    def start_slower_boost(self, boost):
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
        self.boost_timer(boost)

    def stop_slower_boost(self):
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER

    def start_life_boost(self):
        self.game_instance.player_lives += 1

    def start_points_boost(self, boost):
        self.game_instance.ball.points_gained = 15
        self.boost_timer(boost)

    def stop_points_boost(self):
        self.game_instance.ball.points_gained = 10

    def start_ball_boost(self):
        if len(self.game_instance.active_balls) < 3:
            self.new_ball = Ball(
                self.display,
                self.game_instance.paddle,
                self.game_instance,
                self.game_instance.level,
                ball_speed_x=self.game_instance.active_balls[0].x_speed * -1,
                ball_speed_y=-3,
                x_pos=self.game_instance.active_balls[0].x_pos,
                y_pos=self.game_instance.active_balls[0].y_pos,
                on_paddle=False,
            )
            self.game_instance.active_balls.append(self.new_ball)
