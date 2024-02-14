from pygame import mixer
import time


class Sound:
    """
    Calls the sound effects for this game.

    hit_paddle_sound (pygame.mixer.sound): The sound used for when the ball hits
                    the paddle.
    hit_brick_sound (pygame.mixer.sound): The sound used for when the ball hits
                    a brick.
    break_brick_sound (pygame.mixer.sound): The sound used for when a brick gets
                    broken.
    hit_wall_sound (pygame.mixer.sound): The sound used for when the ball hits
                    a wall.
    sound_cooldown_active (bool): Indicates wether the sounds are on cooldown
                    or not.
    """

    def __init__(self):
        """
        Initializes the Sound object.
        """
        self.hit_paddle_sound = mixer.Sound("./sounds/hit_paddle.wav")
        self.hit_brick_sound = mixer.Sound("./sounds/hit_brick.wav")
        self.hit_brick_sound.set_volume(0.5)
        self.break_brick_sound = mixer.Sound("./sounds/break_brick.wav")
        self.break_brick_sound.set_volume(0.5)
        self.hit_wall_sound = mixer.Sound("./sounds/hit_wall.wav")
        self.hit_wall_sound.set_volume(0.3)
        self.sound_cooldown_active = False
        self.start_time = ""

    def play_hit_paddle(self):
        """
        Plays the hit_paddle_sound.
        """
        self.check_cooldown()
        if not self.sound_cooldown_active:
            mixer.Sound.play(self.hit_paddle_sound)
            self.start_cooldown()

    def play_hit_brick(self):
        """
        Plays the hit_brick_sound.
        """
        self.check_cooldown()
        if not self.sound_cooldown_active:
            mixer.Sound.play(self.hit_brick_sound)
            self.start_cooldown()

    def play_break_brick(self):
        """
        Plays the break_brick_sound.
        """
        self.check_cooldown()
        if not self.sound_cooldown_active:
            mixer.Sound.play(self.break_brick_sound)
            self.start_cooldown()

    def play_hit_wall(self):
        """
        Plays the play_hit_wall.
        """
        self.check_cooldown()
        if not self.sound_cooldown_active:
            mixer.Sound.play(self.hit_wall_sound)
            self.start_cooldown()

    def start_cooldown(self):
        """
        Starts the cooldown on sounds.
        """
        if not self.sound_cooldown_active:
            self.start_time = time.time()
            self.sound_cooldown_active = True

    def check_cooldown(self):
        """
        Checks when the cooldown started and ends it once 0.3 seconds passed.
        """
        if self.sound_cooldown_active:
            time_passed = time.time() - self.start_time

            if time_passed > 0.3:
                self.sound_cooldown_active = False
