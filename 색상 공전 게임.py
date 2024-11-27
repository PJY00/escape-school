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

