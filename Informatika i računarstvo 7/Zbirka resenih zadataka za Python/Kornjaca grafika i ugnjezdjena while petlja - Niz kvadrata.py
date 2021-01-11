#Kombinacijom while i for petlji nacrtaj niz kvadrata
#kojima se po jedna stranica dodiruje.

import turtle
turtle.color("Orange")
turtle.width(5)
duzina = 0
#stranica kvadrata je određena pomoću promenljive stranica 
stranica = 50
#kvadrati se crtaju do dužine od 5 stranica
while duzina < stranica*5:
       #jednim prolaskom kroz for petlju se crta jedan kvadrat
       for i in range(4):
              turtle.fd(stranica)
              turtle.rt(90)
       #nakon jednog prolaska kroz for petlju kornjača se pomera udesno za dužinu stranice,
       #a vrednost promenljive duzina se uvećava za datu dužinu stranice (promenljiva stranica)
       turtle.fd(stranica)
       duzina = duzina + stranica
