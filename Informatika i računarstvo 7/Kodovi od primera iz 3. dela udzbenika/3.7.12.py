import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,200))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))

#ELIPSA BOJE PARADAJZA
pg.draw.ellipse(prozor, pg.Color("Tomato"), (10, 10, 200, 100), 4)
#ELIPSA ISPUNJENA BOJOM ŠLJIVE
pg.draw.ellipse(prozor, pg.Color("Plum"), (220, 60, 70, 120), 0)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

