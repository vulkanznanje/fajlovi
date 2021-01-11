import pygame as pg
pg.init()
prozor = pg.display.set_mode((300, 300))
pg.display.set_caption("Trougao")
prozor.fill(pg.Color("White"))
pg.draw.line(prozor, pg.Color("Red"), (50,250), (150,50), 5)
pg.draw.line(prozor, pg.Color("Green"), (150,50), (250,250), 5)
pg.draw.line(prozor, pg.Color("Blue"), (250,250), (50,250), 5)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


