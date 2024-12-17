import pygame
import sys
from F4_main import F4_main
from F3_main import F3_main
from F2_main import F2_main
from F1_main import F1_main
from BG_elv import elv_game

def run_load():
    pygame.init()

    WIDTH, HEIGHT = 1200, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # 창 크기 변경 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    pygame.display.set_caption("Escape School")

    BLACK = (0, 0, 0)

    font_path = 'neodgm_code.ttf'  # 폰트 파일 경로
    font_middle = pygame.font.Font(font_path, 48)  # 폰트 크기 48로 설정
    font_small = pygame.font.Font(font_path, 30)  # 폰트 크기 48로 설정

    # 텍스트 렌더링
    title_name = font_middle.render("불러오기", True, (255, 255, 255))  # 빨간색
    F4_load = font_small.render("4층", True, (255, 255, 255))  # 초록색
    F3_load = font_small.render("3층", True, (255, 255, 255))  # 파란색
    F2_load = font_small.render("2층", True, (255, 255, 255))  # 노란색
    F1_load = font_small.render("1층", True, (255, 255, 255))  # 노란색

    # 텍스트 위치 설정
    title_name_rect = title_name.get_rect(center=(WIDTH // 2, HEIGHT * 1 // 5))  # 상단 중앙
    F4_load_rect = F4_load.get_rect(center=(WIDTH // 2, HEIGHT * 4 // 10))  # 화면 중앙
    F3_load_rect = F3_load.get_rect(center=(WIDTH // 2, HEIGHT * 5 // 10))  # 하단 3/4 지점
    F2_load_rect = F2_load.get_rect(center=(WIDTH // 2, HEIGHT * 6 // 10))  # 하단 4/5 지점
    F1_load_rect = F1_load.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 10))

    # 클릭 이벤트 함수
    def handle_click(pos):
        if F4_load_rect.collidepoint(pos):
            F4_main()
            elv_game()
            F3_main()
            elv_game()
            F2_main()
            elv_game()
            F1_main()
        elif F3_load_rect.collidepoint(pos):
            F3_main()
            elv_game()
            F2_main()
            elv_game()
            F1_main()
        elif F2_load_rect.collidepoint(pos):
            F2_main()
            elv_game()
            F1_main()
        elif F1_load_rect.collidepoint(pos):
            F1_main()

    # 화면 업데이트 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼 클릭 이벤트
                if event.button == 1:  # 왼쪽 마우스 버튼
                    handle_click(event.pos)  # 클릭 위치를 전달하여 처리

            # 창 크기 변경 이벤트 처리
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
        screen.fill(BLACK)

        # 텍스트 화면에 그리기
        screen.blit(title_name, title_name_rect)
        screen.blit(F4_load, F4_load_rect)
        screen.blit(F3_load, F3_load_rect)
        screen.blit(F2_load, F2_load_rect)
        screen.blit(F1_load, F1_load_rect)

        # 화면 업데이트
        pygame.display.flip()  # 한 번만 호출