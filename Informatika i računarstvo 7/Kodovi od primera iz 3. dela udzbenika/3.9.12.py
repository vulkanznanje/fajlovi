import pygame as pg
import math
pg.init()
(s,v) = (300,300)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Relativne koordinate")
prozor.fill(pg.Color("ForestGreen"))
(x,y) = (s//2,v//2) #centar žutog kruga
a = s//4 #stranica jednakostraničnog trougla
h = round(a*math.sqrt(3)/2) #visina trougla
r = a//2 #poluprečnik krugova
latice = pg.Color("White") #boja za latice
pg.draw.circle(prozor, pg.Color("yellow"), (x,y),r)
pg.draw.circle(prozor, latice, (x-a,y),r) #levi krug
pg.draw.circle(prozor, latice, (x-r,y-h),r) #gore levo
pg.draw.circle(prozor, latice, (x+r,y-h),r) #gore desno
pg.draw.circle(prozor, latice, (x+a,y),r) #desni krug
pg.draw.circle(prozor, latice, (x+r,y+h),r) #dole desno
pg.draw.circle(prozor, latice, (x-r,y+h),r) #dole levo
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

#x1 = Cx-a;x2 = Cx-a//2;x3 = Cx+a//2; x4 = Cx+a; x5 = Cx+a//2; x6 = Cx-a//2
#y1 = Cy; #y2 = Cy-h; y3 = Cy-h; y4 = Cy; y5 = Cy+h; y6 = Cy+h





