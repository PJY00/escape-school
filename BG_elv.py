import pygame
import random
import sys

def start_game():
    # 초기화
    pygame.init()
    
    # 화면 설정
    WIDTH, HEIGHT = 1200, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("랜덤 수식 게임")
    
    font_path = 'NEODGM_CODE.TTF' 
    font = pygame.font.Font(font_path, 50)
    small_font = pygame.font.Font(font_path, 50)
    WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)

    # 랜덤 수식 생성 함수
    def generate_problem():
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        operator = random.choice(["+", "-", "*", "//"])
        
        if operator == "//":
            num2 = random.randint(1, 99)  # 0으로 나누는 오류 방지
            answer = num1 // num2
        elif operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        
        problem = f"{num1} {operator} {num2}"
        return problem, answer

    clock = pygame.time.Clock()
    user_input, result_message, result_color = "", "", WHITE
    
    # 첫 문제 생성
    problem, correct_answer = generate_problem()

    while True:
        screen.fill(BLACK)  # 화면 초기화

        # 문제와 사용자 입력 표시
        problem_text = font.render(f"{problem} =", True, WHITE)
        input_text = font.render(user_input, True, GREEN)
        result_text = small_font.render(result_message, True, result_color)
        
        # 화면에 표시
        screen.blit(problem_text, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        screen.blit(input_text, (WIDTH // 2 + 100, HEIGHT // 2 - 100))
        screen.blit(result_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))
        pygame.display.flip()

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
                        if int(user_input) == correct_answer:
                            result_message, result_color = "정답입니다!", GREEN
                            print(1)
                        else:
                            result_message, result_color = "틀렸습니다!", RED
                            print(-1)
                        user_input = ""
                        problem, correct_answer = generate_problem()
                    else:
                        result_message, result_color = "올바른 숫자를 입력하세요!", RED
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.unicode.isdigit() or (event.unicode == "-" and not user_input):
                    user_input += event.unicode

        clock.tick(30)

if __name__ == "__main__":
    start_game()