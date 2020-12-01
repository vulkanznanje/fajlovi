#U belom prozoru veličine 600x600 nacrtaj žutog smajlija sa crnim
#očima i crnim ustima. Za crtanje koristi krugove i kružni luk.

import pygame as pg
import math
pg.init()
prozor = pg.display.set_mode((600, 600))
prozor.fill(pg.Color("white"))
pg.draw.circle(prozor, pg.Color("yellow"), (300, 300), 200)
pg.draw.circle(prozor, pg.Color("black"), (225, 250), 30, 30)
pg.draw.circle(prozor, pg.Color("black"), (375, 250), 30, 30)
pg.draw.arc(prozor,pg.Color("black"),(200,200,200,200),math.radians(-145),math.radians(-35),15)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()



