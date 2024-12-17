import pygame
import sys
from BG_tutorial import run_text
from F4_main import F4_main
from F3_main import F3_main
from F2_main import F2_main
from F1_main import F1_main
from BG_elv import elv_game
from BG_saveload import run_load

pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape School")


# 색상 정의
WHITE = (255, 255, 255)
BOX_COLOR = (0, 0, 0)  # 네모 상자의 색상 (검정색)

# 폰트 설정
font_path = 'neodgm_code.ttf'  # 폰트 파일 경로
font_middle = pygame.font.Font(font_path, 48)  # 폰트 크기 48
font_small = pygame.font.Font(font_path, 30)   # 폰트 크기 30

# 텍스트 렌더링
game_name = font_middle.render("학교탈출", True, WHITE) 
start_text = font_small.render("새게임", True, WHITE)   
load_text = font_small.render("불러오기", True, WHITE)  
quit_text = font_small.render("종료하기", True, WHITE)  

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

# 사진 이미지 로드 함수
def load_photo_image():
    try:
        photo_image = pygame.image.load("NPCpixel.png")  # 이미지 파일 경로 (변경 필요)
        photo_image = pygame.transform.scale(photo_image, (200, 200))  # 이미지 크기 키우기
        return photo_image
    except pygame.error as e:
        print(f"Error loading photo image: {e}")
        sys.exit()

# 배경 이미지 로드
background = load_resources()
photo_image = load_photo_image()

# 클릭 이벤트 함수
def handle_click(pos):
    # 텍스트 클릭
    if start_text_rect.collidepoint(pos):
        run_text()
        F4_main()
        elv_game()
        F3_main()
        elv_game()
        F2_main()
        elv_game()
        F1_main()
    elif load_text_rect.collidepoint(pos):
        run_load()  
    elif quit_text_rect.collidepoint(pos):
        print("Quit button clicked!")  
        pygame.quit()
        sys.exit()
    # 사진 클릭 (사진의 위치를 클릭했을 때)
    photo_rect = photo_image.get_rect(topleft=(50, HEIGHT // 3))  # 왼쪽 위치 설정
    if photo_rect.collidepoint(pos):
        print("Photo clicked!")  # 사진 클릭 시 게임 시작
        run_text()
        F4_main()

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

    # 텍스트 주변에 검은색 상자 그리기 (채우기)
    pygame.draw.rect(screen, BOX_COLOR, game_name_rect.inflate(20, 10))
    pygame.draw.rect(screen, BOX_COLOR, start_text_rect.inflate(20, 10))  # '새게임' 텍스트 주변에 검은 상자 채우기
    pygame.draw.rect(screen, BOX_COLOR, load_text_rect.inflate(20, 10))   # '불러오기' 텍스트 주변에 검은 상자 채우기
    pygame.draw.rect(screen, BOX_COLOR, quit_text_rect.inflate(20, 10))   # '종료하기' 텍스트 주변에 검은 상자 채우기

    # 텍스트 화면에 그리기
    screen.blit(game_name, game_name_rect)
    screen.blit(start_text, start_text_rect)
    screen.blit(load_text, load_text_rect)
    screen.blit(quit_text, quit_text_rect)

    # 사진 이미지 화면에 그리기 (왼쪽으로 이동)
    screen.blit(photo_image, (50, HEIGHT // 3))  # 왼쪽으로 50px 이동

    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
