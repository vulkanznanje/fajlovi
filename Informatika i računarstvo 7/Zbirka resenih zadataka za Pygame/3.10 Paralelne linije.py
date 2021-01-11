#Nacrtaj 15 paralelnih vertikalnih crvenih duži koje se
#prostiru od vrha do dna prozora.

import pygame as pg
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("x linija")
prozor.fill(pg.Color("white"))
x = s//15
for i in range(1,x):
    pg.draw.line(prozor, pg.Color("red"), (i*x, 0), (i*x, v), 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()








