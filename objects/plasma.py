from random import randint

from pygame.sprite import Sprite, collide_rect, spritecollideany

from utils.ultimate_animation import UltimateAnimation
from utils.assets import (plasm_anim, player_plasma_image,
                          enemy_plasma_image, boss_enemy_plasma_image)
from utils.config import *


class Plasma(Sprite):
    """Базовый класс для плазмы. Плазма привидений."""

    image = enemy_plasma_image
    offset = ENEMY_PLASMA_OFFSET

    def __init__(self, x_vel, y_vel, center):
        super().__init__()
        self.rect = self.image.get_rect(center=center)
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self, scene):
        self.rect.x += round(self.x_vel * scene.delta_time)
        self.rect.y += round(self.y_vel * scene.delta_time)
        for wall in scene.walls:
            if self.rect.colliderect(wall):
                scene.plasmas.remove(self)

    def update(self, scene):
        self.move(scene)
        furn = spritecollideany(self, scene.furniture)
        if furn:
            furn.shift_hp(randint(*self.offset))
            UltimateAnimation(scene.animations, plasm_anim, self.rect.center, 9, 3)
            scene.plasmas.remove(self)
        if collide_rect(self, scene.player):
            scene.player.shift_hp(randint(*self.offset))
            UltimateAnimation(scene.animations, plasm_anim, self.rect.center, 9, 3)
            scene.plasmas.remove(self)


class BossPlasma(Plasma):
    """Плазма привидений-боссов."""

    image = boss_enemy_plasma_image
    offset = BOSS_ENEMY_PLASMA_OFFSET


class PlayerPlasma(Plasma):
    """Плазма игрока."""

    image = player_plasma_image
    offset = PLAYER_PLASMA_OFFSET

    def update(self, scene):
        self.move(scene)
        enemy = spritecollideany(self, scene.enemies)
        if enemy:
            enemy.shift_hp(randint(*self.offset))
            UltimateAnimation(scene.animations, plasm_anim, self.rect.center, 9, 3)
            scene.plasmas.remove(self)
        furn = spritecollideany(self, scene.furniture)
        if furn:
            furn.shift_hp(self.offset[1])
            UltimateAnimation(scene.animations, plasm_anim, self.rect.center, 9, 3)
            scene.plasmas.remove(self)
