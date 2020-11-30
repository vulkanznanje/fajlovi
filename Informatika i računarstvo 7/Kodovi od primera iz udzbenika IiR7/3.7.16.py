import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))

pg.draw.arc(prozor, pg.Color("DarkViolet"), (50, 50, 200, 100), 0, 2.2, 5)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

