import pygame as pg

x = 810
y = 720
screen = pg.display.set_mode((x, y))


def feild():
    for string in range(27):
        for row in range(24):
            y = row * 30
            x = string * 30
            pg.draw.rect(screen, (50, 50, 50), (x + 0.5, y + 0.5, 29, 29))
