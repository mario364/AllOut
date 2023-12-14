from random import random, choice
import pygame.sprite

from mobs import Mob
from player import *
from spells import *

def new_mob(sprites: pygame.sprite.Group, mobs: pygame.sprite.Group):
    m = Mob()
    sprites.add(m)
    mobs.add(m)


def collide_hero(player: Player, mob: pygame.sprite.Group):
    collisions = pygame.sprite.spritecollide(player, mob, True)
    for hit in collisions:
        player.hp -= hit.damage


def collide_damage(mob: pygame.sprite.Group, damge: pygame.sprite.Group, sprtes: pygame.sprite.Group, spells: pygame.sprite.Group):
    bullets_collides = pygame.sprite.groupcollide(damge, mob, True, False)
    for bullet in bullets_collides:
        collisions = pygame.sprite.spritecollide(bullet, mob, False)
        for single_mob in collisions:
            single_mob.hp -= bullet.damage
            if single_mob.hp <= 0:
                single_mob.kill()
                new_mob(sprtes, mob)






