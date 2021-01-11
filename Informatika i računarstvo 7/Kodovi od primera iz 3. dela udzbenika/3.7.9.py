import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))
#KRUŽNICA
pg.draw.circle(prozor, pg.Color("Steel Blue"), (80, 100), 65, 3)
#KRUG
pg.draw.circle(prozor, pg.Color("Maroon"), (220, 100), 65, 0)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

