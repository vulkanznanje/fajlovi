import pygame as pg
import math
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Sladoled")
prozor.fill(pg.Color("white"))
#OBOD KORNETA
pg.draw.rect(prozor, pg.Color("black"), (150, 140, 101, 11), 2)
#KUGLA
elipsa = (147, 70, 108, 108)
pg.draw.arc(prozor, pg.Color("black"), elipsa,\
            math.radians(-17), math.radians(200), 3)
#KORNET
temena = ((150, 150), (200,300), (250,150))
pg.draw.polygon(prozor, pg.Color("black"), temena, 2)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()




