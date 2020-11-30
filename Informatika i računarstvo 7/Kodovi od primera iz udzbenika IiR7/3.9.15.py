import pygame as pg
import math
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("White"))
(x,y) = (s//2,v//4) #Gornje teme
a = s//2 #Dužina stranice
h = round(a*math.sqrt(3)/2) #Visina trougla
#Temena trougla: gornje, levo i desno
temena = ((x,y), (x-a/2,y+h), (x+a/2,y+h))
pg.draw.polygon(prozor, pg.Color("Violet"), temena, 7)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()







