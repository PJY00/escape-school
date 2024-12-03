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
planet_color = (128, 0, 128)  # 보라색

# 게임 변수
PLANET_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # 행성 중심 좌표
ORBIT_RADIUS = 250  # 공전 반지름
star_speed = 2  # 별의 회전 속도
star_color_index = 0  # 별의 색상 인덱스
direction_changed = False  # 회전 방향이 변경되었는지 확인
MIN_ORB_DISTANCE_FROM_STAR = 120  # 장애물이 플레이어 별과 떨어져 있어야 하는 최소 거리
MIN_DISTANCE_BETWEEN_ORBS = 80  # 장애물 간 최소 거리

# 원 클래스 (공전 궤도 상의 장애물)
class Orb:
    def __init__(self, star_position, existing_positions):
        self.radius = 10
        max_attempts = 100  # 장애물 생성 시도 제한
        attempts = 0

        while attempts < max_attempts:
            self.angle = random.uniform(0, 360)
            self.position = self.calculate_position()

            # 별과의 거리 계산
            distance_to_star = math.hypot(self.position[0] - star_position[0], self.position[1] - star_position[1])

            # 기존 장애물들과의 거리 계산
            valid_distance = all(
                math.hypot(self.position[0] - pos[0], self.position[1] - pos[1]) >= MIN_DISTANCE_BETWEEN_ORBS
                for pos in existing_positions
            )

            # 조건: 별과 거리, 장애물 간 거리 확인
            if distance_to_star >= MIN_ORB_DISTANCE_FROM_STAR and valid_distance:
                break

            attempts += 1

        # 조건을 만족하지 못하면 기본 위치로 생성
        if attempts == max_attempts:
            print("Warning: Could not place orb with valid spacing. Placing orb at fallback position.")
            self.position = PLANET_CENTER[0] + ORBIT_RADIUS, PLANET_CENTER[1]

        self.color = random.choice(COLORS)

    def calculate_position(self):
        x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
        y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
        return int(x), int(y)

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


# 플레이어 별 클래스
class Star:
    def __init__(self):
        self.color = COLORS[star_color_index]
        self.radius = 13
        self.angle = 0
        self.update_position()

    def update_position(self):
        x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
        y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
        self.position = int(x), int(y)

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


# 장애물 생성 함수
def create_orbs(num_orbs, star_position):
    orbs = []
    existing_positions = []
    for _ in range(num_orbs):
        orb = Orb(star_position, existing_positions)
        orbs.append(orb)
        existing_positions.append(orb.position)
    return orbs


# 성공 함수
def success():
    font = pygame.font.Font(None, 72)
    text = font.render("Success!", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


# 게임 종료 함수
def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()


# 초기화
star = Star()
orbs = create_orbs(2, star.position)  # 처음에 두 개의 장애물 생성
clock = pygame.time.Clock()
score = 0

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

    # 별의 위치 업데이트
    star.angle = (star.angle + star_speed) % 360
    star.update_position()

    # 방향 전환 조건
    if score == 10 and not direction_changed:
        star_speed = -star_speed  
        direction_changed = True 
    if score ==20  and direction_changed:
        star_speed = -star_speed
        direction_changed = False 

    # 행성(중심 원) 그리기
    pygame.draw.circle(screen, planet_color, PLANET_CENTER, 140)  # 중심 원 반지름 140, 색상 보라색
    pygame.draw.circle(screen, WHITE, PLANET_CENTER, ORBIT_RADIUS, 1)

    # 장애물(원) 처리
    for orb in orbs[:]:
        orb.draw()
        distance = math.hypot(orb.position[0] - star.position[0], orb.position[1] - star.position[1])
        if distance < orb.radius + star.radius:
            if orb.color == star.color:
                score += 1
                orbs.remove(orb)
            else:
                game_over()

    # 점수 조건 체크
    if score >= 25:
        success()

    # 새로운 장애물 생성
    if len(orbs) == 0:
        orbs = create_orbs(random.randint(2, 3), star.position)

    # 별 그리기
    star.draw()

    # 점수 표시
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(30)
