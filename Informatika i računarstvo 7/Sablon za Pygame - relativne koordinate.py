import pygame as pg
pg.init()
s = 400
v = 400
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("White"))

#TELO PROGRAMA

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


