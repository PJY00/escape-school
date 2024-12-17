import pygame
import sys
from F1_story import F1_story 
from Color_Orbit_Game import run_orbit
from bad_end import bad_end

def F1_test():
    # 화면 크기 설정
    WIDTH, HEIGHT = 1200, 700

    # 색상 정의
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    TRANSPARENT_BLACK = (0, 0, 0, 150)  # 반투명 검정색 (RGBA)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("클릭 후 텍스트 출력")
    clock = pygame.time.Clock()

    # 폰트 설정
    font_path = 'NEODGM_CODE.TTF'
    font = pygame.font.Font(font_path, 20)


    # 버튼 이미지 불러오기
    button_image = pygame.image.load('NPCpixel.png')  # 이미지 파일 경로 설정
    button_image = pygame.transform.scale(button_image, (400, 400))  # 버튼 크기에 맞게 이미지 조정

    # 배경 이미지 불러오기
    def load_background_image():
        try:
            background = pygame.image.load("class4.png")  # 배경 이미지 파일 경로 설정
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # 화면 크기에 맞게 조정
            return background
        except pygame.error as e:
            print(f"Error loading background image: {e}")
            sys.exit()

    # 배경 이미지 로드
    background = load_background_image()

    # 사각형 버튼 정의
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 400)

    # 텍스트 상태 변수
    texts = [
        "게임을 시작합니다.",
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
    result = run_orbit()
    pygame.time.delay(100)
    
    if result == 1:
        print("게임에서 승리했습니다!")
        # 승리 이벤트 실행
        F1_story()
    elif result == -1:
        # 배드엔딩
        bad_end()
    else:
        print("알 수 없는 결과입니다.")
        # 기본 이벤트 실행

    pygame.quit()
    sys.exit()
    