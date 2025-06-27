import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from ui import UI
from snake import Snake
from food import Food
from modes import GameMode, BlitzMode, InvertedMode
from utilities import load_all_highscores, add_score, get_high_score, get_leaderboard
from sounds import SoundManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.ui = UI(self.screen)
        self.is_paused = False
        self.selected_mode = "normal"
        self.sound = SoundManager()
        self.sound.play_music()

    def run(self):
        self.ui.show_main_menu(
            on_start=self.select_mode, 
            on_settings=self.open_settings, 
            on_quit=self.quit_game,
            on_leaderboard=self.show_leaderboard
        )

    def select_mode(self):
        self.ui.show_mode_selector(self.start_game)

    def start_game(self, mode):
        self.selected_mode = mode
        while True:
            self.snake = Snake()
            self.food = Food()
            mode_class = {
                "normal": GameMode, 
                "blitz": BlitzMode, 
                "inverted": InvertedMode
            }[mode]
            self.mode = mode_class(self)
            score = self.mode.play()

            high_score = get_high_score(mode)
            if score > high_score:
                player_name = self.ui.ask_player_name()
                add_score(mode, player_name, score)

            self.ui.show_game_over(score, get_high_score(mode), self.run)

    def open_settings(self):
        self.ui.show_settings()
        self.run()

    def quit_game(self):
        pygame.quit()
        exit()

    def show_leaderboard(self):
        mode = self.ui.ask_leaderboard_mode()
        leaderboard = get_leaderboard(mode)
        self.ui.show_leaderboard(leaderboard)
        self.run()