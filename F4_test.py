import pygame
import sys
from F4_story import F4_story 
from shooter import run_game

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
TRANSPARENT_BLACK = (0, 0, 0, 150)  # 반투명 검정색 (RGBA)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("클릭 후 텍스트 출력")
    clock = pygame.time.Clock()

    # 폰트 설정
    font_path = 'NEODGM_CODE.TTF'
    font = pygame.font.Font(font_path, 20)

    # 사각형 버튼 정의
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

    # 텍스트 상태 변수
    texts = [
        "첫 번째 메시지입니다.",
        "두 번째 메시지입니다.",
        "세 번째 메시지입니다. 텍스트가 끝났습니다!"
    ]
    current_text_index = 0  # 현재 표시할 텍스트 인덱스
    display_text = ""  # 현재 표시 중인 텍스트
    text_visible = False  # 텍스트 출력 상태

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 버튼 클릭 시 텍스트 출력 활성화
                if event.button == 1 and button_rect.collidepoint(event.pos):
                    if not text_visible:
                        text_visible = True
                        display_text = texts[current_text_index]

            elif event.type == pygame.KEYDOWN:
                # Enter 키로 다음 텍스트로 넘어가기
                if event.key == pygame.K_RETURN and text_visible:
                    current_text_index += 1
                    if current_text_index < len(texts):
                        display_text = texts[current_text_index]
                    else:
                        text_visible = False  # 모든 텍스트가 끝나면 출력 비활성화
                        running = False  # 루프 종료

        # 화면 렌더링
        screen.fill(WHITE)

        # 버튼 렌더링
        pygame.draw.rect(screen, BLUE, button_rect)

        # 텍스트 렌더링
        if text_visible:
            # 반투명 텍스트 상자 생성
            text_box = pygame.Surface((WIDTH, 200), pygame.SRCALPHA)
            text_box.fill(TRANSPARENT_BLACK)
            screen.blit(text_box, (0, HEIGHT - 200))  # 하단에 반투명 상자 표시
            text_surface = font.render(display_text, True, WHITE)
            screen.blit(text_surface, (50, HEIGHT - 180))  # 상자 위에 텍스트 표시

        pygame.display.flip()
        clock.tick(60)
        
    # 텍스트 완료 후 다른 모듈 실행
    run_game()
    F4_story()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()