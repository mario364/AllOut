import pygame
import sys
from mobs import Mob
# Инициализация Pygame
pygame.init()

# Определение основных параметров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Появление мобов")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)

# Определение параметров моба
mob_radius = 20
mob_color = (255, 0, 0)

# Определение параметров таймера
spawn_timer = 10  # Время в секундах

# Список для хранения мобов
mobs_group = pygame.sprite.Group()
def new_mob():
    m = Mob()
    mobs_group.add(m)

for i in range(8):
    new_mob()

# Основной цикл программы
clock = pygame.time.Clock()
pygame.time.set_timer(event=new_mob, millis=10 * 1000)  # Переводим время в миллисекунды

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(white)
    mobs_group.update()
    mobs_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # 30 кадров в секунду
