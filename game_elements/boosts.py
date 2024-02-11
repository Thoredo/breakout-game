import random
import pygame
import time
import constants

EXTEND_TYPE = "extend paddle"
SHRINK_TYPE = "shrink paddle"
FASTER_TYPE = "faster ball"
SLOWER_TYPE = "slower ball"
LIFE_TYPE = "extra life"
POINTS_TYPE = "point boost"
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

        if boost_type_number <= 999:
            self.spawn_boost(EXTEND_TYPE, "enlarge_paddle", brick)
        elif 150 < boost_type_number <= 300:
            self.spawn_boost(SHRINK_TYPE, "shrink_paddle", brick)
        elif 300 < boost_type_number <= 450:
            self.spawn_boost(FASTER_TYPE, "speed_up_ball", brick)
        elif 450 < boost_type_number <= 600:
            self.spawn_boost(SLOWER_TYPE, "slow_down_ball", brick)
        elif 600 < boost_type_number <= 750:
            self.spawn_boost("paddle shoots", "paddle_shoot", brick)
        elif 750 < boost_type_number <= 900:
            self.spawn_boost(POINTS_TYPE, "increase_points_gained", brick)
        elif 900 < boost_type_number <= 950:
            self.spawn_boost("extra ball", "add_ball", brick)
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
            self.game_instance.paddle.width += 30
            self.boost_timer(boost)
        elif boost["type"] == SHRINK_TYPE:
            self.game_instance.paddle.width -= 15
            self.boost_timer(boost)
        elif boost["type"] == FASTER_TYPE:
            if self.game_instance.ball.x_speed > 0:
                self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
            if self.game_instance.ball.y_speed > 0:
                self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
            self.boost_timer(boost)
        elif boost["type"] == SLOWER_TYPE:
            if self.game_instance.ball.x_speed > 0:
                self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
            if self.game_instance.ball.y_speed > 0:
                self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
            self.boost_timer(boost)
        elif boost["type"] == LIFE_TYPE and self.game_instance.player_lives < 5:
            self.game_instance.player_lives += 1
        elif boost["type"] == POINTS_TYPE:
            self.game_instance.ball.points_gained = 15
            self.boost_timer(boost)

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
            self.game_instance.paddle.width -= 30
        elif boost["type"] == SHRINK_TYPE:
            self.game_instance.paddle.width += 15
        elif boost["type"] == FASTER_TYPE:
            if self.game_instance.ball.x_speed > 0:
                self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
            if self.game_instance.ball.y_speed > 0:
                self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
        elif boost["type"] == SLOWER_TYPE:
            if self.game_instance.ball.x_speed > 0:
                self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
            if self.game_instance.ball.y_speed > 0:
                self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
            else:
                self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
        elif boost["type"] == POINTS_TYPE:
            self.game_instance.ball.points_gained = 10
