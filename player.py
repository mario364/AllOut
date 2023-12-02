import pygame
from const import HEIGHT, WIDTH
from pygame.math import Vector2
from random import randint

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
screen_width = WIDTH
screen_height = HEIGHT
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.hp = 150
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.direction = Vector2(1, 0)



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def shoot(self, sprites: pygame.sprite.Group, bullets: pygame.sprite.Group):
            mouse_pos = pygame.mouse.get_pos()
            self.direction = Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)

            if pygame.mouse.get_pressed():
                bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction.normalize())
                sprites.add(bullet)
                bullets.add(bullet)


# Определяем класс Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.damage = randint(10, 25)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7.5
        self.direction = direction
        self.damage = 10

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.rect.left > screen_width or self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0:
            self.kill()

player = Player()