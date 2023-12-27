import pygame
from const import *
from random import randrange, randint, choice
from spells import *

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = randint(10, 150)
        self.damage = randrange(15, 31)

        if self.hp < 30:
            self.image = pygame.image.load(r"img/mobs/skilet.png")
            self.score = 10
        if self.hp >= 30:
            img = pygame.image.load(r"img/mobs/zombi 1.png")
            self.image = pygame.transform.scale(img, (100, 100))
            self.score = 30

        if self.hp > 99:
            img = pygame.image.load(r"img/mobs/zombi2.png")
            self.image = pygame.transform.scale(img, (150, 150))
            self.score = 50


        self.rect = self.image.get_rect()
        self.rect.x = randrange(WIDTH - self.rect.width)
        self.rect.y = randrange(-100, -40)
        self.speedy = randrange(1, 8)
        self.speedx = randrange(-3, 3)
        self.radius = int(self.rect.width * .85 / 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # Появление снова у верхней границы, если выходит за пределы нижней границы
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = randint(0, WIDTH - self.rect.width)
            self.speedx = randint(-5, 5)
            self.speedy = randint(1, 5)

        # Отскок от боковых границ
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT:
            self.speedy = -self.speedy


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 500
        self.damage = 75
        self.x, self.y = 389, 109
        img = pygame.image.load(r"img/mobs/zombi_boss.png")
        self.image = pygame.transform.scale(img, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 2

    def move(self, direction: str):

        if direction == "left":
            self.rect.x -= self.speed
        if direction == "right":
            self.rect.x += self.speed
        if direction == "up":
            self.rect.y -= self.speed
        if direction == "down":
            self.rect.y += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
































# class Rat(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.hp = randint(10, 150)
#         self.damage = randrange(15, 31)
#         if self.hp < 30:
#             self.image = pygame.Surface((10, 10))
#             self.image.fill(GREEN)
#         if self.hp >= 30:
#             self.image = pygame.Surface((40, 40))
#             self.image.fill(RED)
#         if self.hp > 99:
#             self.image = pygame.Surface((100, 100))
#             self.image.fill(BLUE)
#         self.rect = self.image.get_rect()
#         self.rect.x = randrange(WIDTH - self.rect.width)
#         self.rect.y = randrange(-100, -40)
#         self.speedy = randrange(1, 8)
#         self.speedx = randrange(-3, 3)
#         self.radius = int(self.rect.width * .85 / 2)
#
#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#
#         if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
#             self.rect.x = randrange(WIDTH - self.rect.width)
#             self.rect.y = randrange(-100, -40)
#             self.speedy = randrange(1, 8)
#             self.speedx = randrange(-3, 3)



