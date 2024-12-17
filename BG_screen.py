import pygame
import sys
from BG_tutorial import run_text
from F4_main import F4_main

pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape School")

# 색상 정의
WHITE = (255, 255, 255)

# 폰트 설정
font_path = 'neodgm_code.ttf'  # 폰트 파일 경로
font_middle = pygame.font.Font(font_path, 48)  # 폰트 크기 48
font_small = pygame.font.Font(font_path, 30)   # 폰트 크기 30

# 텍스트 렌더링
game_name = font_middle.render("학교탈출", True, (255, 0, 0))  # 빨간색
start_text = font_small.render("새게임", True, (0, 255, 0))   # 초록색
load_text = font_small.render("불러오기", True, (0, 0, 255))  # 파란색
quit_text = font_small.render("종료하기", True, (255, 255, 0))  # 노란색

# 텍스트 위치 설정
game_name_rect = game_name.get_rect(center=(WIDTH // 2, HEIGHT // 5))
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT * 6 // 12))
load_text_rect = load_text.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 12))
quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 8 // 12))

# 배경 이미지 로드 함수
def load_resources():
    try:
        bg = pygame.image.load("main_screen.png")  # 이미지 파일 경로 확인
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))  # 화면 크기에 맞게 조정
        return bg
    except pygame.error as e:
        print(f"Error loading background image: {e}")
        sys.exit()

# 배경 이미지 로드
background = load_resources()

# 클릭 이벤트 함수
def handle_click(pos):
    if start_text_rect.collidepoint(pos):
        run_text()
        F4_main()
    elif load_text_rect.collidepoint(pos):
        print("Load button clicked!")  
    elif quit_text_rect.collidepoint(pos):
        print("Quit button clicked!")  
        pygame.quit()
        sys.exit()

# 화면 업데이트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:  
                handle_click(event.pos)

    # 배경 그리기
    screen.blit(background, (0, 0))

    # 텍스트 화면에 그리기
    screen.blit(game_name, game_name_rect)
    screen.blit(start_text, start_text_rect)
    screen.blit(load_text, load_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
