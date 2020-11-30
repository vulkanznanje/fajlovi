import pygame as pg
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Kućica")
prozor.fill(pg.Color("white"))
pg.draw.rect(prozor, pg.Color("black"), (100, 180, 200, 120), 3)
pg.draw.rect(prozor, pg.Color("black"), (90, 161, 220, 20), 3)
pg.draw.rect(prozor, pg.Color("black"), (120, 300, 80, 20), 3)
pg.draw.rect(prozor, pg.Color("black"), (130, 280, 60, 20), 3)
pg.draw.rect(prozor, pg.Color("black"), (135, 200, 50, 81), 3)
pg.draw.rect(prozor, pg.Color("black"), (220, 200, 50, 50), 3)
pg.draw.rect(prozor, pg.Color("black"), (220, 80, 30, 15), 3)
pg.draw.line(prozor, pg.Color("black"), (225, 93), (225,130), 3)
pg.draw.line(prozor, pg.Color("black"), (243, 93), (243,130), 3)
pg.draw.line(prozor, pg.Color("black"), (244, 200), (244,250), 3)
pg.draw.line(prozor, pg.Color("black"), (220, 225), (270,225), 3)
pg.draw.circle(prozor, pg.Color("black"), (175, 240), 5, 2)
temenaKrov = (90,161), (150,50), (250,50), (310,161)
pg.draw.polygon(prozor, pg.Color("black"),temenaKrov, 3)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


