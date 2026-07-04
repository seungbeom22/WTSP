import pygame
import sys

# 설정
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # 빨, 초, 파, 노
FPS = 60

# 병 클래스
class Bottle:
    def __init__(self, x, y, capacity=4):
        self.rect = pygame.Rect(x, y, 60, 200)
        self.water = []  # 아래부터 위로 색상 저장
        self.capacity = capacity

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2)
        for i, color in enumerate(self.water):
            pygame.draw.rect(screen, color, (self.rect.x + 5, self.rect.y + 195 - (i * 45), 50, 40))

    def pour_to(self, other):
        if not self.water or other.is_full():
            return False
        if other.water and other.water[-1] != self.water[-1]:
            return False
        
        color = self.water.pop()
        other.water.append(color)
        return True

    def is_full(self):
        return len(self.water) >= self.capacity

# 게임 실행
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bottles = [Bottle(100 + i * 150, 200) for i in range(4)]
bottles[0].water = [COLORS[0], COLORS[1], COLORS[0], COLORS[1]] # 초기 상태
selected_bottle = None

while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for b in bottles:
                if b.rect.collidepoint(pos):
                    if selected_bottle is None:
                        selected_bottle = b
                    else:
                        selected_bottle.pour_to(b)
                        selected_bottle = None

    for b in bottles:
        b.draw(screen)
    
    pygame.display.flip()
