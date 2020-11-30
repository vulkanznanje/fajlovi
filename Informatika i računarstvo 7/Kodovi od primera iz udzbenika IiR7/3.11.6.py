import pygame as pg
pg.init()
prozor = pg.display.set_mode((300, 300))
pg.display.set_caption("Dodavanje zvuka")
prozor.fill(pg.Color("White"))

#promenljiva u kojoj je smešten zvučni fajl
zvukAplauza = pg.mixer.Sound("aplauz.wav")
#reprodukcija fajla
zvukAplauza.play()

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


