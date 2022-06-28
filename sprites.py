from matplotlib.pyplot import xscale
import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill((255, 255, 0))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y

	def move(self, dx=0, dy=0):
		self.x += dx
		self.y += dy

	def update(self):
		# 1 px => 64 px
		self.rect.x = self.x * TILE_SIZE
		self.rect.y = self.y * TILE_SIZE

class Wall(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILE_SIZE
		self.rect.y = y * TILE_SIZE