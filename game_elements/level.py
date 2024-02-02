from game_elements.brick import Brick


class Level:
    def __init__(self, display, level):
        self.display = display
        self.current_level = level
        # fmt: off
        self.x_positions = [55, 120, 185, 250, 315, 380, 445, 510, 575, 640, 
                            705, 770, 835, 900, 965]
        self.y_positions = [100, 125, 150, 175, 200, 225, 250, 275, 300]
        # fmt: on

    def draw(self):
        for y_pos in self.y_positions:
            for x_pos in self.x_positions:
                Brick(self.display, 1, x_pos, y_pos)
