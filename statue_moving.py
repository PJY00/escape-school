import pygame
import random
import sys
from pygame.locals import *

# Initialization
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 1200, 700
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("동상 몰래 움직이기")

# Load images with error handling
def load_image(path, size=None):
    try:
        image = pygame.image.load(path)
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        sys.exit()

# Load images
background_image = load_image("Assets/background.png", (WIDTH, HEIGHT))
statue_image = load_image("Assets/statue.png", (110, 220))
player_image = load_image("Assets/player.png", (100, 120))
full_heart = load_image("Assets/full_heart.png", (50, 50))
empty_heart = load_image("Assets/empty_heart.png", (50, 50))

# Statue class
class Statue:
    def __init__(self, pos):
        self.image = statue_image
        self.rect = self.image.get_rect(topleft=pos)
        self.state = "closed"
        self.last_switch_time = pygame.time.get_ticks()

    def update(self):
        # Switch state every 2 seconds
        if pygame.time.get_ticks() - self.last_switch_time > 2000:
            self.state = random.choice(["open", "closed"])
            self.last_switch_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        # Draw border based on state
        border_color = RED if self.state == "open" else GREEN
        pygame.draw.rect(screen, border_color, self.rect, 2)

# Player class
class Player:
    def __init__(self, pos):
        self.image = player_image
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.is_moving = False
        self.lives = 3
        self.last_life_loss_time = 0

    def update(self, keys):
        self.is_moving = False
        if keys[K_LEFT]:
            self.rect.x -= self.speed
            self.is_moving = True
        if keys[K_RIGHT]:
            self.rect.x += self.speed
            self.is_moving = True
        if keys[K_UP]:
            self.rect.y -= self.speed
            self.is_moving = True
        if keys[K_DOWN]:
            self.rect.y += self.speed
            self.is_moving = True

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def lose_life(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_life_loss_time > 1000:  # 1-second delay
            self.lives -= 1
            self.last_life_loss_time = current_time

# Draw lives
def draw_lives(screen, lives):
    for i in range(3):  # Maximum of 3 hearts
        x = 10 + i * 60
        y = 10
        heart_image = full_heart if i < lives else empty_heart
        screen.blit(heart_image, (x, y))

# Show result
def show_result(lives, success):
    screen.fill(WHITE)
    try:
        FONT = pygame.font.Font("NEODGM_CODE.TTF", 50)
    except FileNotFoundError:
        FONT = pygame.font.Font(None, 50)  # Fallback to default font

    if lives <= 0:
        result_text = FONT.render("GAME OVER!", True, RED)
    elif success:
        result_text = FONT.render("SUCCESS!", True, GREEN)

    screen.blit(result_text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Initialize game
def init_game():
    statue = Statue((50, HEIGHT - 220))
    player = Player((WIDTH - 200, HEIGHT - 120))
    clock = pygame.time.Clock()
    return statue, player, clock

# Main game logic
def run_game():
    statue, player, clock = init_game()
    running = True
    success = False

    while running:
        screen.blit(background_image, (0, 0))

        # Event handling
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update statue and player
        statue.update()
        player.update(keys)

        # Collision detection
        if statue.state == "open" and player.is_moving:
            player.lose_life()
            if player.lives <= 0:
                running = False

        if player.rect.colliderect(statue.rect):
            success = True
            running = False

        # Draw everything
        statue.draw(screen)
        player.draw(screen)
        draw_lives(screen, player.lives)

        pygame.display.flip()
        clock.tick(30)

    # Show result
    show_result(player.lives, success)

