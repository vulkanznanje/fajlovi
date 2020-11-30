import pygame as pg
import math
pg.init()
(s,v) = (500,600)
prozor = pg.display.set_mode((s, v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("white"))
(x,y) = (s//2,v//5) #Centar glave
r = v//8 #Poluprečnik glave
crna = pg.Color("Black") #Boja za sve elemente crteža
pg.draw.circle(prozor, crna, (x,y),r, 3) #Glava
pg.draw.line(prozor, crna, (x,y+r),(x,y+2*r),3) #Vrat
pg.draw.line(prozor, crna, (x,y+2*r),(x-r,y+3*r),3) #RukaL
pg.draw.line(prozor, crna, (x,y+2*r),(x+r,y+3*r),3) #RukaD
pg.draw.line(prozor, crna, (x,y+2*r),(x,y+4*r),3) #Telo
pg.draw.line(prozor, crna, (x,y+4*r),(x-r,y+6*r),3) #NogaL
pg.draw.line(prozor, crna, (x,y+4*r),(x+r,y+6*r),3) #NogaD
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()







