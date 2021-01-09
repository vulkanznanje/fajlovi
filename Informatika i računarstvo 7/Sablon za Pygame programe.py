import pygame as pg
pg.init()
prozor = pg.display.set_mode((300,300))
pg.display.set_caption("Naslov")
prozor.fill(pg.Color("White"))

#FUNKCIJE ZA CRTANJE OBLIKA:
#pg.draw.line(prozor, pg.Color("boja"), (x, y), (x, y), debljina)
#pg.draw.lines(prozor, pg.Color("boja"), True/False, (koordinate temena), debljina)
#pg.draw.rect(prozor, pg.Color("boja"), (x, y, a, b), debljina)
#pg.draw.circle(prozor, pg.Color("boja"), (x, y), r, debljina)
#pg.draw.ellipse(prozor, pg.Color("boja"), (x, y, a, b), debljina)
#pg.draw.arc(prozor, pg.Color("boja"), (x, y, a, b), ugaoOD, ugaoDO, debljina)
#pg.draw.polygon(prozor, pg.Color("boja"), (koordinate temena), debljina)

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()


