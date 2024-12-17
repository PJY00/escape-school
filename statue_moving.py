import pygame
import random
from pygame.locals import *

# 초기화
pygame.init()

# 화면 크기와 색상 설정
WIDTH, HEIGHT = 1200, 700
WHITE = (255, 255, 255)

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("동상 몰래 움직이기")

# 이미지 로드 및 크기 조정
background_image = pygame.image.load("Assets/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

statue_image = pygame.image.load("Assets/statue.png")
statue_image = pygame.transform.scale(statue_image, (110, 220))

player_image = pygame.image.load("Assets/player.png")
player_image = pygame.transform.scale(player_image, (100, 120))

# 하트 이미지 로드 및 크기 조정
full_heart = pygame.image.load("Assets/full_heart.png")
full_heart = pygame.transform.scale(full_heart, (50, 50))

empty_heart = pygame.image.load("Assets/empty_heart.png")
empty_heart = pygame.transform.scale(empty_heart, (50, 50))

# 동상 클래스
class Statue:
    def __init__(self, pos):
        self.image = statue_image
        self.rect = self.image.get_rect(topleft=pos)
        self.state = "closed"
        self.last_switch_time = pygame.time.get_ticks()

    def update(self):
        # 랜덤 상태 변경 (2초마다)
        if pygame.time.get_ticks() - self.last_switch_time > 2000:
            self.state = random.choice(["open", "closed"])
            self.last_switch_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

        # 테두리 출력
        if self.state == "open":
            pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # 빨간 테두리
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)  # 초록 테두리

# 플레이어 클래스
class Player:
    def __init__(self, pos):
        self.image = player_image
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.is_moving = False
        self.lives = 3  # 라이프 추가
        self.last_life_loss_time = 0  # 라이프 소진 시간 기록

    def update(self, keys):
        self.is_moving = False
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.is_moving = True

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def lose_life(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_life_loss_time > 1000:  # 1초 딜레이
            self.lives -= 1
            self.last_life_loss_time = current_time  # 마지막 라이프 소진 시간 갱신

# 게임 초기화
def init_game():
    statue = Statue((50, HEIGHT - 220))
    player = Player((WIDTH - 200, HEIGHT - 120))
    clock = pygame.time.Clock()
    return statue, player, clock

# 라이프 그리기 함수
def draw_lives(screen, lives):
    for i in range(3):  # 최대 3개의 하트 표시
        x = 10 + i * 60  # 하트 간격
        y = 10
        if i < lives:
            screen.blit(full_heart, (x, y))  # 남은 라이프
        else:
            screen.blit(empty_heart, (x, y))  # 소진된 라이프

# 게임 로직
def run_game():
    statue, player, clock = init_game()
    running = True
    success = False
    
    while running:
        screen.blit(background_image, (0, 0))

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
            player.lose_life()  # 라이프 감소
            if player.lives <= 0:
                running = False

        if player.rect.colliderect(statue.rect):
            success = True
            running = False

        # 그리기
        statue.draw(screen)
        player.draw(screen)
        draw_lives(screen, player.lives)  # 라이프 그리기

        pygame.display.flip()
        clock.tick(30)

    # 결과 화면
    show_result(player.lives, success)

def show_result(lives, success):
    screen.fill(WHITE)
    FONT = pygame.font.Font("NEODGM_CODE.TTF", 50)  # 폰트 변경
   
    if lives <= 0:
        result_text = FONT.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(result_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        return -1
    elif success:
        result_text = FONT.render("SUCCESS!", True, (0, 255, 0))
        screen.blit(result_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        return 1
    
    pygame.display.flip()
