import pygame
import sys
import random
import math

# 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Orbit Game")

# 색상 정의
COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]  # 빨강, 파랑, 노랑
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 게임 변수
PLANET_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # 행성 중심 좌표
ORBIT_RADIUS = 250  # 공전 반지름
star_speed = 2  # 별이 회전하는 속도
star_color_index = 0  # 별의 색상 인덱스
passed_orbs = 0  # 통과한 원의 개수

# 원 클래스 (공전 궤도 상의 장애물)
class Orb:
    def __init__(self, existing_angles):
        self.radius = 20
        self.color = random.choice(COLORS)
        while True:
            self.angle = random.uniform(0, 360)
            if all(abs(self.angle - angle) > 40 for angle in existing_angles):  # 최소 40도 간격
                break
        self.position = self.calculate_position()

    def calculate_position(self):
        x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
        y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
        return (int(x), int(y))

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# 플레이어 별 클래스
class Star:
    def __init__(self):
        self.color = COLORS[star_color_index]
        self.radius = 10
        self.angle = 0
        self.update_position()

    def update_position(self):
        x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
        y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
        self.position = (int(x), int(y))

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# 초기화
star = Star()
existing_angles = []
orbs = [Orb(existing_angles) for _ in range(3)]
for orb in orbs:
    existing_angles.append(orb.angle)
clock = pygame.time.Clock()
score = 0

# 게임 종료 함수
def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# 메인 게임 루프
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                star_color_index = (star_color_index + 1) % len(COLORS)
                star.color = COLORS[star_color_index]

    