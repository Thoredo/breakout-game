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
    """
    Manages the boost functionalities in the game.

    Attributes
    ----------
    display (pygame.Surface): The Pygame surface representing the game window.
    game_instance (Game): Instance of the main Game class, allowing access to game state and components.
    on_screen_boosts (list): List containing active boosts currently on the screen.
    active_boosts (list): List containing boosts currently active in the game.
    """

    def __init__(self, display, game_instance):
        """
        Initializes the BoostHandler object.

        Parameters
        ----------
        display (pygame.Surface): The Pygame surface representing the game window.
        game_instance (Game): Instance of the main Game class, allowing access to game state and components.
        """
        self.display = display
        self.game_instance = game_instance
        self.on_screen_boosts = []
        self.active_boosts = []

    def check_boost_spawn(self, brick):
        """
        Checks if a boost should be spawned after breaking a brick.

        Parameters
        ----------
        brick (Brick): The brick object that was broken.
        """
        spawn_number = random.randint(1, 10000)
        # if spawn_number < 1500:
        if spawn_number < 9999:
            self.select_boost_type(brick)

    def select_boost_type(self, brick):
        """
        Selects the type of boost to spawn based on probability.

        Parameters
        ----------
        brick (Brick): The brick object that was broken.
        """
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
        """
        Draws the boosts on the screen and handles boost functionalities.
        """
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
        """
        Spawns a boost on the screen.

        Parameters
        ----------
        type (str): The type of boost.
        image (str): The image file path for the boost.
        brick (Brick): The brick object where the boost spawns.
        """
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
        """
        Draws the boost on the screen.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        new_boost = pygame.image.load(boost["image"])
        self.display.blit(new_boost, (boost["x_pos"], boost["y_pos"]))
        return pygame.Rect(boost["x_pos"], boost["y_pos"], 80, 10)

    def boost_collision_paddle(self, boost_rect, boost):
        """
        Detects collision between a boost and the paddle.

        Parameters
        ----------
        boost_rect (pygame.Rect): The rectangle representing the boost.
        boost (dict): The boost information.
        """
        if boost_rect.colliderect(self.game_instance.paddle):
            self.activate_boost(boost)
            self.on_screen_boosts.remove(boost)

    def activate_boost(self, boost):
        """
        Activates the boost and starts its timer.

        Parameters
        ----------
        boost (dict): The boost information.
        """
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
        elif boost["type"] == SHOOT_TYPE:
            self.start_shoot_boost(boost)

    def boost_timer(self, boost):
        """
        Starts the timer for the boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        time_started = time.time()
        self.active_boosts.append(
            {"time started": time_started, "boost": boost, "time passed": 0}
        )

    def check_timer(self):
        """
        Checks the timer for active boosts and deactivates them when the time expires.
        """
        for boost in self.active_boosts:
            boost["time passed"] = time.time() - boost["time started"]
            if boost["time passed"] > 30:
                self.active_boosts.remove(boost)
                self.deactivate_boost(boost["boost"])

    def deactivate_boost(self, boost):
        """
        Deactivates the boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
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
        elif boost["type"] == SHOOT_TYPE:
            self.stop_shoot_boost()

    def start_extend_boost(self, boost):
        """
        Starts the extend paddle boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        self.game_instance.paddle.width += 30
        self.boost_timer(boost)

    def stop_extend_boost(self):
        """
        Stops the extend paddle boost.
        """
        self.game_instance.paddle.width -= 30

    def start_shrink_boost(self, boost):
        """
        Starts the shrink paddle boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        self.game_instance.paddle.width -= 15
        self.boost_timer(boost)

    def stop_shrink_boost(self):
        """
        Stops the shrink paddle boost.
        """
        self.game_instance.paddle.width += 15

    def start_faster_boost(self, boost):
        """
        Starts the faster ball boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
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
        """
        Stops the faster ball boost.
        """
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER

    def start_slower_boost(self, boost):
        """
        Starts the slower ball boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
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
        """
        Stops the slower ball boost.
        """
        if self.game_instance.ball.x_speed > 0:
            self.game_instance.ball.x_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.x_speed -= SPEED_BOOSTS_NUMBER
        if self.game_instance.ball.y_speed > 0:
            self.game_instance.ball.y_speed += SPEED_BOOSTS_NUMBER
        else:
            self.game_instance.ball.y_speed -= SPEED_BOOSTS_NUMBER

    def start_life_boost(self):
        """
        Starts the extra life boost.
        """
        self.game_instance.player_lives += 1

    def start_points_boost(self, boost):
        """
        Starts the point boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        self.game_instance.ball.points_gained = 15
        self.boost_timer(boost)

    def stop_points_boost(self):
        """
        Stops the point boost.
        """
        self.game_instance.ball.points_gained = 10

    def start_ball_boost(self):
        """
        Starts the extra ball boost.
        """
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

    def start_shoot_boost(self, boost):
        """
        Starts the paddle shooting boost.

        Parameters
        ----------
        boost (dict): The boost information.
        """
        self.game_instance.paddle.activate_gun()
        self.boost_timer(boost)

    def stop_shoot_boost(self):
        """
        Stops the paddle shooting boost.
        """
        self.game_instance.paddle.remove_gun()

    def remove_on_screen_boosts(self):
        """
        Removes the boosts that are currently falling down.
        """
        self.on_screen_boosts = []
