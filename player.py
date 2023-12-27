import pygame.image

from const import HEIGHT, WIDTH
from pygame.math import Vector2
from random import randint, choice
from spells import *

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
        images = [r"C:\Python_Projects\AllOut\img\pers\player_blue.png",
                  r"C:\Python_Projects\AllOut\img\pers\player_green.png",
                  r"C:\Python_Projects\AllOut\img\pers\player_red.png"]
        img = pygame.image.load(choice(images))
        self.image = pygame.transform.scale(img, (100, 100))
        # self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.direction = Vector2(1, 0)
        self.move_direction = None


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.move_direction = "left"
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.move_direction = "right"
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.move_direction = "up"
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.move_direction = "down"

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot_bullet(self, sprites: pygame.sprite.Group, bullets: pygame.sprite.Group):
        mouse_pos = pygame.mouse.get_pos()
        self.direction = Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)

        if pygame.mouse.get_pressed():
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction.normalize())
            sprites.add(bullet)
            bullets.add(bullet)

    # def shoot_spell(self, sprites: pygame.sprite.Group, spell_sprite: pygame.sprite.Group):
    #     keys = list(self.spells.keys())
    #     cls = choice(keys)
    #     spell = self.spells[cls](self.rect.centerx, self.rect.top)
    #     sprites.add(spell)
    #     spell_sprite.add(spell)


# Определяем класс Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.damage = randint(30, 50)
        img = pygame.image.load(r"C:\Python_Projects\AllOut\img\atack\bullet.png")
        self.image = pygame.transform.scale(img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7.5
        self.direction = direction
        self.damage = randint(20, 50)

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.rect.left > screen_width or self.rect.right < 0 or self.rect.top > screen_height or self.rect.bottom < 0:
            self.kill()


player = Player()
