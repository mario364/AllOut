import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Появление нового спрайта")

# Класс для спрайта
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Группа спрайтов
all_sprites = pygame.sprite.Group()

# Создание первого спрайта
player1 = Player(WIDTH // 4, HEIGHT // 2)
all_sprites.add(player1)

# Основной игровой цикл
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка спрайтов и фона
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Проверка времени прошедшего с начала игры
    current_time = pygame.time.get_ticks()
    if current_time - start_time > 30000:  # 30 секунд (в миллисекундах)
        # Создание нового спрайта через 30 секунд
        player2 = Player(3 * WIDTH // 4, HEIGHT // 2)
        all_sprites.add(player2)
        start_time = current_time  # Сброс времени

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты кадров
    clock.tick(60)
