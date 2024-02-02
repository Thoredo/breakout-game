from game_elements.brick import Brick


class Level:
    def __init__(self, display, level):
        self.display = display
        self.current_level = level

    def draw(self):
        Brick(self.display, 1, 5, 5)
