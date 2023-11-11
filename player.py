import pygame as pg


class Player:
    def __init__(self, x=359, y=359):
        self.tipe = "player"
        self.size = (31, 31)
        self.image = pg.Surface((31, 31))
        self.color = (0, 255, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_key = pg.K_DOWN
        self.cords = (self.rect.x, self.rect.y)
        self.life = True
        self.dash = 9
    def living(self, entiti_cords2):
        from math import fabs
        # print(entiti_cords2)
        for i in entiti_cords2:
            if i[0] == 'monster' and ((fabs(i[1][0] - self.rect.x) == 0 and fabs(i[1][1] - self.rect.y) == 30)
                                      or (fabs(i[1][0] - self.rect.x) == 30 and fabs(i[1][1] - self.rect.y) == 0)):
                self.color = (150, 150, 150)
                self.life = False
                self.tipe = "body"

    def step(self, event, cords):
        # print(cords[1])
        if not self.life:
            return 1
        event=event.key
        if event == pg.K_SPACE:
            self.dash -= 3
            event = self.last_key
            if event == pg.K_LEFT:
                if (not (self.rect.x - 60, self.rect.y) in cords[0]) and \
                        (not (self.rect.x - 60, self.rect.y) in cords[1]) and \
                        (not (self.rect.x - 30, self.rect.y) in cords[0]) and \
                        (not (self.rect.x - 30, self.rect.y) in cords[1]):
                    self.last_key = pg.K_LEFT
                    self.rect.x -= 60
                    return 1
            if event == pg.K_RIGHT:
                if (not (self.rect.x + 60, self.rect.y) in cords[0]) and \
                        (not (self.rect.x + 60, self.rect.y) in cords[1]) and \
                        (not (self.rect.x + 30, self.rect.y) in cords[0]) and \
                        (not (self.rect.x + 30, self.rect.y) in cords[1]):
                    self.last_key = pg.K_RIGHT
                    self.rect.x += 60
                    return 1
            if event == pg.K_UP:
                if (not (self.rect.x, self.rect.y - 60) in cords[0]) and \
                        (not (self.rect.x, self.rect.y - 60) in cords[1]) and \
                        (not (self.rect.x, self.rect.y - 30) in cords[0]) and \
                        (not (self.rect.x, self.rect.y - 30) in cords[1]):
                    self.last_key = pg.K_UP
                    self.rect.y -= 60
                    return 1
            if event == pg.K_DOWN:
                if (not (self.rect.x, self.rect.y + 60) in cords[0]) and \
                        (not (self.rect.x, self.rect.y + 60) in cords[1]) and \
                        (not (self.rect.x, self.rect.y + 30) in cords[0]) and \
                        (not (self.rect.x, self.rect.y + 30) in cords[1]):
                    self.last_key = pg.K_DOWN
                    self.rect.y += 60
                    return 1


        if event == pg.K_LEFT:
            if (not (self.rect.x - 30, self.rect.y) in cords[0]) and \
                    (not (self.rect.x - 30, self.rect.y) in cords[1]):
                self.last_key=pg.K_LEFT
                self.rect.x -= 30
        if event == pg.K_RIGHT:
            if (not (self.rect.x + 30, self.rect.y) in cords[0]) and \
                    (not (self.rect.x + 30, self.rect.y) in cords[1]):
                self.last_key=pg.K_RIGHT
                self.rect.x += 30
        if event == pg.K_UP:
            if (not (self.rect.x, self.rect.y - 30) in cords[0]) and \
                    (not (self.rect.x, self.rect.y - 30) in cords[1]):
                self.last_key=pg.K_UP
                self.rect.y -= 30
        if event == pg.K_DOWN:
            if (not (self.rect.x, self.rect.y + 30) in cords[0]) and \
                    (not (self.rect.x, self.rect.y + 30) in cords[1]):
                self.last_key=pg.K_DOWN
                self.rect.y += 30
        if self.dash<9:
            self.dash+=1


class Monster:
    def __init__(self, x=329, y=359):
        self.tipe = "monster"
        self.size = (31, 31)
        self.image = pg.Surface((31, 31))
        self.color = (255, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cords = (self.rect.x, self.rect.y)
        self.life = True
        self.direction = []
        self.err_step = 0

    def step_m(self, event, cords, entiti):
        if not self.life:
            return 1
        for index, unit in enumerate(entiti):
            if unit[0] == 1:
                from math import fabs
                if fabs(unit[1].rect.x - self.rect.x) <= 90 and fabs(unit[1].rect.y - self.rect.y) <= 90:
                    # print(unit[1].rect.x,unit[1].rect.y,self.rect.x,self.rect.y)
                    if unit[1].rect.x < self.rect.x:
                        if not (self.rect.x - 30, self.rect.y) in cords[0]:
                            if not (self.rect.x - 30, self.rect.y) in cords[1]:
                                #print("left", unit[1].rect.x, self.rect.x)
                                self.direction.append((pg.K_LEFT, self.rect.x - unit[1].rect.x))
                    if unit[1].rect.x > self.rect.x:
                        if not (self.rect.x + 30, self.rect.y) in cords[0]:
                            if not (self.rect.x + 30, self.rect.y) in cords[1]:
                                #print("right", unit[1].rect.x, self.rect.x)
                                self.direction.append((pg.K_RIGHT, unit[1].rect.x - self.rect.x))
                    if unit[1].rect.y < self.rect.y:
                        if not (self.rect.x, self.rect.y - 30) in cords[0]:
                            if not (self.rect.x, self.rect.y - 30) in cords[1]:
                                #print("up", unit[1].rect.y, self.rect.y)
                                self.direction.append((pg.K_UP, self.rect.y - unit[1].rect.y))
                    if unit[1].rect.y > self.rect.y:
                        if not (self.rect.x, self.rect.y + 30) in cords[0]:
                            if not (self.rect.x, self.rect.y + 30) in cords[1]:
                                #print("down", unit[1].rect.y, self.rect.y)
                                self.direction.append((pg.K_DOWN, unit[1].rect.y - self.rect.y))
                    # print(self.direction)

                    if len(self.direction) == 1:
                        event = self.direction[0][0]
                    elif len(self.direction) == 2:
                        #print(self.direction)
                        if self.direction[0][1] < self.direction[1][1]:
                            event = self.direction[1][0]
                        elif self.direction[0][1] > self.direction[1][1]:
                            event = self.direction[0][0]
                        elif self.direction[0][1] == self.direction[1][1]:
                            from random import choice
                            event = choice([self.direction[0][0], self.direction[1][0]])
                    self.direction.clear()
                else:
                    self.direction.clear()
        # print(event)
        if event == pg.K_LEFT:
            if not (self.rect.x - 30, self.rect.y) in cords[0]:
                if not (self.rect.x - 30, self.rect.y) in cords[1]:
                    self.rect.x -= 30
                return 1
        if event == pg.K_RIGHT:
            if not (self.rect.x + 30, self.rect.y) in cords[0]:
                if not (self.rect.x + 30, self.rect.y) in cords[1]:
                    self.rect.x += 30
                return 1
        if event == pg.K_UP:
            if not (self.rect.x, self.rect.y - 30) in cords[0]:
                if not (self.rect.x, self.rect.y - 30) in cords[1]:
                    self.rect.y -= 30
                return 1
        if event == pg.K_DOWN:
            if not (self.rect.x, self.rect.y + 30) in cords[0]:
                if not (self.rect.x, self.rect.y + 30) in cords[1]:
                    self.rect.y += 30
                return 1
        self.err_step += 1
        if self.err_step > 10:
            return 1
        return 0
