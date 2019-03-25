from pygame.sprite import collide_rect

from things import Thing
from config import *


class Teleport(Thing):

    def __init__(self, x, y, id, tgt_id):
        super().__init__(TELEPORT_SIZE, TELEPORT_COLOR, topleft=(x, y))
        self.id = id
        self.tgt_id = tgt_id
        self.active = True

    def check_mobs_overlaying(self, mobs):
        for mob in mobs:
            if self.rect.colliderect(mob.frame_rect):
                return mob

    def handle_teleporting(self, teleport, mobs):
        mob = self.check_mobs_overlaying(mobs)
        if mob:
            mob.frame_rect.center = teleport.rect.center
            teleport.active = False

    def update(self, player, enemies, healers, teleports):
        if self.active and self.tgt_id:
            tgt_teleport = self.get_tp_by_id(teleports, self.tgt_id)
            if collide_rect(self, player):
                player.rect.center = tgt_teleport.rect.center
                tgt_teleport.active = False
            self.handle_teleporting(tgt_teleport, enemies)
            self.handle_teleporting(tgt_teleport, healers)
        else:
            is_overlayed = False
            if collide_rect(self, player):
                is_overlayed = True
            if self.check_mobs_overlaying(enemies):
                is_overlayed = True
            if self.check_mobs_overlaying(healers):
                is_overlayed = True
            self.active = not is_overlayed

    @staticmethod
    def get_tp_by_id(group, id):
        for tp in group:
            if tp.id == id:
                return tp
