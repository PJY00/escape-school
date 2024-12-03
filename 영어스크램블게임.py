import pygame
import random

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)


# 폰트 설정
#font = pygame.font.Font(None, 74)

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
input_box = pygame.Rect(185, 350, 240, 70)  # 입력 박스 위치와 크기
active = False  # 입력 박스 활성화 여부

def main():
 # 게임 초기화
    screen = init_game()
    bg = load_resources()
    font = pygame.font.Font(None, 74)  # 폰트 정의
   

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
        text = font.render(scrambled_word, True, black)  
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 3 - text.get_height() // 2))  

         # 입력 상자 표시
        pygame.draw.rect(screen, gray if active else black, input_box, 2)
        input_surface = font.render(input_text, True, black)
        screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))
        input_box.w = max(240, input_surface.get_width() + 10)  

        pygame.display.flip() 

    pygame.quit()

if __name__ == "__main__":
    main()