import pygame as pg
import math
pg.init()
prozor = pg.display.set_mode((400, 400))
pg.display.set_caption("Čiča Gliša")
prozor.fill(pg.Color("white"))
pg.draw.circle(prozor, pg.Color("black"), (200, 100), 40, 3) #GLAVA
pg.draw.line(prozor, pg.Color("black"), (200, 140), (200,250), 3) #TELO
pg.draw.line(prozor, pg.Color("black"), (200, 250), (170,350), 3) #NOGA L
pg.draw.line(prozor, pg.Color("black"), (200, 250), (230,350), 3) #NOGA D
pg.draw.line(prozor, pg.Color("black"), (200, 170), (140,230), 3) #RUKA L
pg.draw.line(prozor, pg.Color("black"), (200, 170), (260,230), 3) #RUKA D
pg.draw.rect(prozor, pg.Color("black"), (180, 20, 40, 40)) #ŠEŠIR CILINDAR
pg.draw.line(prozor, pg.Color("black"), (160, 60), (240,60), 4) #ŠEŠIR OBOD
pg.draw.circle(prozor, pg.Color("black"), (185, 90), 6, 3) #OKO LEVO
pg.draw.circle(prozor, pg.Color("black"), (215, 90), 6, 3) #OKO DESNO
#USTA
elipsa = (180, 105, 40, 20)
pg.draw.arc(prozor, pg.Color("black"), elipsa, math.radians(180), math.radians(360), 5)
#DESNI DEO LEPTIR-MAŠNE
temena1 = ((185,150), (185,160), (205,155))
pg.draw.polygon(prozor, pg.Color("red"), temena1)
#LEVI DEO LEPTIR-MAŠNE
temena2 = ((195,155), (215,150), (215,160))
pg.draw.polygon(prozor, pg.Color("red"), temena2)
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()



