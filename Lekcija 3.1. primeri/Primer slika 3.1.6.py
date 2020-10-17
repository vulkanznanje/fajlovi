import matplotlib.pyplot as plt
Učenici = ["Una", "Marta", "Ognjen", "Petra",
"Novak", "Đurđe", "Kalina", "Vanja"]
Čučnjevi = [25, 16, 5, 21, 28, 25, 25, 26]
plt.bar(Učenici, Čučnjevi, color = "r")
plt.title("Čučnjevi")
plt.show()
plt.close()

