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
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, 40)
        self.big_font = pygame.font.SysFont(FONT_NAME, 60)
        self.small_font = pygame.font.SysFont(FONT_NAME, 28)

    def show_main_menu(self, on_start, on_settings, on_quit, on_leaderboard):
        while True:
            self.screen.fill(WHITE)
            title_surface = self.big_font.render("Snake Game", True, GREEN)
            self.screen.blit(title_surface, ((SCREEN_WIDTH - title_surface.get_width()) // 2, 100))

            buttons = [
                Button("Start Game", 300, 200, 200, 50, on_start),
                Button("Leaderboard", 300, 270, 200, 50, on_leaderboard),
                Button("Settings", 300, 340, 200, 50, on_settings),
                Button("Quit", 300, 410, 200, 50, on_quit)
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

    def ask_player_name(self):
        name = ""
        input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 40)
        font = pygame.font.SysFont(FONT_NAME, 30)

        while True:
            self.screen.fill(BLACK)
            title = self.font.render("New High Score!", True, GREEN)
            prompt = self.small_font.render("Enter your name:", True, WHITE)
            name_surface = font.render(name, True, BLACK)

            pygame.draw.rect(self.screen, WHITE, input_box)
            self.screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, 200))
            self.screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, 250))
            self.screen.blit(name_surface, (input_box.x + 10, input_box.y + 5))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and name.strip():
                        return name.strip()
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 12 and event.unicode.isprintable():
                            name += event.unicode

    def ask_leaderboard_mode(self):
        while True:
            self.screen.fill(BLACK)
            title = self.big_font.render("View Leaderboard", True, GREEN)
            self.screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, 100))

            buttons = [
                Button("Normal", 300, 220, 200, 50, lambda: setattr(self, 'selected_mode', 'normal')),
                Button("Blitz", 300, 290, 200, 50, lambda: setattr(self, 'selected_mode', 'blitz')),
                Button("Inverted", 300, 360, 200, 50, lambda: setattr(self, 'selected_mode', 'inverted')),
            ]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.rect.collidepoint(pygame.mouse.get_pos()):
                            return self.selected_mode

            for button in buttons:
                button.draw(self.screen)

            pygame.display.update()

    def show_leaderboard(self, leaderboard):
        while True:
            self.screen.fill(BLACK)
            title = self.big_font.render("Leaderboard", True, GREEN)
            self.screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, 50))

            for i, entry in enumerate(leaderboard):
                text = self.font.render(f"{i+1}. {entry['name']} - {entry['score']}", True, WHITE)
                self.screen.blit(text, (200, 130 + i * 40))

            prompt = self.small_font.render("Press ESC to return", True, GRAY)
            self.screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, SCREEN_HEIGHT - 60))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
