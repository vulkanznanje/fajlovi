import pygame as pg
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Srce")
prozor.fill(pg.Color("White"))
#KVADRAT
temena = ((100,200), (200,100), (300,200), (200,300))
pg.draw.polygon(prozor, pg.Color("red"), temena)
#LEVI KRUG
pg.draw.circle(prozor, pg.Color("red"), (150, 150), 71)
#DESNI KRUG
pg.draw.circle(prozor, pg.Color("red"), (250, 150), 71)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


