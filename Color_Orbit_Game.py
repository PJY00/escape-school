import pygame
import sys
import random
import math

def run_orbit():
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
    PLANET_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ORBIT_RADIUS = 250
    COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]  # Red, Blue, Yellow
    PLANET_COLOR = (128, 0, 128)  # Purple
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Orb Class
    class Orb:
        def __init__(self, star_position, existing_positions):
            self.radius = 10
            self.color = random.choice(COLORS)
            self.angle = random.uniform(0, 360)
            self.position = self.calculate_position()
            self.place_orb(star_position, existing_positions)

        def calculate_position(self):
            x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
            y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
            return int(x), int(y)

        def place_orb(self, star_position, existing_positions):
            max_attempts = 100
            for _ in range(max_attempts):
                distance_to_star = math.hypot(self.position[0] - star_position[0], self.position[1] - star_position[1])
                valid_distance = all(
                    math.hypot(self.position[0] - pos[0], self.position[1] - pos[1]) >= 80 for pos in existing_positions
                )
                if distance_to_star >= 200 and valid_distance:  # 별과의 거리 기준을 200으로 조정
                    return
                self.angle = random.uniform(0, 360)
                self.position = self.calculate_position()
            self.position = PLANET_CENTER[0] + ORBIT_RADIUS, PLANET_CENTER[1]

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, self.position, self.radius)

    # Star Class
    class Star:
        def __init__(self):
            self.radius = 13
            self.angle = 0
            self.color_index = 0
            self.color = COLORS[self.color_index]
            self.update_position()

        def update_position(self):
            x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
            y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
            self.position = int(x), int(y)

        def change_color(self):
            self.color_index = (self.color_index + 1) % len(COLORS)
            self.color = COLORS[self.color_index]

        def draw(self, screen):
            pygame.draw.circle(screen, self.color, self.position, self.radius)

    # Utility Functions
    def create_orbs(num_orbs, star_position):
        orbs = []
        existing_positions = []
        for _ in range(num_orbs):
            orb = Orb(star_position, existing_positions)
            orbs.append(orb)
            existing_positions.append(orb.position)
        return orbs

    def success(screen):
        try:
            font = pygame.font.Font("NEODGM_CODE.TTF", 72)
        except FileNotFoundError:
            font = pygame.font.SysFont("arial", 72)
        text = font.render("Success!", True, WHITE)
        screen.fill(BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
        return 1  # Success return

    def game_over(screen, score, lives):
        try:
            font = pygame.font.Font("NEODGM_CODE.TTF", 72)
        except FileNotFoundError:
            font = pygame.font.SysFont("arial", 72)
        text = font.render("Game Over", True, WHITE)
        score_text = pygame.font.Font("NEODGM_CODE.TTF", 48).render(f"Score: {score}", True, WHITE)
        lives_text = pygame.font.Font("NEODGM_CODE.TTF", 48).render(f"Lives: {lives}", True, WHITE)

        screen.fill(BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(lives_text, (SCREEN_WIDTH // 2 - lives_text.get_width() // 2, SCREEN_HEIGHT // 2 + 80))

        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()  # Ensure that the game quits after showing "Game Over"
        return -1  # Game over return

    def show_instructions(screen):
        try:
            font_title = pygame.font.Font("NEODGM_CODE.TTF", 48)
            font_text = pygame.font.Font("NEODGM_CODE.TTF", 28)
        except FileNotFoundError:
            font_title = pygame.font.SysFont("arial", 48)
            font_text = pygame.font.SysFont("arial", 28)

        title_text = font_title.render("Orbit Game Instructions", True, WHITE)
        instructions = [
            "1. 스페이스 바를 눌러 별의 색상을 변경하세요.",
            "2. 별의 색상을 오브의 색상과 맞추면 점수를 얻습니다.",
            "3. 색상이 맞지 않는 오브는 피하세요 - 충돌하면 게임 오버입니다!",
            "4. 10점과 20점에 도달하면 별의 회전 방향이 바뀝니다.",
            "",
            "스페이스 바를 눌러 게임을 시작하세요!",
        ]

        screen.fill(BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        for i, line in enumerate(instructions):
            text = font_text.render(line, True, WHITE)
            screen.blit(text, (50, 200 + i * 40))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False

    def show_countdown(screen):
        try:
            font = pygame.font.Font("NEODGM_CODE.TTF", 72)
        except FileNotFoundError:
            font = pygame.font.SysFont("arial", 72)
        for i in range(3, 0, -1):
            screen.fill(BLACK)
            countdown_text = font.render(str(i), True, WHITE)
            screen.blit(countdown_text, (SCREEN_WIDTH // 2 - countdown_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            pygame.display.flip()
            pygame.time.delay(1000)

    # Main Game Loop
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Orbit Game")

    show_instructions(screen)  # Show instructions before starting the game
    show_countdown(screen)  # Show countdown before the game starts

    star = Star()
    orbs = create_orbs(2, star.position)
    clock = pygame.time.Clock()
    score = 0
    lives = 3  # Set initial lives to 3
    star_speed = 2

    # 플래그 변수
    direction_changed_10 = False
    direction_changed_20 = False

    while True:
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    star.change_color()

        # Update star position
        star.angle = (star.angle + star_speed) % 360
        star.update_position()

        # Change direction based on score
        if score >= 10 and not direction_changed_10:
            star_speed = -star_speed
            direction_changed_10 = True

        if score >= 20 and not direction_changed_20:
            star_speed = -star_speed
            direction_changed_20 = True

        # Draw planet and orbit
        pygame.draw.circle(screen, PLANET_COLOR, PLANET_CENTER, 140)
        pygame.draw.circle(screen, WHITE, PLANET_CENTER, ORBIT_RADIUS, 1)

        # Draw and process orbs
        for orb in orbs[:]:
            orb.draw(screen)
            distance = math.hypot(orb.position[0] - star.position[0], orb.position[1] - star.position[1])
            if distance < orb.radius + star.radius:
                if orb.color == star.color:
                    score += 1
                    orbs.remove(orb)
                else:
                    lives -= 1  # Decrease life if the orb color does not match
                    orbs.remove(orb)
                    if lives == 0:
                        return game_over(screen, score, lives)  # Game over if no lives are left

        # Check for success
        if score >= 25:
            return success(screen)  # Success return

        # Generate new orbs if needed
        if len(orbs) == 0:
            orbs = create_orbs(random.randint(2, 3), star.position)

        # Draw star
        star.draw(screen)

        # Display score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        clock.tick(30)