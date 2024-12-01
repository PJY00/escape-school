import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

# 창 크기 변경 이벤트 처리
for event in pygame.event.get():
    if event.type == pygame.VIDEORESIZE:
        WIDTH, HEIGHT = event.w, event.h
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Escape School")

WHITE=(255,255,255)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
    
    screen.fill(WHITE)
    pygame.display.flip()
    
    
pygame.quit()      