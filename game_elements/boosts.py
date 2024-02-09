import random


class BoostHandler:
    def __init__(self):
        pass

    def check_boost_spawn(self):
        spawn_number = random.randint(1, 10000)
        print(spawn_number)
        if spawn_number < 500:
            self.spawn_boost()

    def spawn_boost(self):
        print("spawn boost")
