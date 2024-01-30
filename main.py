import pygame
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

        pygame.font.init()
        self.my_font = pygame.font.SysFont("Arial", 30, bold=True)

        self.game_state_manager = GameStateManager("main menu")
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.instructions = InstructionsPage(self.screen, self.game_state_manager)

        self.states = {
            "main menu": self.main_menu,
            "instructions": self.instructions,
        }

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
        logo = pygame.image.load("logo.png")
        self.display.blit(logo, (273, 145))

        pygame.draw.rect(self.display, "black", (490, 300, 100, 50))
        play_text = game_instance.my_font.render("Play", True, "white")
        self.display.blit(play_text, (515, 307))

        pygame.draw.rect(self.display, "black", (450, 360, 200, 50))
        instructions_text = game_instance.my_font.render("Instructions", True, "white")
        self.display.blit(instructions_text, (480, 366))

        pygame.draw.rect(self.display, "black", (490, 420, 100, 50))
        quit_text = game_instance.my_font.render("Quit", True, "white")
        self.display.blit(quit_text, (515, 426))

    def open_instructions(self):
        self.gamestatemanager.set_state("instructions")


class InstructionsPage:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.gamestatemanager = game_state_manager

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        self.instructions_page.mainloop(self.display)


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
