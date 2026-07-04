import pygame
import random

# 1. 초기화
pygame.init()

# 2. 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Water Sop - 물방울 게임")
clock = pygame.time.Clock()

# 3. 색상 및 변수
BLUE = (0, 100, 255)
WHITE = (255, 255, 255)
drop_x = random.randint(50, 750)
drop_y = 0
speed = 5
score = 0

# 4. 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 물방울 이동
    drop_y += speed
    if drop_y > 600:
        drop_y = 0
        drop_x = random.randint(50, 750)
        speed += 0.5  # 점점 빨라짐

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (drop_x, drop_y), 20)
    
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
