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
        self.mouse = (0, 0)
        self.mouse_clicked = (False, False, False)

        pygame.font.init()
        self.menu_font = pygame.font.SysFont("Arial", 30, bold=True)

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
            self.mouse = pygame.mouse.get_pos()
            self.mouse_clicked = pygame.mouse.get_pressed()
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

        # Play Button
        pygame.draw.rect(self.display, "black", (490, 300, 100, 50))
        if 490 < game_instance.mouse[0] < 590 and 300 < game_instance.mouse[1] < 350:
            play_text = game_instance.menu_font.render("Play", True, "red")
        else:
            play_text = game_instance.menu_font.render("Play", True, "white")
        self.display.blit(play_text, (515, 307))

        # Instructions button
        pygame.draw.rect(self.display, "black", (450, 360, 200, 50))
        if 450 < game_instance.mouse[0] < 650 and 360 < game_instance.mouse[1] < 410:
            instructions_text = game_instance.menu_font.render(
                "Instructions", True, "red"
            )
            if game_instance.mouse_clicked[0] == True:
                self.open_instructions()
        else:
            instructions_text = game_instance.menu_font.render(
                "Instructions", True, "white"
            )
        self.display.blit(instructions_text, (480, 366))

        # Quit Button
        pygame.draw.rect(self.display, "black", (490, 420, 100, 50))
        if 490 < game_instance.mouse[0] < 590 and 420 < game_instance.mouse[1] < 470:
            quit_text = game_instance.menu_font.render("Quit", True, "red")
        else:
            quit_text = game_instance.menu_font.render("Quit", True, "white")
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
