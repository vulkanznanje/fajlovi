import pygame as pg
import random
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Tufne")
prozor.fill(pg.Color("White"))
for r in range (s//40, s//4, 4): 
    #NASUMIČNA BOJA
    BOJA = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #NASUMIČNA X KOORDINATA CENTRA
    Cx = random.randint(0,s)
    #NASUMIČNA Y KOORDINATA CENTRA
    Cy = random.randint(0,v)
    pg.draw.circle(prozor, BOJA, (Cx,Cy), r, 4)
    pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

