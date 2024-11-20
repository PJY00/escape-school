import pygame
import sys
import random
import math
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Orbit Game")

COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 게임 변수
PLANET_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # 행성 중심 좌표
ORBIT_RADIUS = 250  # 공전 반지름
star_angle = 0  # 별의 초기 각도
star_speed = 2  # 별이 회전하는 속도
star_color_index = 0  # 별의 색상 인덱스
passed_orbs = 0  # 통과한 원의 개수

# 원 클래스 (공전 궤도 상의 장애물)
class Orb:
    def __init__(self):
        self.angle = random.uniform(0, 360) 
        self.color = random.choice(COLORS)  
        self.radius = 20  
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

    def update_position(self):
        x = PLANET_CENTER[0] + ORBIT_RADIUS * math.cos(math.radians(self.angle))
        y = PLANET_CENTER[1] + ORBIT_RADIUS * math.sin(math.radians(self.angle))
        self.position = (int(x), int(y))

    def draw(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

# 초기화
star = Star() 
orbs = [Orb() for _ in range(3)]  
clock = pygame.time.Clock()  
score = 0  

# 게임 종료 함수
def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
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

    # 별의 위치 업데이트
    star.angle = (star.angle + star_speed) % 360
    star.update_position()
    
    # 행성(중심 원) 그리기
    pygame.draw.circle(screen, WHITE, PLANET_CENTER, 30)  # 중심 행성
    pygame.draw.circle(screen, WHITE, PLANET_CENTER, ORBIT_RADIUS, 1)  # 궤도
    
    # 장애물(원) 처리
    for orb in orbs:
        orb.draw()
        distance = math.hypot(orb.position[0] - star.position[0], orb.position[1] - star.position[1])
        if distance < orb.radius + star.radius: 
            if orb.color == star.color:
                score += 1 
                passed_orbs += 1  
                orbs.remove(orb)  
            else:
                game_over()  
    
    # 장애물이 모두 통과되었을 때 새로 생성
    if passed_orbs == 3:
        orbs = [Orb() for _ in range(3)]  
        passed_orbs = 0 

    # 별 그리기
    star.draw()

    # 점수 표시
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(30)
