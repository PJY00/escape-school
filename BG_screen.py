import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# 창 크기 변경 이벤트 처리
for event in pygame.event.get():
    if event.type == pygame.VIDEORESIZE:
        WIDTH, HEIGHT = event.w, event.h
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption("Escape School")

WHITE = (255, 255, 255)

font_path = 'neodgm_code.ttf'  # 폰트 파일 경로
font_middle = pygame.font.Font(font_path, 48)  # 폰트 크기 48로 설정
font_small = pygame.font.Font(font_path, 30)  # 폰트 크기 48로 설정

# 텍스트 렌더링
game_name = font_middle.render("학교탈출", True, (255, 0, 0))  # 빨간색
start_text = font_small.render("시작하기", True, (0, 255, 0))  # 초록색
save_text = font_small.render("저장하기", True, (0, 0, 255))  # 파란색
load_text = font_small.render("불러오기", True, (255, 255, 0))  # 노란색

    # 텍스트 위치 설정
game_name_rect = game_name.get_rect(center=(WIDTH // 2, HEIGHT // 5))  # 상단 중앙
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT * 6 // 12))  # 화면 중앙
save_text_rect = save_text.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 12))  # 하단 3/4 지점
load_text_rect = load_text.get_rect(center=(WIDTH // 2, HEIGHT * 8 // 12))  # 하단 4/5 지점

# 화면 업데이트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 창 크기 변경 이벤트 처리
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    screen.fill(WHITE)

     # 텍스트 화면에 그리기
    screen.blit(game_name, game_name_rect)
    screen.blit(start_text, start_text_rect)
    screen.blit(save_text, save_text_rect)
    screen.blit(load_text, load_text_rect)

    # 화면 업데이트
    pygame.display.flip()  # 한 번만 호출

pygame.quit()
