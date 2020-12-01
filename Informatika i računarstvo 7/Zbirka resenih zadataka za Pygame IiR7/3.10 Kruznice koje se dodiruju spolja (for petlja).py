#Pomoću for petlje nacrtaj niz od 10 simetričnih kružnica
#koje se dodiruju spolja u jednoj tački i koje se
#nalaze sredini prozora po vertikali.

import pygame as pg
pg.init()
(s, v) = (600, 300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Simetrične kružnice")
prozor.fill(pg.Color("White"))
y=v//2
r=s//20
for i in range(1,s,2):
    pg.draw.circle(prozor, pg.Color("Brown"), (i*r,y), r, 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()







