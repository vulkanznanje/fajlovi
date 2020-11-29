sekundi = int(input("Unesi vreme u sekundama: "))
h = sekundi // 3600
m = (sekundi%3600)//60
s = (sekundi%3600)%60

print("Uneto vreme je:", h, "sat/i", m, "minuta i", s, "sekundi.")
