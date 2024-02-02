import pygame


class MainMenu:
    def __init__(self, display, game_state_manager, game_instance):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.game_instance = game_instance
        self.menu_font = pygame.font.SysFont("Arial", 30, bold=True)

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        logo = pygame.image.load("images/logo.png")
        self.display.blit(logo, (273, 145))

        # Play Button
        pygame.draw.rect(self.display, "black", (490, 300, 100, 50))
        if (
            490 < self.game_instance.mouse[0] < 590
            and 300 < self.game_instance.mouse[1] < 350
        ):
            play_text = self.menu_font.render("Play", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.start_game()
        else:
            play_text = self.menu_font.render("Play", True, "white")
        self.display.blit(play_text, (515, 307))

        # Instructions button
        pygame.draw.rect(self.display, "black", (450, 360, 200, 50))
        if (
            450 < self.game_instance.mouse[0] < 650
            and 360 < self.game_instance.mouse[1] < 410
        ):
            instructions_text = self.menu_font.render("Instructions", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.open_instructions()
        else:
            instructions_text = self.menu_font.render("Instructions", True, "white")
        self.display.blit(instructions_text, (480, 366))

        # Quit Button
        pygame.draw.rect(self.display, "black", (490, 420, 100, 50))
        if (
            490 < self.game_instance.mouse[0] < 590
            and 420 < self.game_instance.mouse[1] < 470
        ):
            quit_text = self.menu_font.render("Quit", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.quit_game()
        else:
            quit_text = self.menu_font.render("Quit", True, "white")
        self.display.blit(quit_text, (515, 426))

    def open_instructions(self):
        self.gamestatemanager.set_state("instructions")

    def quit_game(self):
        self.game_instance.is_running = False

    def start_game(self):
        self.gamestatemanager.set_state("game")
