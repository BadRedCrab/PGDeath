import random
from map import *
from data import dark_eneble, howmanyplayers, FPS, deathscreen, dark_cords, game_end, tick


clock = pg.time.Clock()

pg.init()
pg.mixer.init()
pg.display.set_caption('Game')

dark_s = pg.image.load('textures/dark.png').convert_alpha()
dash_s = pg.image.load('textures/dash.png').convert_alpha()



while not game_end:
    tick += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_end = True
        if event.type == pg.KEYDOWN:
            for index, unit in enumerate(entiti):
                cords_entiti()
                # print(cords[1])
                if unit[0] == 0:
                    h = 0
                    while h == 0:
                        event_m = random.choice([pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN])
                        h = unit[1].step_m(event_m, cords, entiti)
                    cords_entiti()
                elif unit[0] == 1:
                    unit[1].step(event, cords)
                    cords_entiti()

    clock.tick(FPS)
    screen.fill((30, 30, 30))
    feild()
    for index, unit in enumerate(entiti):
        pg.draw.rect(screen, unit[1].color, (unit[1].rect.x, unit[1].rect.y, *unit[1].size))

    walls()

    for i in entiti:
        if i[1].tipe == "player":
            i[1].living(entiti_cords2)

    for index, unit in enumerate(entiti):
        if unit[1].tipe == "player" or unit[1].tipe == "body":
            if tick == 1:
                dark_cords[0] += int(unit[1].rect.x - 15)
                dark_cords[1] += int(unit[1].rect.y - 15)

            dark_r = dark_s.get_rect(bottomright=(dark_cords[0], dark_cords[1]))



            from math import fabs

            if fabs(unit[1].rect.x + 810 - dark_cords[0]) > 31 or fabs(unit[1].rect.y + 810 - dark_cords[1]) > 31:
                if dark_cords[2] != 5.0:
                    dark_cords[2] += 0.5
            else:
                if dark_cords[2] != 2.0:
                    dark_cords[2] -= 0.5
            if unit[1].rect.x + 810 < dark_cords[0]:
                dark_cords[0] -= int(dark_cords[2])
            if unit[1].rect.y + 815 < dark_cords[1]:
                dark_cords[1] -= int(dark_cords[2])
            if unit[1].rect.x + 810 > dark_cords[0]:
                dark_cords[0] += int(dark_cords[2])
            if unit[1].rect.y + 815 > dark_cords[1]:
                dark_cords[1] += int(dark_cords[2])
            # print(unit[1].rect.x+810,dark_cords[0],unit[1].rect.y+815,dark_cords[1])
            if dark_eneble:
                screen.blit(dark_s, dark_r)
            if unit[1].dash >= 3:
                dash_r1 = dash_s.get_rect(bottomright=(30, 30))
                screen.blit(dash_s, dash_r1)
            if unit[1].dash >= 6:
                dash_r2 = dash_s.get_rect(bottomright=(60, 30))
                screen.blit(dash_s, dash_r2)
            if unit[1].dash >= 9:
                dash_r3 = dash_s.get_rect(bottomright=(90, 30))
                screen.blit(dash_s, dash_r3)
    howmanyplayers = 0
    for i in entiti:
        if i[1].tipe == "player":
            howmanyplayers += 1

    if howmanyplayers == 0:
        for i in entiti:
            i[1].life = False
        surf = pg.Surface((810, 720))
        surf.fill((0, 0, 0))
        surf.set_alpha(deathscreen)
        screen.blit(surf, (0, 0))
        if deathscreen < 201:
            deathscreen += 5
        f1 = pg.font.Font(None, 50)
        pg.draw.rect(screen, (120, 120, 120), (230, 313, 350, 50))

        text1 = f1.render('Смерть неминуема', True, (0, 0, 0))
        screen.blit(text1, (250, 320))
        if deathscreen >=201:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN or event.type == pg.QUIT:
                    game_end = True


    pg.display.update()
    pg.display.flip()
