#Na sivoj pozadini nacrtaj crni semafor na kom žuto svetlo trepće.

import random
import pygame as pg
pg.init()
(sirina, visina) = (400, 400)
r=sirina//8
prozor = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Semafor")
(x, y) = (sirina//2, visina//2)
boje = ["yellow", "lightyellow"]
broj_boje = 0
def crtaj():
    global broj_boje
    prozor.fill(pg.Color("grey"))
    pg.draw.rect(prozor, pg.Color("black"), (2.5*r,r,3*r, 6*r))
    pg.draw.circle(prozor, pg.Color("red"), (x, y-2*r), r)
    pg.draw.circle(prozor,pg.Color(boje[broj_boje]), (x,y),r)
    pg.draw.circle(prozor, pg.Color("green"), (x, y+2*r), r)
def novi_frejm():
    global broj_boje
    broj_boje = (broj_boje + 1) % len(boje)
kraj = False
sat = pg.time.Clock()  
while not kraj:
    crtaj()                              
    pg.display.update()     
    for dogadjaj in pg.event.get():      
        if dogadjaj.type == pg.QUIT:
            kraj = True         
    sat.tick(3)                          
    novi_frejm()
pg.quit()











    




