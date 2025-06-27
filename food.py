import random
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_BLOCK, RED

class Food:
    def __init__(self):
        self.position = self.spawn()

    def spawn(self):
        grid_columns = SCREEN_WIDTH // SNAKE_BLOCK
        grid_rows = SCREEN_HEIGHT // SNAKE_BLOCK

        spawn_x = random.randint(1, grid_columns - 2) * SNAKE_BLOCK
        spawn_y = random.randint(1, grid_rows - 2) * SNAKE_BLOCK
        return (spawn_x, spawn_y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, SNAKE_BLOCK, SNAKE_BLOCK))