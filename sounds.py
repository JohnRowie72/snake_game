import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.eat_sound = pygame.mixer.Sound("assets/eat.wav")
        self.game_over_sound = pygame.mixer.Sound("assets/game_over.wav")
        self.eat_sound.set_volume(1.0)
        self.game_over_sound.set_volume(0.7)
        self.bg_music = "assets/bg_music.mp3"

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.bg_music)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_eat(self):
        self.eat_sound.play()

    def play_game_over(self):
        self.game_over_sound.play()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
