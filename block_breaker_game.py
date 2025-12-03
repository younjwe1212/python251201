import pygame
import sys
import random
from enum import Enum

# 게임 상수
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_SIZE = 8
BLOCK_WIDTH = 75
BLOCK_HEIGHT = 15
BLOCK_ROWS = 4
BLOCK_COLS = 10

class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    WIN = 3

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 7

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_SIZE * 2, BALL_SIZE * 2)
        self.vel_x = 5
        self.vel_y = -5
        self.speed = 5

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, BALL_SIZE)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # 벽 충돌
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.vel_x = -self.vel_x
        if self.rect.top <= 0:
            self.vel_y = -self.vel_y

    def check_paddle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.vel_y = -self.vel_y
            self.rect.bottom = paddle.rect.top

    def check_block_collision(self, blocks):
        for block in blocks[:]:
            if self.rect.colliderect(block.rect):
                self.vel_y = -self.vel_y
                blocks.remove(block)
                return True
        return False

class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("벽돌깨기 게임")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.state = GameState.PLAYING
        self.score = 0

        # 게임 객체 초기화
        self.paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.blocks = self.create_blocks()

    def create_blocks(self):
        blocks = []
        for row in range(BLOCK_ROWS):
            for col in range(BLOCK_COLS):
                x = col * (BLOCK_WIDTH + 5) + 10
                y = row * (BLOCK_HEIGHT + 5) + 50
                blocks.append(Block(x, y))
        return blocks

    def draw(self):
        self.screen.fill((0, 0, 0))

        # 게임 객체 그리기
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        for block in self.blocks:
            block.draw(self.screen)

        # 점수 표시
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # 게임 상태 메시지
        if self.state == GameState.GAME_OVER:
            game_over_text = self.font.render("GAME OVER! Press R to Restart", True, (255, 0, 0))
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        elif self.state == GameState.WIN:
            win_text = self.font.render("YOU WIN! Press R to Restart", True, (0, 255, 0))
            self.screen.blit(win_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))

        pygame.display.flip()

    def update(self):
        if self.state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            self.paddle.update(keys)
            self.ball.update()

            # 충돌 감지
            self.ball.check_paddle_collision(self.paddle)
            if self.ball.check_block_collision(self.blocks):
                self.score += 10

            # 게임 오버 확인
            if self.ball.rect.top >= SCREEN_HEIGHT:
                self.state = GameState.GAME_OVER

            # 승리 확인
            if len(self.blocks) == 0:
                self.state = GameState.WIN

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.state != GameState.PLAYING:
                    self.__init__()
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()