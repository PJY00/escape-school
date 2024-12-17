import pygame
import random

def run_game():
    # 화면 크기 설정
    WIDTH = 1200
    HEIGHT = 700
    FPS = 60

    # 색상 정의
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    # pygame 초기화
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shooter!")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # 점수 변수
    score = 0

    # 스프라이트 그룹 및 클래스 정의
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 40))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((30, 40))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)
            self.speedx = random.randrange(-3, 3)

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 4)

        def shoot(self):
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((10, 10))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.bottom = y
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()

    class EnemyBullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((10, 10))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.top = y
            self.speedy = 5

        def update(self):
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT:
                self.kill()

    # 그룹 생성
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()

    # 플레이어 생성
    player = Player()
    all_sprites.add(player)

    # 적 생성
    for _ in range(8):
        mob = Mob()
        all_sprites.add(mob)
        mobs.add(mob)

    # 게임 루프
    running = True
    last_shoot_time = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # 업데이트
        all_sprites.update()

        # 충돌 처리
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 10
            mob = Mob()
            all_sprites.add(mob)
            mobs.add(mob)
            
        if score >= 300:
            print("실패!")
            return 1

        if pygame.sprite.spritecollide(player, enemy_bullets, False) or pygame.sprite.spritecollide(player, mobs, False):
            return -1

        # 랜덤으로 3개의 적만 총알 발사
        current_time = pygame.time.get_ticks()
        if current_time - last_shoot_time > 2000:  # 2초 간격
            shooting_mobs = random.sample(mobs.sprites(), min(5, len(mobs)))
            for mob in shooting_mobs:
                mob.shoot()
            last_shoot_time = current_time

        # 화면 렌더링
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
