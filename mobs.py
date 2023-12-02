import pygame
from const import *
from random import randrange, randint


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = randint(20, 35)
        self.damage = randrange(15, 31)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(WIDTH - self.rect.width)
        self.rect.y = randrange(-100, -40)
        self.speedy = randrange(1, 8)
        self.speedx = randrange(-3, 3)
        self.radius = int(self.rect.width * .85 / 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = randrange(WIDTH - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speedy = randrange(1, 8)
            self.speedx = randrange(-3, 3)
