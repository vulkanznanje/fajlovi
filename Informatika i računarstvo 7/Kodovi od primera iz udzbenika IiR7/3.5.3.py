import pygame as pg
pg.init()

#čuvanje kodova boja u torkama
bojaZaProzor = (240,255,255) #azurna
bojaZaObjekte = (92,51,23) #pekarska čokolada

prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Boje u torkama")

#prozor obojen bojom iz torke bojaZaProzor
prozor.fill(bojaZaProzor) 

#argument za boju duži je naziv torke
pg.draw.line(prozor, bojaZaObjekte, (50,100), (250,100), 5)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

