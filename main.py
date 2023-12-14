import pygame

from const import *
from func import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AllOut!')

bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
hero = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(hero)
sprite_mobs = pygame.sprite.Group()
spels = pygame.sprite.Group()
all_sprites.add(spels)
FPS = 60
clock = pygame.time.Clock()

spawn_timer = 10
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, spawn_timer * 1000)
loop_cnt = 0

for i in range(5):
    new_mob(all_sprites, sprite_mobs)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hero.shoot_bullet(all_sprites, bullets)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.shoot_spell(all_sprites, spels)
        if event.type == spawn_event:
            loop_cnt += 1
            for i in range(6):
                new_mob(all_sprites, sprite_mobs)
    if loop_cnt > 3:
        print('ВСЕ!')

    all_sprites.update()

    collide_hero(hero, sprite_mobs)

    collide_damage(sprite_mobs, bullets, all_sprites, spels)
    collide_damage(sprite_mobs, spels, all_sprites, spels)

    if hero.hp <= 0:
        run = False

    screen.fill(BG)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
