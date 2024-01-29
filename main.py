import pygame
import pygame_menu
import sys

WIDTH, HEIGHT = 1080, 720
FPS = 60


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.is_running = True

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager)

        self.states = {"main menu": self.main_menu}

    def run(self):
        while self.is_running:
            self.handle_events()
            self.clock.tick(FPS)

            self.states[self.game_state_manager.get_state()].run()
            pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False


class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gamestatemanager = game_state_manager

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        menu = pygame_menu.Menu(
            title="Breakout",
            width=1080,
            height=720,
            theme=pygame_menu.themes.THEME_DARK,
        )
        play_button = menu.add.button("Play")
        instructions_button = menu.add.button("Instructions")
        highscores_button = menu.add.button("Highscores")
        quit_button = menu.add.button("Quit")
        menu.mainloop(self.display)

    def open_instructions(self):
        pass


class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state


if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
    pygame.quit()
    sys.exit()
