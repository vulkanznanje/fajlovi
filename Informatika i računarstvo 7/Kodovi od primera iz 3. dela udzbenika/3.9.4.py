import pygame as pg
import math
pg.init()
s = 300
v = 300
prozor = pg.display.set_mode((s, v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("White"))
(x,y) = (s//2,v//2) #Centar prozora
d = s//2 #Dijagonala kvadrata
a = (d*math.sqrt(2))/2 #Stranica kvadrata
a = round(a) #Zaokruživanje na celobrojnu vrednost
#Levo, gornje, desno i donje teme mnogougla (kvadrata)
temena = ((x-d//2, y), (x, y-d//2), (x+d//2, y), (x, y+d//2))
pg.draw.polygon(prozor, pg.Color("red"), temena)
#Levi krug
pg.draw.circle(prozor, pg.Color("red"), (x-d//4, y-d//4), a//2)
#Desni krug
pg.draw.circle(prozor, pg.Color("red"), (x+d//4, y-d//4), a//2)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

#s = int(input("Unesi širinu prozora: "))
#v = int(input("Unesi visinu prozora: "))
