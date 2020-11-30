import pygame as pg
pg.init()
(s,v) = (500,100)
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Simetrične kružnice")
prozor.fill(pg.Color("White"))
y = v//2
r = s//20
x = r
while x < s:
    pg.draw.circle(prozor, pg.Color("Black"), (x,y), r)
    pg.draw.circle(prozor, pg.Color("Red"), (x,y), r, 5)
    x = x + 2*r
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()






