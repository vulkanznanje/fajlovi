broj_učenika = int(input("Koliko je učenika prisutno u školi? "))
broj_bombona = int(input("Koliko je bombona u kesici? "))

bombona_po_učeniku = broj_bombona // broj_učenika
ostalo_bombona = broj_bombona % broj_učenika

print("Svaki učenik će dobiti", bombona_po_učeniku, "bombona.")
print("Ostalo je još", ostalo_bombona, "bombona.")
