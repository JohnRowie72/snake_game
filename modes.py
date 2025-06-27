import pygame
import time
from config import BLACK, FPS
from utilities import check_collision

class GameMode:
    def __init__(self, game):
        self.game = game
        self.snake = game.snake
        self.food = game.food
        self.ui = game.ui
        self.clock = game.clock
        self.screen = game.screen
        self.score = 0
        self.speed = FPS

    def play(self):
        running = True
        while running:
            self.clock.tick(self.speed)
            self.handle_events()
            if self.game.is_paused:
                continue

            self.snake.move()
            
            #debug print
            print("Snake Head:", self.snake.body[0], "Food:", self.food.position)

            if check_collision(self.snake.body[0], self.food.position):
                self.food.position = self.food.spawn()
                self.snake.grow = True
                self.score += 10
                self.game.sound.play_eat()
                self.game.sound.play_eat()
                if self.score % 50 == 0:
                    self.speed += 1
            
            if self.snake.check_self_collision() or self.hit_wall():
                break

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.ui.show_score(self.score)
            pygame.display.update()

        self.game.sound.play_game_over()
        self.ui.show_game_over(self.score, self.game.high_score, self.game.run)
        return

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.is_paused = not self.game.is_paused
                else:
                    self.snake.change_direction(event.key)

    def hit_wall(self):
        head_x, head_y = self.snake.body[0]
        return (head_x < 0 or head_x >= self.game.screen.get_width()) or (head_y < 0 or head_y >= self.game.screen.get_height())

class BlitzMode(GameMode):
    def play(self):
        start = time.time()
        duration = 30
        running = True
        self.score = 0

        while running:
            elapsed = time.time() - start
            time_left = duration - elapsed
            if time_left <= 0:
                break

            self.clock.tick(self.speed)
            self.handle_events()
            if self.game.is_paused:
                continue

            self.snake.move()
            if check_collision(self.snake.body[0], self.food.position):
                self.food.position = self.food.spawn()
                self.snake.grow = True
                self.score += 20
                self.game.sound.play_eat()

            if self.snake.check_self_collision() or self.hit_wall():
                running = False

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.ui.show_score(self.score)
            self.ui.show_timer(time_left)
            pygame.display.update()

        self.game.sound.play_game_over()
        self.ui.show_game_over(self.score, self.game.high_score, self.game.run)
        return

class InvertedMode(GameMode):
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                key = event.key
                inv = {
                    pygame.K_UP: pygame.K_DOWN,
                    pygame.K_DOWN: pygame.K_UP,
                    pygame.K_LEFT: pygame.K_RIGHT,
                    pygame.K_RIGHT: pygame.K_LEFT
                }
                self.snake.change_direction(inv.get(key, key))