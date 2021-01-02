#Rad s datumima
#Datumi se u Python-u unose kao stringovi u formatu
#godina-mesec-dan. Više informacija o radu s datumima
#naći ćeš na zvaničnoj veb-adresi pandas biblioteke:
#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html
import pandas as pd
Rođendani = [[1, "Una",    "Zorić",      "2006-04-28"],
             [2, "Marta",  "Stanojević", "2006-09-13"],
             [3, "Ognjen", "Novaković",  "2006-05-01"],
             [4, "Petra",  "Kaličanin",  "2006-07-17"]]
Tabela = pd.DataFrame(Rođendani)
Tabela.columns=["R. br.", "Ime", "Prezime", "DatumRođenja"]
print("Najstariji učenik je rođen:", Tabela["DatumRođenja"].min())
#NAPOMENA: da vidiš rezultat naredbe print moraš sačuvati program
#pa ga pokrenuti. Nakon toga će rezultat biti vidljiv u konzoli.




