map0 = [
    'wwwwwwwwwwwwwwwwwwwwwwwwwww',
    'w.........................w',
    'w.p.......................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'w.........................w',
    'wwwwwwwwwwwwwwwwwwwwwwwwwww'
]
map1 = [
    'wwwwwwwwwwwwwwwwwwwwwwwwwww',
    'wp.w...........ww.....ww..w',
    'w..w...www...w....ww......w',
    'ww.w.....wwwwww.wwwww.ww.ww',
    'ww...w.....w..........w...w',
    'w....w....m.......mw.ww.www',
    'w..wwwm..w.w.wwww.ww......w',
    'w.....w....w.w.......www..w',
    'w..ww...w.........wwwww..ww',
    'w.......wwww..w...........w',
    'w.www.w..w....w.w.wwwww.w.w',
    'w..w..w..w....w.........w.w',
    'ww..........w.wwww.ww.www.w',
    'w...wwwww.w...w..w....m...w',
    'w.w..w....w....w.w..w..w..w',
    'www..w..w..m.w...w.ww..ww.w',
    'w....ww......www.w........w',
    'w..w....ww.w...w.w.w.ww.w.w',
    'w........w.....w...w.w....w',
    'w.ww.w.wwwww.....w.w...w..w',
    'w..w.w.w....m..w.w...w.ww.w',
    'ww.w.w.www.w.ww....w.w.ww.w',
    'w..m.......w.....w...w.m..w',
    'wwwwwwwwwwwwwwwwwwwwwwwwwww'
]
map2 = [
    'wwwwwwwwwwwwwwwwwwwwwwwwwww',
    'w.......w.........w.......w',
    'w.p..w..w.........w..w....w',
    'w....w...............w....w',
    'w....wwww.wwwwwww.wwww....w',
    'w.ww.w...............w.ww.w',
    'w..........w..............w',
    'w.w.w.w.w.w.w.............w',
    'w..w...w..www.............w',
    'w.w.w.w...w.w.............w',
    'w.........................w',
    'w.........................w',
    'w.....ww...........ww.....w',
    'w...w.....w.....w.....w...w',
    'w.....w......w......w.....w',
    'w.........................w',
    'w.wwww.wwwwww.wwwwww.wwww.w',
    'w.........................w',
    'w.ww.w...w.......w...w.ww.w',
    'w....w...w.......w...w....w',
    'w....w......www......w....w',
    'w....w...w.......w...w....w',
    'w........w.......w........w',
    'wwwwwwwwwwwwwwwwwwwwwwwwwww'
]
maps=[map0,map1,map2]
def choise_map(key=-1):
    if key==-1:
        import random
        return random.choice(maps)
    else:
        return maps[key]