import pygame as pg
pg.init()
pg.display.set_caption("Šahovska tabla")
(s, v) = (400, 400)
prozor = pg.display.set_mode((s, v))
prozor.fill(pg.Color("White"))
#Broj podela table po horizontali i vertikali
brojPodela = 8
sirinaPolja = s//brojPodela #Širina 1 polja
visinaPolja = v//brojPodela #Visina 1 polja
for i in range(brojPodela):
    for j in range(brojPodela):
        if (i % 2 !=0 and j % 2 ==0) or (i % 2 == 0 and j % 2 != 0):
            #Položaj i dimenzije polja u promenljivoj
            KVADRAT = (i*sirinaPolja, j*visinaPolja, sirinaPolja, visinaPolja)
            pg.draw.rect(prozor, pg.Color("Black"), KVADRAT)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

