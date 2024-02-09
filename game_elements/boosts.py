import random
import pygame


class BoostHandler:
    def __init__(self, display, game_instance):
        self.display = display
        self.game_instance = game_instance
        self.on_screen_boosts = []
        self.boost_id = 1

    def check_boost_spawn(self, brick):
        spawn_number = random.randint(1, 10000)
        if spawn_number < 1000:
            self.spawn_boost(brick)

    def spawn_boost(self, brick):
        boost_type_number = random.randint(1, 1000)

        if boost_type_number <= 999:
            boost_type = "extend paddle"
            boost_image = "images/enlarge_paddle.png"
            boost_info = {
                "id": self.boost_id,
                "type": boost_type,
                "image": boost_image,
                "x_pos": brick.x_pos,
                "y_pos": brick.y_pos,
            }
            self.on_screen_boosts.append(boost_info)
            self.boost_id += 1
        elif 150 < boost_type_number <= 300:
            print("smaller paddle")
        elif 300 < boost_type_number <= 450:
            print("faster ball")
        elif 450 < boost_type_number <= 600:
            print("slower ball")
        elif 600 < boost_type_number <= 750:
            print("paddle shoots")
        elif 750 < boost_type_number <= 900:
            print("1.5 point boost")
        elif 900 < boost_type_number <= 950:
            print("extra life")
        elif 950 < boost_type_number <= 1000:
            print("extra life")

    def draw(self):
        if len(self.on_screen_boosts) > 0:
            for boost in self.on_screen_boosts:
                new_boost = pygame.image.load(boost["image"])
                self.display.blit(new_boost, (boost["x_pos"], boost["y_pos"]))
                boost_rect = pygame.Rect(boost["x_pos"], boost["y_pos"], 80, 10)

                # Remove boost once its out of the screen
                if boost["y_pos"] == 720:
                    self.on_screen_boosts.remove(boost)

                # Detect Collision with paddle
                if boost_rect.colliderect(self.game_instance.paddle):
                    self.on_screen_boosts.remove(boost)

                boost["y_pos"] += 2
