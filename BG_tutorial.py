import pygame
import sys

def run_text():
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
        "어...? 나 잠들었었나?",
        "(낯익은 칠판이 보이며 잠에서 깨어난다.)",
        "몇시지?",
        "11시??? 빨리 나가야겠다.",
        "(엘리베이터를 타기 위해 이동중중)",
        "엘리베이터가 작동하지 않잖아..",
        "다른 곳을 둘러보자",
        "(근처 강의실로 이동중)"
        "강의실 안에 누군가가 있다.",
        "저기 혹시 정문 비밀번호 알고 계세요?",
        "NPC : 저도 비밀번호 전부는 모르는데 한 자리는 알고있어요.",
        "NPC : 게임에서 이기면 알려드릴게요",
    ]

    # 텍스트 출력 상태 변수
    current_text_index = 0  # 현재 텍스트 인덱스
    displayed_text = ""  # 현재까지 화면에 출력된 텍스트
    last_char_time = pygame.time.get_ticks()  # 마지막 글자 출력 시간
    char_delay = 40  # 글자 출력 간격 (밀리초)

    # 고정 좌표 및 여백 설정
    left_margin = 50  # 좌측 여백
    right_margin = WIDTH - 50  # 우측 여백
    line_height = 20  # 줄 간격
    text_y = HEIGHT - (len(texts) * 25) - 30  # 텍스트 시작 y 좌표

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
            # 모든 텍스트가 출력된 경우 루프 종료
            running = False
            continue
        
        # 텍스트를 화면에 렌더링 (줄 바꿈 처리)
        words = displayed_text.split(' ')  # 공백 기준으로 단어 분리
        lines = []  # 줄 목록
        current_line = ""  # 현재 줄
        for word in words:
            test_line = current_line + (word + " ")  # 현재 줄에 단어 추가
            if font.size(test_line)[0] <= right_margin - left_margin:  # 너비가 범위 내에 있으면
                current_line = test_line
            else:
                lines.append(current_line)  # 현재 줄을 줄 목록에 추가
                current_line = word + " "  # 새 줄 시작
        lines.append(current_line)  # 마지막 줄 추가

        # 텍스트를 화면에 렌더링
        y_position = text_y  # y 좌표 초기화
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (left_margin, y_position))  # 좌측 정렬 위치에 출력
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
