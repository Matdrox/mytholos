# Matei Cananau 2022
import pygame as pg
import sys
from settings import *
# from sprites import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.load_data()

	def load_data(self):
		pass

	def new(self):
		self.all_sprites = pg.sprite.Group()
	
	def run(self):
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS)/1000
			self.events()
			self.update()
			self.draw()
	
	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
		self.all_sprites.update()
	
	def draw_grid(self):
		for x in range(0, WIDTH, TILE_SIZE):
			pg.draw.line(self.screen, (150, 150, 150), (x, 0), (x, HEIGHT))
		for y in range(0, WIDTH, TILE_SIZE):
			pg.draw.line(self.screen, (150, 150, 150), (0, y), (WIDTH, y))

	def draw(self):
		self.screen.fill(BG_COLOR)
		self.draw_grid()
		self.all_sprites.draw(self.screen)
		pg.display.flip()
	
	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()
	
	def show_start_screen(self):
		pass

	def show_go_screen(self):
		pass

g = Game()
g.show_start_screen()
while True:
	g.new()
	g.run()
	g.show_go_screen()