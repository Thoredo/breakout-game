class GameScreen:
    def __init__(self, display, game_state_manager, paddle, ball):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.paddle = paddle
        self.ball = ball

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        self.paddle.draw_paddle()
        self.ball.draw_ball()
