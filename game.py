import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui import UI
from snake import Snake
from food import Food
from modes import GameMode, BlitzMode, InvertedMode
from utilities import load_high_score, save_high_score

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.ui = UI(self.screen)
        self.high_score = load_high_score()
        self.is_paused = False
        self.selected_mode = "normal"

    def run(self):
        self.ui.show_main_menu(self.select_mode, self.open_settings, self.quit_game)

    def select_mode(self):
        self.ui.show_mode_selector(self.start_game)

    def start_game(self, mode):
        self.selected_mode = mode
        while True:
            self.snake = Snake()
            self.food = Food()
            mode_class = {"normal": GameMode, "blitz": BlitzMode, "inverted": InvertedMode}[mode]
            self.mode = mode_class(self)
            score = self.mode.play()
            if score > self.high_score:
                self.high_score = score
                save_high_score(score)
            self.ui.show_game_over(score, self.high_score)

    def open_settings(self):
        self.ui.show_settings()
        self.run()

    def quit_game(self):
        pygame.quit()
        exit()