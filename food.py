import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_BLOCK

class Food:
    def __init__(self):
        self.position = self.spawn()

    def spawn(self):
        spawn_x = random.randrange(0, SCREEN_WIDTH, SNAKE_BLOCK)
        spawn_y = random.randrange(0, SCREEN_HEIGHT, SNAKE_BLOCK)
        return (spawn_x, spawn_y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, SNAKE_BLOCK, SNAKE_BLOCK))