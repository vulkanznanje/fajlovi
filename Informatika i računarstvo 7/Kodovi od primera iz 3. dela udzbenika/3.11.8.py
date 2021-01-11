import pygame as pg
pg.init()
prozor = pg.display.set_mode((300, 300))
pg.display.set_caption("Dodavanje muzike")
prozor.fill(pg.Color("White"))

pg.mixer.music.load("Decak iz vode.mp3")
pg.mixer.music.play(-1)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()
