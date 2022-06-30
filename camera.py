import pygame as pg
from settings import *


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.y = 0

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        self.y = -target.rect.y + int(HEIGHT/2)+128
        # print(y/32+12)
        # y = min(0, y)
        # y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(0, self.y, self.width, self.height)
