import pygame as pg
import math
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("White"))
(x,y) = (s//2,v//6) #Teme naspram osnovice (teme C)
a = s//2 #Dužina osnovice
ha = round(v*2/3) #Visina nad osnovicom
#Temena C, A i B
temena = ((x,y), (x-a/2,y+ha), (x+a/2,y+ha))
pg.draw.polygon(prozor, pg.Color("Turquoise"), temena, 5)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()






