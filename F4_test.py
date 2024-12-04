import pygame
import sys

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
TRANSPARENT_BLACK = (0, 0, 0, 150)  # 반투명 검정색 (RGBA)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("반투명 텍스트 상자")
    clock = pygame.time.Clock()

    # 폰트 설정
    font_path = 'NEODGM_CODE.TTF'
    font = pygame.font.Font(font_path, 30)

    # 사각형 버튼 정의
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

    # 반투명 텍스트 상자 정의
    text_box = pygame.Surface((WIDTH, 100), pygame.SRCALPHA)  # 반투명 박스
    text_box.fill(TRANSPARENT_BLACK)

    # 텍스트 변수
    display_text = ""
    text_visible = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 버튼 클릭 감지
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    display_text = "버튼이 클릭됨"  # 표시할 텍스트
                    text_visible = True  # 텍스트 표시 활성화

        # 화면 렌더링
        screen.fill(WHITE)

        # 버튼 렌더링
        pygame.draw.rect(screen, BLUE, button_rect)

        # 텍스트 상자와 텍스트 렌더링
        if text_visible:
            screen.blit(text_box, (0, HEIGHT - 100))  # 하단에 텍스트 상자 표시
            text_surface = font.render(display_text, True, WHITE)
            screen.blit(text_surface, (50, HEIGHT - 75))  # 텍스트 상자 위에 텍스트 표시

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
