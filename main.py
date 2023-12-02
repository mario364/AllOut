
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
FPS = 60
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


for i in range(randint(1, 9)):
    newmob(all_sprites, sprite_mobs)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hero.shoot(all_sprites, bullets)

    all_sprites.update()

    collisions = pygame.sprite.spritecollide(hero, sprite_mobs, True)
    for hit in collisions:
        hero.hp -= hit.damage
        if hero.hp <= 0:
            run = False

    hits = pygame.sprite.groupcollide(sprite_mobs, bullets, True, False)
    for hit in hits:
        newmob(all_sprites, sprite_mobs)

    more_mob(start_time)

    screen.fill(BG)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
