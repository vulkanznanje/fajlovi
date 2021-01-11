#Poruka dobrodošlice i objašnjenje kako se odgovara na pitanja
print("""Dobrodošli u test iz biologije! Odgovore unosite malim slovima abecede.
Tačan odgovor donosi 4 poena, a netačan -1 (1 negativan poen).
Ako niste sigurni napišite Ne znam ili samo pritisnite Enter. SREĆNO!!!\n""")
#Lista sa pitanjima
Pitanja = ["Ćelija vrši razmenu supstanci sa spoljašnjom sredinom preko:",
           "Koliko hromozoma imaju ljudske ćelije?",
           "Od koje vrste mišićnog tkiva je izgrađeno tanko crevo?"]
#Lista sa ponudjenim odgovorima na pitanja
PonudjeniOdgovori = ["a)jedra \nb)membrane \nc)mitohondrija \nd)citoplazme \n",
                     "a)23 \nb)38 \nc)46 \nd)52 \n",
                     "a)glatko \nb)srčano \nc)poprečno-prugasto \nd)vlaknasto \n"]
#Lista sa tačnim odgovorima
TacniOdgovori = ["b","c","а"]
#Lista sa tačnim odgovorima u formi iskazne rečenice
PunOdgovor = ["Ćelija vrši razmenu supstanci sa spoljašnjom sredinom preko membrane.\n",
              "Ljudske ćelije imaju 46 hromozoma.\n",
              "Tanko crevo je izgrađeno od glatkog mišićnog tkiva.\n"]
Poeni = 0 #Vrednost promenljive za proračun broja poena je na početku 0
#Brojačka petlja za prolazak kroz 4 liste sa ugnježdenim grananjem
for i in range(len(Pitanja)):
    print(Pitanja[i])
    Odgovor = input(PonudjeniOdgovori[i])
    if Odgovor == TacniOdgovori[i]:
        print("Tačan odgovor!\n")
        Poeni = Poeni + 4
    elif Odgovor == "" or Odgovor == "Ne znam" or Odgovor == "ne znam":
        print("Tačan odgovor glasi:", PunOdgovor[i])
    else:
        print("Netačno! Tačan odgovor glasi:", PunOdgovor[i])      
        Poeni = Poeni - 1
#Poruka o osvojenom broju poena
print("Osvojili ste:", Poeni, "od 12 poena.")

