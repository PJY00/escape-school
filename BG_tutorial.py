import pygame
import sys

# 화면 크기 설정
WIDTH, HEIGHT = 1200, 700

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 게임 화면 크기 설정
pygame.display.set_caption("타이핑 효과")  # 창 제목 설정
clock = pygame.time.Clock()  # FPS 설정

# 폰트 설정
font_path = 'NEODGM_CODE.TTF'  # 폰트 파일 경로
font = pygame.font.Font(font_path, 20)  # 폰트 크기 36으로 설정

# 텍스트 리스트
texts = [
    "텍스트 출력 테스트",
    "출력 테스트 두번째 줄",
    "출력 테스트 세번째 줄",
    "마지막 줄임. 출력 확인 바람"
]

# 텍스트 출력 상태 변수
current_text_index = 0  # 현재 텍스트 인덱스
displayed_text = ""  # 현재까지 화면에 출력된 텍스트
last_char_time = pygame.time.get_ticks()  # 마지막 글자 출력 시간
char_delay = 100  # 글자 출력 간격 (밀리초)

# 고정 좌표 설정
text_x = 30  # 텍스트 시작 x 좌표
line_height = 50  # 줄 간격
text_y = HEIGHT - (len(texts) * 30) - 40  # 텍스트 시작 y 좌표

# 메인 루프
running = True
while running:
    screen.fill(WHITE)  # 화면 배경 색상 설정

    # 현재 텍스트 렌더링
    if current_text_index < len(texts):
        full_text = texts[current_text_index]  # 현재 텍스트 가져오기

        # 일정 간격마다 한 글자씩 추가
        current_time = pygame.time.get_ticks()
        if current_time - last_char_time > char_delay:
            if len(displayed_text) < len(full_text):  # 아직 전체 텍스트를 출력하지 않은 경우
                displayed_text += full_text[len(displayed_text)]  # 다음 글자 추가
                last_char_time = current_time  # 마지막 글자 출력 시간 갱신
    else:
        # 모든 텍스트가 출력된 후의 처리
        displayed_text = "모든 텍스트가 출력 끝!"

     # 텍스트를 화면에 렌더링
    y_position = text_y  # y 좌표 초기화
    for idx, text in enumerate(displayed_text.split('\n')):  # 여러 줄의 텍스트 처리
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (text_x, y_position))  # 좌측 정렬 위치에 출력
        y_position += line_height  # 다음 줄로 이동

    pygame.display.flip()  # 화면 업데이트

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # 엔터 키 입력 시
                if len(displayed_text) < len(full_text):  
                    # 아직 텍스트가 완전히 출력되지 않았다면 즉시 출력
                    displayed_text = full_text
                else:
                    # 현재 텍스트 출력 완료 시 다음 텍스트로 이동
                    current_text_index += 1  # 다음 텍스트로 이동
                    displayed_text = ""  # 출력된 텍스트 초기화

    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
