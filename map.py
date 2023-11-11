from feild_sc import *
from player import Monster, Player
from maps import choise_map
from data import nmap
text_map = choise_map(nmap)

wall_cords = []
entiti_cords = []
entiti_cords2 = []
cords = [wall_cords, entiti_cords]

entiti = []
initpl = 1


def cords_entiti():
    global entiti
    global entiti_cords
    entiti_cords.clear()
    entiti_cords2.clear()
    for unit in entiti:
        entiti_cords.append((unit[1].rect.x, unit[1].rect.y))
        entiti_cords2.append((unit[1].tipe, (unit[1].rect.x, unit[1].rect.y)))
        # print(unit[1].cords)


def walls():
    for index, value in enumerate(text_map):
        for index2, value2 in enumerate(value):
            global wall_cords
            global initpl
            if value2 == 'w':
                pg.draw.rect(screen, (20, 10, 10), (index2 * 30 - 1, index * 30 - 1, 31, 31))
                wall_cords.append((index2 * 30 - 1, index * 30 - 1))
            if initpl == 1:
                global entiti
                if value2 == 'p':
                    player = Player(index2 * 30 - 1, index * 30 - 1)
                    entiti.append((1, player))
                if value2 == 'm':
                    monster = Monster(index2 * 30 - 1, index * 30 - 1)
                    entiti.append((0, monster))
    initpl = 0


def ii_monsters():
    pass
