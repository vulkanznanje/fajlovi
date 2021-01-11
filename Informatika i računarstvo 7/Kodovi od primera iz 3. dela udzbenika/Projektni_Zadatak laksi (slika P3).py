print("Dobrodošli u test iz biologije! Odgovore unosite malim slovima abecede. SREĆNO!!!\n")

Poeni = 0
print("Ćelija vrši razmenu supstanci sa spoljašnjom sredinom preko:")
Odgovor1 = input("a)jedra \nb)membrane \nc)mitohondrija \nd)citoplazme \n")
if Odgovor1 == "b":
    print("Tačan odgovor!\n")
    Poeni = Poeni + 1
else:
    print("Netačno! Ćelija vrši razmenu supstanci sa spoljašnjom sredinom preko membrane.\n")

print("Koliko hromozoma imaju ljudske ćelije?")
Odgovor2 = input("a)23 \nb)38 \nc)46 \nd)52 \n")
if Odgovor2 == "c":
    print("Tačan odgovor!\n")
    Poeni = Poeni + 1
else:
    print("Netačno! Ljudske ćelije imaju 46 hromozoma.\n")

print("Od koje vrste mišićnog tkiva je izgrađeno tanko crevo?")
Odgovor3 = input("a)glatko \nb)srčano \nc)poprečno-prugasto \nd)vlaknasto \n")
if Odgovor3 == "a":
    print("Tačan odgovor!\n")
    Poeni = Poeni + 1
else:
    print("Netačno! Tanko crevo je izgrađeno od glatkog mišićnog tkiva.\n")

Procenti = (Poeni/3)*100
print("Odgovorili ste tačno na:", Poeni, "od 3 pitanja.")
print("Vaš procenat uspešnosti je:", Procenti,"%")


