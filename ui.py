import pygame
from config import *

class Button:
    def __init__(self, text, pos_x, pos_y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.callback = callback
        self.color = GRAY
        self.hover = WHITE
        self.font = pygame.font.SysFont(FONT_NAME, 30)

    def draw(self, screen):
        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        is_hover = self.rect.collidepoint(mouse_position)
        color = self.hover if is_hover else self.color

        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        if is_hover and mouse_click:
            pygame.time.delay(150)
            self.callback()

class UI:
    def __init__(self,screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, 40)
        self.big_font = pygame.font.SysFont(FONT_NAME, 60)

    def show_main_menu(self, on_start, on_settings, on_quit):
        while True:
            self.screen.fill(WHITE)
            title_surface = self.big_font.render("Snake Game", True, GREEN)
            self.screen.blit(title_surface, (SCREEN_WIDTH - title_surface.get_width()) // 2, 100)

            buttons = [
                Button("Start Game", 300, 220, 200, 50, on_start),
                Button("Settings", 300, 290, 200, 50, on_settings),
                Button("Quit", 300, 360, 200, 50, on_quit)
            ]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for button in buttons:
                button.draw(self.screen)

            pygame.display.update()

    def show_mode_selector(self, on_select):
        while True:
            self.screen.fill(BLACK)
            title_surface = self.big_font.render("Select Mode", True, GREEN)
            self.screen.blit(title_surface, ((SCREEN_WIDTH - title_surface.get_width()) // 2, 100))

            buttons = [
                Button("Normal Mode", 300, 220, 200, 50, lambda: on_select("normal")),
                Button("Blitz Mode", 300, 290, 200, 50, lambda: on_select("blitz")),
                Button("Inverted Mode", 300, 360, 200, 50, lambda: on_select("inverted")),
            ]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            for button in buttons:
                button.draw(self.screen)

            pygame.display.update()

    def show_settings(self):
        while True:
            self.screen.fill(GRAY)
            text_surface = self.big_font.render("Settings - Coming Soon", True, WHITE)
            self.screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, SCREEN_HEIGHT // 2 - 30))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def show_score(self, score):
        score_surface = self.font.render(f"Score: {score}", True, WHITE)
        self.screen.blit(score_surface, (10, 10))

    def show_game_over(self, score, high_score):
        self.screen.fill(BLACK)
        messages = [
            self.big_font.render("Game Over!", True, RED),
            self.font.render(f"Score: {score}", True, WHITE),
            self.font.render(f"High Score: {high_score}", True, WHITE),
            self.font.render("Press Enter to Continue", True, GRAY)
        ]

        for index, message in enumerate(messages):
            self.screen.blit(message, (SCREEN_WIDTH // 2 - message.get_width() // 2, 180 + index * 60))

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
