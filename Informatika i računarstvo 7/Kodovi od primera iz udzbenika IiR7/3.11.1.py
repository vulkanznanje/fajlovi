import pygame as pg
pg.init()
s = 400
v = 400
prozor = pg.display.set_mode((s,v))
pg.display.set_caption("Dodavanje teksta")
prozor.fill(pg.Color("White"))
#font i veličina slova
font = pg.font.SysFont("Calibri", 40)
#string koji želiš da ispišeš
tekst = "Tekst u PYGAME-u!"
#promenljiva u kojoj čuvaš string i biraš boju slova
blokTeksta = font.render(tekst, True, pg.Color("Purple"))
#funkcija koja prikazuje tekst na odabranoj poziciji
prozor.blit(blokTeksta, (0,0))
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


