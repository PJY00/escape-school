import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Escape School")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 폰트 경로 및 설정
font_path = 'neodgm_code.ttf'  # 폰트 파일 경로
font_middle = pygame.font.Font(font_path, 48)
font_small = pygame.font.Font(font_path, 30)
font_text = pygame.font.Font(font_path, 20)

# 메인 화면 텍스트 렌더링
game_name = font_middle.render("학교탈출", True, (255, 0, 0))
start_text = font_small.render("새게임", True, (0, 255, 0))
load_text = font_small.render("불러오기", True, (0, 0, 255))
quit_text = font_small.render("종료하기", True, (255, 255, 0))

# 텍스트 위치 설정
game_name_rect = game_name.get_rect(center=(WIDTH // 2, HEIGHT // 5))
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT * 6 // 12))
load_text_rect = load_text.get_rect(center=(WIDTH // 2, HEIGHT * 7 // 12))
quit_text_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT * 8 // 12))

# 텍스트 출력 상태 변수 (새게임 화면)
texts = [
    "텍스트 출력 테스트",
    "출력 테스트 두번째 줄",
    "출력 테스트 세번째 줄",
    "마지막 줄임. 출력 확인 바람.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec erat sit amet odio feugiat scelerisque.",
    "안녕, 여기는 더미 텍스트야. 출력 테스트를 위해 준비된 문장이지. 긴 문장이 제대로 출력되는지 확인하려고 만들어졌어.",
]
current_text_index = 0
displayed_text = ""
last_char_time = pygame.time.get_ticks()
char_delay = 40
left_margin = 50
right_margin = WIDTH - 50
line_height = 20
text_y = 100

# 게임 상태 (화면 전환)
MAIN_MENU = "main_menu"
TEXT_SCREEN = "text_screen"
game_state = MAIN_MENU

# 클릭 이벤트 처리
def handle_click(pos):
    global game_state
    if start_text_rect.collidepoint(pos):
        print("새게임 버튼 클릭됨!")
        game_state = TEXT_SCREEN  # 텍스트 출력 화면으로 전환
    elif load_text_rect.collidepoint(pos):
        print("불러오기 버튼 클릭됨!")
    elif quit_text_rect.collidepoint(pos):
        print("종료 버튼 클릭됨!")
        pygame.quit()
        sys.exit()

# 텍스트 출력 함수
def render_text_screen():
    global displayed_text, current_text_index, last_char_time

    screen.fill(WHITE)

    if current_text_index < len(texts):
        full_text = texts[current_text_index]
        current_time = pygame.time.get_ticks()
        if current_time - last_char_time > char_delay:
            if len(displayed_text) < len(full_text):
                displayed_text += full_text[len(displayed_text)]
                last_char_time = current_time
    else:
        displayed_text = "모든 텍스트가 출력 끝!"

    words = displayed_text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + (word + " ")
        if font_text.size(test_line)[0] <= right_margin - left_margin:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)

    y_position = text_y
    for line in lines:
        text_surface = font_text.render(line, True, BLACK)
        screen.blit(text_surface, (left_margin, y_position))
        y_position += line_height

# 메인 루프
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and game_state == MAIN_MENU:
                handle_click(event.pos)
        elif event.type == pygame.KEYDOWN and game_state == TEXT_SCREEN:
            if event.key == pygame.K_RETURN:
                if len(displayed_text) < len(texts[current_text_index]):
                    displayed_text = texts[current_text_index]
                else:
                    current_text_index += 1
                    displayed_text = ""
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    if game_state == MAIN_MENU:
        # 메인 메뉴 화면
        screen.blit(game_name, game_name_rect)
        screen.blit(start_text, start_text_rect)
        screen.blit(load_text, load_text_rect)
        screen.blit(quit_text, quit_text_rect)
    elif game_state == TEXT_SCREEN:
        # 텍스트 출력 화면
        render_text_screen()

    pygame.display.flip()

pygame.quit()
sys.exit()
