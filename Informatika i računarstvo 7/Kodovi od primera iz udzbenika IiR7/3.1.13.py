Broj = int(input("Unesi ceo broj: "))
if (Broj < 10): 
    print("Uneti broj je jednocifren.")
elif (Broj > 9 and Broj < 100): 
    print("Uneti broj je dvocifren.")
elif (Broj > 99 and Broj < 1000): 
    print("Uneti broj je trocifren.")
else:
    print("Uneti broj je veći od 999!")

