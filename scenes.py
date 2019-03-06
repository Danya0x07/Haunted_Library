from pygame import display, event, mouse, Surface, Color
from pygame.sprite import Group
from pygame.time import Clock
from pygame.locals import *

import maps
from objects import Wall, Camera, Hunter, Button
from settings import *


class Menu:
    NUM_OF_BTNS = 3

    def __init__(self, screen):
        self.screen = screen
        self.bg = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg.fill(Color('#333377'))
        self.clock = Clock()
        self.btn_frame = Surface((BTN_WIDTH, BTN_HEIGHT * Menu.NUM_OF_BTNS))
        self.btn_rect = self.btn_frame.get_rect(center=self.bg.get_rect().center)
        print(self.btn_rect.center)
        self.create_buttons()

    def create_buttons(self):
        Button.frame_rect = self.btn_rect
        self.btn_play = Button("btn 1", 0)
        self.buttons = Group(self.btn_play, Button("btn 2", 1), Button("btn 3", 2))

    def check_events(self):
        for e in event.get():
            if e.type == QUIT:
                raise SystemExit
            elif e.type == MOUSEBUTTONDOWN:
                for btn in iter(self.buttons):
                    if btn.check_pressed(e.pos):
                        print('button pressed')

    def update_objects(self):
        self.buttons.update(mouse.get_pos())

    def draw_objects(self):
        self.buttons.draw(self.btn_frame)
        self.bg.blit(self.btn_frame, self.btn_rect)
        self.screen.blit(self.bg, (0, 0))

    def mainloop(self):
        while True:
            self.check_events()
            self.update_objects()
            self.draw_objects()
            self.clock.tick(60)
            display.update()

class MainScene:

    def __init__(self, screen):
        self.screen = screen
        self.create_objects()
        self.create_map(maps.hotel_map)

    def create_objects(self):
        self.bg = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg.fill(Color('#000077'))
        self.hunter = Hunter(0, 0)
        self.entities = Group(self.hunter)
        self.walls = []
        self.camera = Camera(maps.hotel_map)
        self.clock = Clock()

    def create_map(self, level_map):
        x = y = 0
        for row in level_map:
            for col in row:
                if col == '-':
                    wall = Wall(x, y)
                    self.entities.add(wall)
                    self.walls.append(wall)
                    #self.walls += (wall,)
                x += WALL_LENGTH
            y += WALL_LENGTH
            x = 0

    def check_events(self):
        for e in event.get():
            if e.type == QUIT:
                raise SystemExit
            elif e.type == KEYDOWN:
                self.hunter.set_direction(e.key, True)
            elif e.type == KEYUP:
                self.hunter.set_direction(e.key, False)

    def update_objects(self):
        self.hunter.update(self.walls)
        self.camera.update(self.hunter)

    def draw_objects(self):
        self.screen.blit(self.bg, (0, 0))
        for e in self.entities:
            self.screen.blit(e.image, self.camera.apply(e))

    def mainloop(self):
        while True:
            self.check_events()
            self.update_objects()
            self.draw_objects()
            self.clock.tick(60)
            display.update()