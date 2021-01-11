import pygame as pg
import random
pg.init()
(s,v) = (400,400)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Koncentrični prstenovi")
prozor.fill(pg.Color("White"))
for r in range (s//2,s//40,-s//20):   
    BOJA = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    pg.draw.circle(prozor, BOJA, (s//2,v//2), r, 0)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

