#Napiši program koji će računati faktorijel unetog broja (n!).
#Faktorijel celog broja n predstavlja proizvod svih
#pozitivnih brojeva koji su manji ili jednaki n.

n = int(input("Unesi broj čiji faktorijel želiš: "))
Proizvod = 1
for i in range(1, n+1):
    Proizvod = Proizvod * i
    print(Proizvod) #međuproizvodi
print("Faktorijel broja", n, "je:", Proizvod)
