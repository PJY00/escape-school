import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("비밀번호를 입력하시오.")

# 폰트 설정
font_path = 'NEODGM_CODE.TTF'  # 폰트 파일 경로
font = pygame.font.Font(font_path, 35)  # 폰트 크기 36으로 설정
small_font=pygame.font.Font(font_path,25)

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)


# 비밀번호 입력 초기화
password = ""
max_length = 5  # 비밀번호 최대 길이
correct_password="13245"
input_box = pygame.Rect(WIDTH // 2 - 250, HEIGHT // 2 - 30, 500, 120)


# 게임 루프
running = True
input_complete = False
game_passed=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # 키보드 입력 처리
        if event.type == pygame.KEYDOWN and not input_complete:
            if event.key == pygame.K_RETURN:  # 엔터키 입력 시 완료
                input_complete = True
                if password==correct_password:
                    game_passed=True
            elif event.key == pygame.K_BACKSPACE:  # 백스페이스 처리
                password = password[:-1]
            elif len(password) < max_length and event.unicode.isdigit():  # 최대 길이만큼 입력
                password += event.unicode  # 입력된 문자 추가
    
    # 화면 색상 채우기
    screen.fill(WHITE)

    # 텍스트 표시
    if not input_complete:
        prompt_text = font.render("비밀번호를 입력하시오 (숫자 5자리):", True, BLACK)
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, 100))
        
        pygame.draw.rect(screen, GRAY, input_box, border_radius=10)
        text_surface = font.render(password, True, BLACK)
        text_x = input_box.x + (input_box.width - text_surface.get_width()) // 2
        text_y = input_box.y + (input_box.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

        pygame.draw.rect(screen, BLACK, input_box, 3, border_radius=10)  # 조금 더 지정

    elif game_passed:
        success_text = font.render("문이 열립니다", True, BLACK)
        screen.blit(success_text, (WIDTH // 2 - success_text.get_width() // 2, HEIGHT // 2 - 30))
    else:
        failure_text = font.render("다시 시도하세요", True, RED)
        screen.blit(failure_text, (WIDTH // 2 - failure_text.get_width() // 2, HEIGHT // 2 - 80))
    # 화면 업데이트
    pygame.display.flip()
