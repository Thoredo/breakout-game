import pygame


class GameOverScreen:
    def __init__(self, display, game_state_manager, game_instance):
        self.display = display
        self.gamestatemanager = game_state_manager
        self.game_instance = game_instance
        self.game_over_font = pygame.font.SysFont("Arial", 90, bold=True)
        self.stats_font = pygame.font.SysFont("Arial", 30, bold=True)
        self.back_button_font = pygame.font.SysFont("Arial", 30, bold=True)

    def run(self):
        self.display.fill("black")
        self.draw()

    def draw(self):
        game_over_text = self.game_over_font.render("Game Over", True, "white")
        self.display.blit(game_over_text, (340, 200))

        final_level_text = self.stats_font.render(
            f"Level: {self.game_instance.current_level}", True, "white"
        )
        self.display.blit(final_level_text, (510, 370))

        final_score_text = self.stats_font.render(
            f"Score: {self.game_instance.player_score}", True, "white"
        )
        self.display.blit(final_score_text, (510, 420))

        pygame.draw.rect(self.display, "black", (500, 640, 120, 50))
        if (
            500 < self.game_instance.mouse[0] < 620
            and 640 < self.game_instance.mouse[1] < 710
        ):
            back_button_text = self.back_button_font.render("Back", True, "red")
            if self.game_instance.mouse_clicked[0] == True:
                self.open_main_menu()
        else:
            back_button_text = self.back_button_font.render("Back", True, "white")
        self.display.blit(back_button_text, (530, 647))

    def open_main_menu(self):
        self.gamestatemanager.set_state("main menu")