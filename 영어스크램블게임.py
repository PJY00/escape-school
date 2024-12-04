import pygame
import random

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)


# 폰트 설정
#font = pygame.font.Font(None,
# 텍스트 입력 변수
input_text = ""  
input_box = pygame.Rect(200, 350, 240, 50)
active = False  


# 화면 크기
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

def init_game():
    """게임 초기화 함수"""
    pygame.init()
    pygame.display.set_caption("scrambled game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def load_resources():
    #리소스 로드 함수
    try:
        bg = pygame.image.load("bg.png")
        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except FileNotFoundError:
        print("리소스 파일이 누락되었습니다. 주사위와 배경 이미지를 확인하세요.")
        pygame.quit()
        exit()
    return bg

def draw_underline(screen, word, font, x, y, input_text):
    #밑줄과 입력된 문자 그리기
    spacing = 10  # 밑줄 간격
    start_x = x  # 첫 번째 밑줄 시작 위치

    for i, char in enumerate(word):
        # 밑줄 그리기
        pygame.draw.line(screen, black, (start_x, y), (start_x + 30, y), 2)

        # 입력된 문자 표시
        if i < len(input_text):  # 입력된 문자만 표시
            char_surface = font.render(input_text[i], True, black)
            screen.blit(char_surface, (start_x + 5, y - 40))

        # 다음 밑줄 위치로 이동
        start_x += 30 + spacing


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

# 텍스트 입력 변수
input_text = ""  # 사용자가 입력한 텍스트


def main():
 # 게임 초기화
    screen = init_game()
    bg = load_resources()
    font = pygame.font.Font(None, 74)  # 폰트 정의

    # 입력 상자 관련 변수
    global selected_word, scrambled_word  # 전역 변수 사용 선언
    input_text = ""  # 사용자가 입력한 텍스트
    active = False
    input_box = pygame.Rect(185, 350, 240, 70)  # 입력 박스 위치와 크기
   

    # 게임 리소스
    selected_word = random.choice(words)
    scrambled_word = scramble_word(selected_word)
    input_text = ""
    
    active = False

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True  
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:  
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]  
                    else:
                        input_text += event.unicode 

                    if input_text == selected_word:  # 정답인 경우
                    # 새로운 단어를 선택하고 섞음
                     selected_word = random.choice(words)
                     scrambled_word = scramble_word(selected_word)
                     input_text = ""  # 입력 상자 초기화



       

        # 화면에 단어 표시
        screen.fill(white)  
        screen.blit(bg, (0, 0))
        text = font.render(scrambled_word, True, white)  
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 3 - text.get_height() // 2))  

        

        # 밑줄과 입력된 문자 표시
        draw_underline(screen, selected_word, font, 185, 400, input_text)


        pygame.display.flip() 

    pygame.quit()

if __name__ == "__main__":
    main()