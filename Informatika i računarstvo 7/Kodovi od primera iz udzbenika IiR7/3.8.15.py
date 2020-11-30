import pygame as pg
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Obojena glava robota")
prozor.fill(pg.Color("white"))
pg.draw.circle(prozor, pg.Color("blue"), (200, 35), 15)
pg.draw.circle(prozor, pg.Color("black"), (200, 35), 15, 3)
temenaKapica = ((180, 100), (220,100), (200,50))
pg.draw.polygon(prozor, pg.Color("red"), temenaKapica)
pg.draw.polygon(prozor, pg.Color("black"), temenaKapica, 3)
pg.draw.rect(prozor, pg.Color("grey"), (100, 100, 200, 150))
pg.draw.rect(prozor, pg.Color("black"), (100, 100, 200, 150), 3)
pg.draw.circle(prozor, pg.Color("white"), (150, 150), 17)
pg.draw.circle(prozor, pg.Color("black"), (150, 150), 20, 3)
pg.draw.circle(prozor, pg.Color("white"), (250, 150), 17)
pg.draw.circle(prozor, pg.Color("black"), (250, 150), 20, 3)
pg.draw.circle(prozor, pg.Color("black"), (146, 156), 12)
pg.draw.circle(prozor, pg.Color("black"), (246, 156), 12)
pg.draw.rect(prozor, pg.Color("white"), (150, 200, 100, 20))
pg.draw.rect(prozor, pg.Color("black"), (150, 200, 100, 20), 3)
pg.draw.rect(prozor, pg.Color("red"), (150, 250, 100, 50))
pg.draw.rect(prozor, pg.Color("black"), (150, 250, 100, 50), 3)
pg.draw.rect(prozor, pg.Color("blue"), (80, 150, 20, 50))
pg.draw.rect(prozor, pg.Color("black"), (80, 150, 20, 50), 3)
pg.draw.rect(prozor, pg.Color("blue"), (300, 150, 20, 50))
pg.draw.rect(prozor, pg.Color("black"), (300, 150, 20, 50), 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()



