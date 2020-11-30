import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,300))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))

pg.draw.polygon(prozor, pg.Color("Purple"), ((50,250),(250,250),(150,50)),5)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

