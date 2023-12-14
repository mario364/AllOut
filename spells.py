import pygame
from random import randint

import const
from const import YELLOW


class GreenSpell(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.damage = randint(51, 80)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()


class RedSpell(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.damage = randint(60, 80)
        self.image = pygame.Surface((50, 50))
        self.image.fill(const.PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()