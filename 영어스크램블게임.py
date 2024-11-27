import pygame
import random

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("English Scramble Game")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 폰트 설정
font = pygame.font.Font(None, 74)

# 단어 리스트
words = ["apple", "cherry", "melon", "orange", "grape"]

# 단어 섞기 함수
def scramble_word(word):
    word_list = list(word)  # 단어를 문자 리스트로 변환
    random.shuffle(word_list)  # 리스트의 순서를 섞음
    return " ".join(word_list)  # 공백으로 연결된 문자열 반환

# 게임 변수
selected_word = random.choice(words)  # 랜덤 단어 선택
scrambled_word = scramble_word(selected_word)  # 섞은 단어 생성

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False

    # 화면에 단어 표시
    screen.fill(white)  # 화면 배경 채우기
    text = font.render(scrambled_word, True, black)  # 텍스트 렌더링
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))  # 화면 중앙에 출력

    pygame.display.flip()  # 화면 업데이트

pygame.quit()
