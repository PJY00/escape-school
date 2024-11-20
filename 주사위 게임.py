import pygame
import random
from pygame.locals import *

def init_game():
    """게임 초기화 함수"""
    pygame.init()
    pygame.display.set_caption("Dice Throw Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def load_resources():
    """리소스 로드 함수"""
    dice_images = [pygame.image.load(f"{i}.png") for i in range(1, NUM_DICES + 1)]
    try:
        bg = pygame.image.load('bg.png')
        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except FileNotFoundError:
        bg = None
    return dice_images, bg

class Button:
    """버튼 클래스"""
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = GRAY

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        font = pygame.font.SysFont("arial", 24)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Dice:
    """주사위 클래스"""
    def __init__(self, image):
        self.image = pygame.transform.scale(image, DICE_SIZE)
        self.x = SCREEN_WIDTH // 2 - DICE_SIZE[0] // 2
        self.y = SCREEN_HEIGHT // 2 - DICE_SIZE[1] // 2

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

def set_text(screen, text, y_offset):
    """텍스트 출력 함수"""
    font = pygame.font.SysFont("arial", 30)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
    screen.blit(text_surface, text_rect)

def main():
    """메인 함수"""
    global SCREEN_WIDTH, SCREEN_HEIGHT, NUM_DICES, DICE_SIZE, WHITE, BLACK, GRAY

    # 전역 변수 초기화
    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
    NUM_DICES = 6
    DICE_SIZE = (100, 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)

    # 초기화 및 리소스 로드
    screen = init_game()
    dice_images, bg = load_resources()
    dices = [Dice(dice_images[i]) for i in range(NUM_DICES)]

    # 버튼 생성
    roll_button = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 100, 150, 50, "Roll Dice")

    # 게임 상태 변수
    is_active = True
    current_dice = random.choice(dices)
    clock = pygame.time.Clock()

    # 게임 루프
    while is_active:
        screen.fill(BLACK)

        # 배경 이미지 출력
        if bg:
            screen.blit(bg, (0, 0))

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == QUIT:
                is_active = False

            # 버튼 클릭 이벤트
            if roll_button.is_clicked(event):
                current_dice = random.choice(dices)

        # 텍스트 출력
        set_text(screen, "Dice Throw Game", 50)

        # 주사위 출력
        current_dice.draw(screen)

        # 버튼 출력
        roll_button.draw(screen)

        # 화면 업데이트
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# 게임 실행
if __name__ == "__main__":
    main()
