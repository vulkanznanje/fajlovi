import math
a = int(input("Unesi dužinu stranice: "))
Odgovor = input("Šta želiš da izračunaš? h/O/P/R ")
if Odgovor == "h": 
    Visina = a*math.sqrt(3)/2
    print("Visina =", Visina)
elif Odgovor == "O":
    Obim = a*3
    print("Obim =", Obim)
elif Odgovor == "P":
    Povrsina = a**2*math.sqrt(3)/4
    print("Površina =", Povrsina)
elif Odgovor == "R":
    PoluprecnikO = a*math.sqrt(3)/3
    print("Poluprečnik opisanog kruga =", PoluprecnikO)
else:
    print("Uneli ste pogrešan karakter!")

