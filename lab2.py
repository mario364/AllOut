import pygame
import sys
import random
from func import newmob

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Увеличение количества врагов")


# Класс для врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


# Группа врагов
all_enemies = pygame.sprite.Group()
for i in range(2):
    newmob(all_enemies)

# Основной игровой цикл
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
spawn_interval = 30000  # Интервал появления нового врага (30 секунд в миллисекундах)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Проверка времени прошедшего с начала игры
    # current_time = pygame.time.get_ticks()
    # if current_time - start_time > spawn_interval:
    #     # Создание нового врага каждые 30 секунд
    #     for i in range(8):
    #         newmob(all_sprites,all_enemies)

    # Отрисовка врагов и фона
    screen.fill(WHITE)
    all_enemies.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты кадров
    clock.tick(60)
