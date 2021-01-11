Odgovor = input("Čiji obim želiš da izračunaš? T/K/P: ")
if Odgovor == "T":
    a = int(input("Unesi stranicu a: "))
    Obim_trougla = 3*a
    print ("Obim trougla je", Obim_trougla, "cm")
if Odgovor == "K":
    a = int(input("Unesi stranicu a: "))
    Obim_kvadrata = 4*a
    print ("Obim kvadrata je", Obim_kvadrata, "cm")
if Odgovor == "P":
    a = int(input("Unesi stranicu a: "))
    b = int(input("Unesi stranicu b: "))
    Obim_pravougaonika = 2*a + 2*b
    print ("Obim pravougaonika je", Obim_pravougaonika, "cm")



