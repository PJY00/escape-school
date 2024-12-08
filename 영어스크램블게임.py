import pygame
import random

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# 화면 크기
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600

# 단어 리스트
words = ["apple", "cherry", "mango", "orange", "grape","kiwi","plum"]

# 단어 섞기 함수
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)
    

# 게임 초기화
def init_game():
    pygame.init()
    pygame.display.set_caption("Scrambled Game")
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 배경 설정
def load_resources():
    bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg=pygame.image.load("diceImage/bg.png")
    new_width = int(SCREEN_WIDTH * 1.0)
    new_height = int(SCREEN_HEIGHT * 1.0)
    bg = pygame.transform.scale(bg, (new_width, new_height))
    return bg

# 점수 표시 함수
def draw_score(screen, font, score, total_questions):
   
    # 점수 텍스트
    score_text = font.render(f"{score}/{total_questions}", True, black)
    
    #텍스트 위치
    text_x=10
    text_y=10
    screen.bilt(score_text,(text_x,text_y))

 #밑줄과 입력 표시
def draw_underline(screen, word, font, x, y, input_text):
    spacing = 20
    line_width = 30
    start_x = x

    for i, char in enumerate(word):
        pygame.draw.line(screen, black, (start_x, y), (start_x + line_width, y), 2)
        if i < len(input_text):
           screen.blit(char_surface, (start_x + 8, y - 40))
        start_x += line_width + spacing

# 메인 함수
def main():
    screen = init_game()
    bg = load_resources()
    font = pygame.font.Font(None, 74)

    selected_word = random.choice(words)
    scrambled_word = scramble_word(selected_word)
    input_text = ""
    score = 0
    total_questions = 5
    current_question = 0
    active = False
    input_box = pygame.Rect(185, 350, 240, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == selected_word:
                        score += 1
                        current_question += 1
                        if current_question == total_questions:
                            print(f"게임 종료! ")
                            running = False
                        else:
                            selected_word = random.choice(words)
                            scrambled_word = scramble_word(selected_word)
                            input_text = ""
                else:
                    input_text += event.unicode

        screen.fill(white)
        screen.blit(bg, (0, 0))
        scrambled_text = font.render(scrambled_word, True, white)
        screen.blit(scrambled_text, (SCREEN_WIDTH // 2 - scrambled_text.get_width() // 2, 150))
        draw_underline(screen, selected_word, font, 185, 400, input_text)
        score_text = font.render(f" {score}/{total_questions}", True, black)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
