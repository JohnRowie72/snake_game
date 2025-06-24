import pygame
from config import GREEN, SNAKE_BLOCK

class Snake:
    def __init__(self):
        self.body = [(100, 50), (80, 50), (60, 50)]
        self.direction = 'RIGHT'
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            head_y -= SNAKE_BLOCK
        elif self.direction == 'DOWN':
            head_y += SNAKE_BLOCK
        elif self.direction == 'LEFT':
            head_x -= SNAKE_BLOCK
        elif self.direction == 'RIGHT':
            head_x += SNAKE_BLOCK

        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, SNAKE_BLOCK, SNAKE_BLOCK))

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key == pygame.K_DOWN and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key == pygame.K_LEFT and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key == pygame.K_RIGHT and self.direction != 'LEFT':
            self.direction = 'RIGHT'