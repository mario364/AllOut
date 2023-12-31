# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os
from mobs import Boss
from player import Player




WIDTH = 800  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 30

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно с нашими параметрами
pygame.display.set_caption('My Game')  # Название окна


clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()  # создание группы спрайтов в игре
boss = Boss()
player = Player(200, 200)
all_sprites.add(boss)
all_sprites.add(player)



# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    boss.move(player.move_direction)
    # Обновление
    all_sprites.update()  # добавим группу целиком в цикл
    # Визуализация
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
