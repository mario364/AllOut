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
            self.image = pygame.Surface((10, 10))
            self.image.fill(GREEN)
        if self.hp >= 30:
            self.image = pygame.Surface((40, 40))
            self.image.fill(RED)
        if self.hp > 99:
            self.image = pygame.Surface((100, 100))
            self.image.fill(BLUE)

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




class Rat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = randint(10, 150)
        self.damage = randrange(15, 31)
        if self.hp < 30:
            self.image = pygame.Surface((10, 10))
            self.image.fill(GREEN)
        if self.hp >= 30:
            self.image = pygame.Surface((40, 40))
            self.image.fill(RED)
        if self.hp > 99:
            self.image = pygame.Surface((100, 100))
            self.image.fill(BLUE)
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
