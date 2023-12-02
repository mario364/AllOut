import pygame.sprite

from mobs import Mob
from player import *


def newmob(sprites: pygame.sprite.Group, mobs: pygame.sprite.Sprite):
    m = Mob()
    m2 = Mob()
    sprites.add(m)
    mobs.add(m)
    sprites.add(m2)
    mobs.add(m2)


def coollide_player(hero: Player, mobs, flag: bool):
    collisons = pygame.sprite.spritecollide(player, mobs, flag)
    for hit in collisons:
        hero.hp -= hit.damage
        if hero.hp <= 0:
            return False
        else:
            return True

def more_mob(start_time):
   pass
   # for i in range()




