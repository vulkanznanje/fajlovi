n = int(input("Unesi početak intervala: "))
m = int(input("Unesi kraj intervala: "))
Zbir = 0
for i in range(n, m+1):
    Zbir = Zbir + i
    print(Zbir)
print("Zbir celih brojeva u navedenom intervalu je:", Zbir)

