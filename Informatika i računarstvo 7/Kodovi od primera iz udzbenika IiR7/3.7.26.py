import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,300))
pg.display.set_caption("Crtamo oblike")
prozor.fill(pg.Color("White"))

#Torka temena6 čuva koordinate temena šestougla
temena6 = ((50,150),(100,63),(200,63),(250,150),(200,237),(100,237))
pg.draw.polygon(prozor, pg.Color("RoyalBlue"), temena6, 3)
pg.display.update()

while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()

