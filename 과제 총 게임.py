import pygame
import random

# 화면 크기 설정
WIDTH = 480
HEIGHT = 600
FPS = 60

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# pygame 초기화
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 게임 화면 크기 설정
pygame.display.set_caption("Shmup!")  # 창 제목 설정
clock = pygame.time.Clock()  # 게임 루프 속도를 설정

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))  # 플레이어 크기 설정
        self.image.fill(GREEN)  # 플레이어 색상 설정
        self.rect = self.image.get_rect()  # 플레이어의 위치와 크기 설정
        self.rect.centerx = WIDTH / 2  # 플레이어의 초기 X 위치는 화면 중앙
        self.rect.bottom = HEIGHT - 10  # 플레이어의 초기 Y 위치는 화면 하단에서 10px 위
        self.speedx = 0  # 플레이어의 X 속도 초기화

    def update(self):
        self.speedx = 0  # 매 프레임마다 속도를 0으로 설정
        keystate = pygame.key.get_pressed()  # 현재 눌린 키를 가져옴
        if keystate[pygame.K_LEFT]:  # 왼쪽 화살표 키가 눌리면
            self.speedx = -8  # 왼쪽으로 이동
        if keystate[pygame.K_RIGHT]:  # 오른쪽 화살표 키가 눌리면
            self.speedx = 8  # 오른쪽으로 이동
        self.rect.x += self.speedx  # X 위치 갱신
        if self.rect.right > WIDTH:  # 화면을 벗어나지 않도록 조정
            self.rect.right = WIDTH
        if self.rect.left < 0:  # 화면을 벗어나지 않도록 조정
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)  # 플레이어의 위치에서 총알 생성
        all_sprites.add(bullet)  # 총알을 모든 스프라이트 그룹에 추가
        bullets.add(bullet)  # 총알을 총알 그룹에 추가

# 적 클래스
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))  # 적 크기 설정
        self.image.fill(RED)  # 적 색상 설정
        self.rect = self.image.get_rect()  # 적의 위치와 크기 설정
        self.rect.x = random.randrange(WIDTH - self.rect.width)  # 적의 X 위치 랜덤 설정
        self.rect.y = random.randrange(-100, -40)  # 적의 Y 위치 랜덤 설정 (화면 위에서 출발)
        self.speedy = random.randrange(1, 8)  # Y 속도 랜덤 설정 (속도는 1부터 8 사이)
        self.speedx = random.randrange(-3, 3)  # X 속도 랜덤 설정 (좌우로 이동)

    def update(self):
        self.rect.x += self.speedx  # X 위치 갱신
        self.rect.y += self.speedy  # Y 위치 갱신
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:  # 화면 밖으로 나가면
            self.rect.x = random.randrange(WIDTH - self.rect.width)  # 새로운 위치로 재설정
            self.rect.y = random.randrange(-100, -40)  # 화면 위쪽에서 다시 생성
            self.speedy = random.randrange(1, 8)  # 새로운 속도 설정

# 총알 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))  # 총알 크기 설정
        self.image.fill(YELLOW)  # 총알 색상 설정
        self.rect = self.image.get_rect()  # 총알의 위치와 크기 설정
        self.rect.bottom = y  # 총알의 Y 위치 설정
        self.rect.centerx = x  # 총알의 X 위치 설정
        self.speedy = -10  # 총알의 Y 속도 (위로 발사)

    def update(self):
        self.rect.y += self.speedy  # Y 위치 갱신 (위로 이동)
        if self.rect.bottom < 0:  # 화면 밖으로 나가면
            self.kill()  # 총알 삭제

# 모든 스프라이트 그룹 및 게임 오브젝트 생성
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group() 
player = Player()  # 플레이어 객체 생성
all_sprites.add(player)  # 모든 스프라이트 그룹에 플레이어 추가

# 적 생성
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# 게임 루프
running = True
while running:
    clock.tick(FPS)  # FPS에 맞춰 게임 루프 실행
    for event in pygame.event.get():  # 모든 이벤트 처리
        if event.type == pygame.QUIT:  # 창을 닫으면 게임 종료
            running = False
        elif event.type == pygame.KEYDOWN:  # 키가 눌리면
            if event.key == pygame.K_SPACE:  # 스페이스바가 눌리면 총알 발사
                player.shoot()

    all_sprites.update()  # 모든 스프라이트 업데이트

    # 총알과 적의 충돌 처리
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()  # 새로운 적 생성
        all_sprites.add(m)  # 모든 스프라이트 그룹에 추가
        mobs.add(m)  # 적 그룹에 추가

    # 플레이어와 적의 충돌 처리
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:  # 충돌이 발생하면 게임 종료
        running = False

    screen.fill(BLACK)  # 화면을 검정색으로 채움
    all_sprites.draw(screen)  # 모든 스프라이트를 화면에 그리기
    pygame.display.flip()  # 화면 업데이트

# 게임 종료
pygame.quit()
