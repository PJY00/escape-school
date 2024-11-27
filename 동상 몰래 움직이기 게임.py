import pygame
import random
from pygame.locals import *

# 초기화
pygame.init()

# 화면 크기와 색상 설정
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("동상 몰래 움직이기")

# 폰트
FONT = pygame.font.Font(None, 50)

# 동상 클래스
class Statue:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 50, 100)
        self.state = "closed"  # 초기 상태: 눈 감음
        self.last_switch_time = pygame.time.get_ticks()

    def update(self):
        # 랜덤 상태 변경 (2초마다)
        if pygame.time.get_ticks() - self.last_switch_time > 2000:
            self.state = random.choice(["open", "closed"])
            self.last_switch_time = pygame.time.get_ticks()

    def draw(self, screen):
        color = RED if self.state == "open" else GREEN
        pygame.draw.rect(screen, color, self.rect)

# 플레이어 클래스
class Player:
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
        self.speed = 5
        self.is_moving = False

    def update(self, keys):
        # 플레이어 이동
        self.is_moving = False
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.is_moving = True

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

# 게임 초기화
def init_game():
    statue = Statue((50, HEIGHT // 2 - 50))
    player = Player((WIDTH - 100, HEIGHT // 2 - 25))
    clock = pygame.time.Clock()
    game_over = False
    success = False

# 게임 로직
def main():
    
    
    running = True
    statue = Statue((50, HEIGHT // 2 - 50))
    player = Player((WIDTH - 100, HEIGHT // 2 - 25))
    clock = pygame.time.Clock()
    game_over = False
    success = False
    
    while running:
        screen.fill(WHITE)

        # 이벤트 처리
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # 동상 상태 업데이트
        statue.update()

        # 플레이어 업데이트
        player.update(keys)

        # 충돌 감지
        if statue.state == "open" and player.is_moving:
            game_over = True
            running = False

        if player.rect.colliderect(statue.rect):
            success = True
            running = False

        # 그리기
        statue.draw(screen)
        player.draw(screen)

        # 동상 상태 텍스트
        state_text = FONT.render(
            "눈 뜸!" if statue.state == "open" else "눈 감음!", True, RED if statue.state == "open" else GREEN
        )
        screen.blit(state_text, (WIDTH // 2 - 100, 50))

        pygame.display.flip()
        clock.tick(30)

    # 결과 화면
    screen.fill(WHITE)
    if game_over:
        result_text = FONT.render("GAME OVER!", True, RED)
    elif success:
        result_text = FONT.render("SUCCESS!", True, GREEN)
    screen.blit(result_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
    pygame.display.flip()
    pygame.time.delay(3000)

    pygame.quit()
    

if __name__ == "__main__":
    main()