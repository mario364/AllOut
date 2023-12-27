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
pygame.display.set_caption("Следование за спрайтом")

# Класс для спрайта
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Создание спрайтов
player1 = Player(WIDTH // 4, HEIGHT // 2)
player2 = Player(3 * WIDTH // 4, HEIGHT // 2)

# Группа спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2)

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление положения спрайтов
    player1.rect.x += 2  # или другое значение по вашему выбору
    player2.rect.x -= 2  # или другое значение по вашему выбору

    # Отрисовка спрайтов и фона
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты кадров
    clock.tick(60)
