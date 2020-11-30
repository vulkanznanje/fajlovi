import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Crtanje duži")
prozor.fill(pg.Color("White"))
pg.draw.line(prozor, pg.Color("Blue"), (50, 100), (250, 100), 5)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


