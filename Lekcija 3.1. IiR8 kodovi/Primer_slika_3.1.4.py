import pandas as pd
Podaci = [[1, "Una",    "Zorić",       161, 45, 25],
          [2, "Marta",  "Stojanović",  165, 53, 16],
          [3, "Ognjen", "Novaković",   171, 64,  5],
          [4, "Petra",  "Kaličanin",   159, 48, 21],
          [5, "Novak",  "Đorđević",    175, 67, 28],
          [6, "Đurđe",  "Martać",      178, 65, 25],
          [7, "Kalina", "Ognjenović",  170, 62, 25],
          [8, "Vanja",  "Čolović",     181, 72, 26]]
Tabela = pd.DataFrame(Podaci)
Tabela.columns=["R. br.", "Ime", "Prezime", "Visina", "Težina", "Čučnjevi"]
print(Tabela)
print()
print("Najniži takmičar ima:", Tabela["Visina"].min(), "cm")
print("Najteži takmičar ima:", Tabela["Težina"].max(), "kg")
print("Prosečan broj čučnjeva je:", Tabela["Čučnjevi"].mean())



