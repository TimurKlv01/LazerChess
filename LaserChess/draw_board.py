import pygame as pg
WIDTH = 1200
HEIGHT = 900
screen = pg.display.set_mode([WIDTH, HEIGHT])
def draw_board():
    pg.draw.rect(screen, (226, 200, 182), [0, 0, 1000, 800])
    for i in range(10):
        pg.draw.line(screen, (255, 239, 226), (0, 100 * i), (1000, 100 * i), 3)
        pg.draw.line(screen, (255, 239, 226), (100 * i, 0), (100 * i, 800), 3)
