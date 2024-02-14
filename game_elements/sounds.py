from pygame import mixer


class Sound:
    """
    Calls the sound effects for this game.

    hit_paddle_sound (pygame.mixer.sound): The sound used for when the ball hits
                    the paddle.
    """

    def __init__(self):
        """
        Initializes the Sound object.
        """
        self.hit_paddle_sound = mixer.Sound("./sounds/hit_paddle.wav")

    def play_hit_paddle(self):
        """
        Plays the hit_paddle_sound
        """
        mixer.Sound.play(self.hit_paddle_sound)
