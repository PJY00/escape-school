import pygame
import random
from pygame.locals import *
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
DICE_SIZE = (100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def init_game():
    """게임 초기화 함수"""
    pygame.init()
    pygame.display.set_caption("Dice Mini Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def load_resources():
    """리소스 로드 함수"""
    try:
        dice_images = [pygame.image.load(f"diceImage/dice_{i}.png") for i in range(1, 7)]
        dice_images = [pygame.transform.scale(img, DICE_SIZE) for img in dice_images]
        bg = pygame.image.load("diceImage/bg.png")
        
        print()
        print(len(dice_images))
        print()

        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except FileNotFoundError:
        print("리소스 파일이 누락되었습니다. 주사위와 배경 이미지를 확인하세요.")
        pygame.quit()
        exit()
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

def set_text(screen, text, y_offset, color=WHITE, font_size=30):
    """텍스트 출력 함수"""
    font = pygame.font.SysFont("arial", font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
    screen.blit(text_surface, text_rect)

def main():
    """메인 함수"""
    screen = init_game()
    dice_images, bg = load_resources()

    roll_button = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 100, 150, 50, "Roll Dice")

    success_count = 0
    dice_rolls = []
    clock = pygame.time.Clock()
    is_active = True

    while is_active:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))
        set_text(screen, "2개의 주사위를 굴려 합이 10이 되게 만드세요!", 50, WHITE, 24)
        set_text(screen, "3번 성공하면 비밀번호의 한 자리를 드립니다.", 80, WHITE, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                is_active = False

            if roll_button.is_clicked(event):
                dice_rolls = [random.randint(0, 5), random.randint(0, 5)]
                dice_sum = (dice_rolls[0] + 1) + (dice_rolls[1] + 1)
                if dice_sum == 10:
                    success_count += 1

        if dice_rolls:
            screen.blit(dice_images[dice_rolls[0]], (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            screen.blit(dice_images[dice_rolls[1]], (SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50))

        set_text(screen, f"성공 횟수: {success_count}", SCREEN_HEIGHT - 200, WHITE)

        if success_count >= 3:
            set_text(screen, "축하합니다! 비밀번호의 한 자리를 얻었습니다.", SCREEN_HEIGHT // 2 + 100, WHITE, 24)

        roll_button.draw(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
