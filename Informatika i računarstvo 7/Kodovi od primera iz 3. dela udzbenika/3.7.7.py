import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))

pg.draw.rect(prozor, pg.Color("Salmon"), (50, 50, 200, 100), 0)
pg.draw.rect(prozor, pg.Color("DarkGreen"), (50, 50, 200, 100), 6)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

