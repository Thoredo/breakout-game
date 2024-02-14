from pygame import mixer


class Sound:
    """
    Calls the sound effects for this game.

    hit_paddle_sound (pygame.mixer.sound): The sound used for when the ball hits
                    the paddle.
    hit_brick_sound (pygame.mixer.sound): The sound used for when the ball hits
                    a brick.
    break_brick_sound (pygame.mixer.sound): The sound used for when a brick gets
                    broken.
    """

    def __init__(self):
        """
        Initializes the Sound object.
        """
        self.hit_paddle_sound = mixer.Sound("./sounds/hit_paddle.wav")
        self.hit_brick_sound = mixer.Sound("./sounds/hit_brick.wav")
        self.break_brick_sound = mixer.Sound("./sounds/break_brick.wav")

    def play_hit_paddle(self):
        """
        Plays the hit_paddle_sound.
        """
        mixer.Sound.play(self.hit_paddle_sound)

    def play_hit_brick(self):
        """
        Plays the hit_brick_sound.
        """
        mixer.Sound.play(self.hit_brick_sound)

    def play_break_brick(self):
        """
        Plays the break_brick_sound.
        """
        mixer.Sound.play(self.break_brick_sound)
