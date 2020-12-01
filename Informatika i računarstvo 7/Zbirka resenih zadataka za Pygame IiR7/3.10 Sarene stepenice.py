#Nacrtaj niz od 10 vertikalnih pravougaonika različitih boja pri čemu
#svaki naredni treba da bude viši od prethodnog (gledano s leva na desno).
#Neka program sam bira boje za pravougaonike (koristi funkciju random.randint).

import pygame as pg
import random
pg.init()
s = 400
v = 400
prozor = pg.display.set_mode((s, v))
pg.display.set_caption("Šarene stepenice")
prozor.fill(pg.Color("white"))
brojStepenika = 10
sirinaS = s//brojStepenika
visinaS = v//brojStepenika
for i in range(brojStepenika):
    boja = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pg.draw.rect(prozor,boja, (i*sirinaS, v - i*visinaS, sirinaS, v - visinaS))
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()






