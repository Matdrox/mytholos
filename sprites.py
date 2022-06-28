import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill((0, 0, 0))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def update(self):
		self.rect.x = self.x * TILE_SIZE
		self.rect.y = self.y * TILE_SIZE