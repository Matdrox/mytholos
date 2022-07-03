import random
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from camera import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.score = -500

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        self.player_img = pg.image.load(
            path.join(img_folder, PLAYER_IMG)).convert_alpha()
        # CHANGE ORIGIN

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                if tile == 'e':
                    self.enemy = Enemy(self, col, row)
        self.camera = Camera(WIDTH, HEIGHT)

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
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, (150, 150, 150), (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, (150, 150, 150), (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill((255, 212, 162))
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                    if self.camera.y > self.score:
                        self.score = self.camera.y
                        pg.display.set_caption(str(self.camera.y))
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                rand = random.randint(1, 4)
                if rand == 1:
                    self.enemy.move(dx=-1)
                if rand == 2:
                    self.enemy.move(dx=1)
                if rand == 3:
                    self.enemy.move(dy=-1)
                if rand == 4:
                    self.enemy.move(dy=1)

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
