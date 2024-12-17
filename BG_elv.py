import pygame
import random
import sys
from bad_end import bad_end

def elv_game():
    # Initialize pygame
    pygame.init()
    
    # Screen dimensions and colors
    WIDTH, HEIGHT = 1200, 700
    WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)

    # Screen setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Escape School")

    # Load background image
    def load_background_image():
        try:
            background = pygame.image.load("elev.png")
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            return background
        except pygame.error as e:
            print(f"Error loading background image: {e}")
            sys.exit()

    background = load_background_image()

    # Font setup
    font_path = 'NEODGM_CODE.TTF'
    font = pygame.font.Font(font_path, 50)
    small_font = pygame.font.Font(font_path, 40)

    # Function to generate a random math problem
    def generate_problem():
        num1 = random.randint(10, 99)
        num2 = random.randint(1, 99)  # Avoid 0 to prevent division errors
        operator = random.choice(["+", "-", "*", "//"])
        
        if operator == "//":
            answer = num1 // num2
        elif operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        
        problem = f"{num1} {operator} {num2}"
        return problem, answer

    # Clock for controlling FPS
    clock = pygame.time.Clock()

    # Game variables
    user_input = ""
    result_message = ""
    result_color = WHITE
    problem, correct_answer = generate_problem()

    # Main game loop
    running = True
    while running:
        # Render the background
        screen.blit(background, (0, 0))

        # Render the math problem and user input
        problem_text = font.render(f"{problem} =", True, WHITE)
        input_text = font.render(user_input, True, GREEN)
        result_text = small_font.render(result_message, True, result_color)

        # Display the text
        screen.blit(problem_text, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        screen.blit(input_text, (WIDTH // 2 + 100, HEIGHT // 2 - 100))
        screen.blit(result_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Submit answer
                    if user_input.isdigit() or (user_input.startswith("-") and user_input[1:].isdigit()):
                        if int(user_input) == correct_answer:
                            result_message = "정답입니다!"
                            result_color = GREEN
                            running = False  # Exit loop on success
                        else:
                            result_message = "틀렸습니다!"
                            result_color = RED
                            bad_end()
                        user_input = ""
                        problem, correct_answer = generate_problem()
                    else:
                        result_message = "올바른 숫자를 입력하세요!"
                        result_color = RED
                elif event.key == pygame.K_BACKSPACE:  # Remove last character
                    user_input = user_input[:-1]
                elif event.unicode.isdigit() or (event.unicode == "-" and not user_input):  # Add digit or negative sign
                    user_input += event.unicode

        # Control the frame rate
        clock.tick(30)
