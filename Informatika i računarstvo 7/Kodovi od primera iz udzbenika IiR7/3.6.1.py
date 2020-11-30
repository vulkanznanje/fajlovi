import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,300))
pg.display.set_caption("Paralelne duži")
prozor.fill(pg.Color("Azure"))

pg.draw.line(prozor, pg.Color("Green"), (10, 50), (250, 290), 3)
pg.draw.line(prozor, pg.Color("Brown"), (50, 10), (290, 250), 10)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()


