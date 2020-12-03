#Nacrtaj šahovsku tablu koja će biti udaljena za po jedno polje od svake
#ivice prozora i koja će biti uokvirena crnim kvadratom.

import pygame as pg
pg.init()
pg.display.set_caption("Sahovska tabla")
(sirina, visina) = (400, 400)
prozor = pg.display.set_mode((sirina, visina))
Polje = sirina//10
Broj_polja = 8
prozor.fill(pg.Color("white"))
Broj_kvadrata = 0
for i in range(1,Broj_polja+1):
    for j in range(1,Broj_polja+1):
        if Broj_kvadrata % 2 == 0:
            pg.draw.rect(prozor, pg.Color("White"),[Polje*j,Polje*i,Polje,Polje])
        else:
            pg.draw.rect(prozor, pg.Color("Black"), [Polje*j,Polje*i,Polje,Polje])
        Broj_kvadrata = Broj_kvadrata + 1
    Broj_kvadrata = Broj_kvadrata - 1
pg.draw.rect(prozor,pg.Color("Black"),[Polje,Polje,Broj_polja*Polje,Broj_polja*Polje],1)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
