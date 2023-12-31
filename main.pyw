import pygame

from const import *
from func import *
from player import Player
from mobs import Boss

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AllOut!')

background = pygame.image.load(r"img/maps/maps3.jpg")
background_rect = background.get_rect()


bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
hero = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(hero)
sprite_mobs = pygame.sprite.Group()
boss = Boss()
FPS = 60
clock = pygame.time.Clock()
spawn_timer = 10
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, spawn_timer * 500)
spawn_enable = True
loop_cnt = 0
score = 0

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
        if event.type == spawn_event and spawn_enable:
            loop_cnt += 1
            for i in range(6):
                new_mob(all_sprites, sprite_mobs)
    if loop_cnt > 5:
        print('ВСЕ!')
        spawn_enable = False
        all_sprites.add(boss)
        sprite_mobs.add(boss)
        boss.move(hero.move_direction)


    all_sprites.update()

    collide_hero(hero, sprite_mobs)

    collide_damage(sprite_mobs, bullets)


    if hero.hp <= 0:
        run = False
        print("Смерть")

    screen.fill(BG)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
