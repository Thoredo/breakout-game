from game_elements.brick import Brick
import random


class Level:
    def __init__(self, display, level):
        self.display = display
        self.current_level = level
        self.bricks = []
        # fmt: off
        self.x_positions = [55, 120, 185, 250, 315, 380, 445, 510, 575, 640, 
                            705, 770, 835, 900, 965]
        self.y_positions = [100, 125, 150, 175, 200, 225, 250, 275, 300]
        # fmt: on

    def create_bricks(self):
        for y_pos in self.y_positions:
            for x_pos in self.x_positions:
                spawn_chance = random.randint(1, 100)
                if 40 > spawn_chance and self.current_level > 1:
                    new_brick = Brick(
                        self.display, self.current_level - 1, x_pos, y_pos
                    )
                    self.bricks.append(new_brick)
                elif 95 > spawn_chance:
                    new_brick = Brick(self.display, self.current_level, x_pos, y_pos)
                    self.bricks.append(new_brick)

    def draw(self):
        for brick in self.bricks:
            brick.draw()

    def update_bricks(self, bricks_list):
        self.bricks = bricks_list
