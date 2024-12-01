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
font = pygame.font.Font(font_path, 48)  # 폰트 크기 48로 설정

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

    # 텍스트 렌더링
    text = font.render('Hello, Pygame!', True, (255, 0, 0))  # 빨간색 텍스트

    # 화면에 텍스트를 그리기
    screen.fill(WHITE)  # 배경을 흰색으로 설정
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # 텍스트를 화면 중앙에 위치
    screen.blit(text, text_rect)  # 텍스트를 화면에 블릿

    # 화면 업데이트
    pygame.display.flip()  # 한 번만 호출

pygame.quit()
