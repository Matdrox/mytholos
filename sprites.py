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
		if not self.collide_walls(dx, dy):
			self.x += dx
			self.y += dy
	
	def collide_walls(self, dx=0, dy=0):
		for wall in self.game.walls:
			if wall.x == self.x + dx and wall.y == self.y + dy:
				return True
		# for enemy in self.game.enemies:
		# 	if enemy.x == self.x + dx and enemy.y == self.y + dy:
		# 		return True
		return False

	def update(self):
		# 1 px => 64 px
		self.rect.x = self.x * TILE_SIZE
		self.rect.y = self.y * TILE_SIZE

class Enemy(pg.sprite.Sprite):
	def __init__(self, game, x, y):
		self.groups = game.all_sprites, game.walls
		self.game = game
		pg.sprite.Sprite.__init__(self, self.groups)
		self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
		self.image.fill((255, 0, 0))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.rect.x = x * TILE_SIZE
		self.rect.y = y * TILE_SIZE
	
	def move(self, dx=0, dy=0):
		if not self.collide_walls(dx, dy):
			self.x += dx
			self.y += dy

	def collide_walls(self, dx=0, dy=0):
		for wall in self.game.walls:
			if wall.x == self.x + dx and wall.y == self.y + dy:
				return True
		if self.game.player.x == self.x + dx and self.game.player.y == self.y + dy:
			return True
		return False

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