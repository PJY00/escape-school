import pygame
import random


# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# 단어 리스트
words = ["apple", "cherry", "mango", "orange","kiwi","plum"]

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
    text_x=50
    text_y=8
    screen.blit(score_text,(text_x,text_y))

 #밑줄과 입력 표시
def draw_underline(screen, word, font, x, y, input_text):
    spacing = 25
    line_width = 50
    start_x = x+ 237
    line_y=y+ 30

    for i in range(len(word)):
        pygame.draw.line(screen, black, (start_x, y), (start_x + line_width, y), 5)
        if i < len(input_text):
            char_surface=font.render(input_text[i],True,black)
            char_x = start_x + (line_width - char_surface.get_width()) // 2
            char_y = line_y - 85
            screen.blit(char_surface, (char_x,char_y))
        start_x += line_width + spacing

# 새 단어를 선택하는 함수 (중복 방지)
def select_new_word(words, used_words):
    remaining_words = list(set(words) - set(used_words))
    if not remaining_words: 
        used_words.clear()
        remaining_words = words
    selected_word = random.choice(remaining_words)
    used_words.append(selected_word)
    return selected_word

#새로운 화면 표시(게임 종료 후)
def show_end_screen(screen, font):
    screen.fill(white)
    message = font.render("congratulations! Hint: 2", True, black)
    message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(message, message_rect)
    pygame.display.flip()

# 메인 함수
def run_scram():
    screen = init_game()
    bg = load_resources()

    #폰트설정
    font_path = 'NEODGM_CODE.TTF'
    font = pygame.font.Font(font_path, 60)

    used_words=[]
    selected_word = select_new_word(words, used_words)
    scrambled_word = scramble_word(selected_word)
    input_text = ""
    score = 0
    total_questions = 5
    current_question = 0
    active = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == selected_word:
                        score += 1
                        current_question += 1
                        if current_question == total_questions:
                            show_end_screen(screen,font)
                            pygame.time.delay(5000)
                            running=False

                        else:
                            selected_word = random.choice(words)
                            scrambled_word = scramble_word(selected_word)
                            input_text = ""
                else:
                    if len(input_text) < len(selected_word):
                        input_text += event.unicode

        screen.fill(white)
        screen.blit(bg, (0, 0))

        # 힌트 텍스트 폰트 크기 설정
        hint_font = pygame.font.Font(font_path, 10)  # 기존 폰트 크기보다 작게 설정

        # "올바르게 배열하세요 힌트: 과일" 텍스트 표시
        hint_font = pygame.font.Font(font_path, 30)  # 폰트 크기 30으로 설정 (원하는 숫자로 변경 가능)
        hint_text = hint_font.render("올바르게 배열하세요 힌트: 과일", True, black)
        screen.blit(hint_text, (SCREEN_WIDTH // 2 - hint_text.get_width() // 2, 100))

        #섞인 단어 표시
        scrambled_text = font.render(scrambled_word, True, white)
        screen.blit(scrambled_text, (SCREEN_WIDTH // 2 - scrambled_text.get_width() // 2, 150))
        draw_underline(screen, selected_word, font, 185, 400, input_text)
        score_text = font.render(f" {score}/{total_questions}", True, black)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
