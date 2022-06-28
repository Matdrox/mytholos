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