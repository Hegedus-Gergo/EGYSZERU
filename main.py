import random

veletlen_szamok_listaja = []

for veletlen_szam in range(6):
    veletlen_szam = random.randint(1,15)
    veletlen_szamok_listaja.append(veletlen_szam)

print(veletlen_szamok_listaja)

for sorszam in range(0, len(veletlen_szamok_listaja)):
    for ertek in range(sorszam + 1, len(veletlen_szamok_listaja)):
        if veletlen_szamok_listaja[sorszam] > veletlen_szamok_listaja[ertek]:
            seged_valtozo1 = veletlen_szamok_listaja[sorszam]
            veletlen_szamok_listaja[sorszam] = veletlen_szamok_listaja[ertek]
            veletlen_szamok_listaja[ertek] = seged_valtozo1
            print(veletlen_szamok_listaja)

print(veletlen_szamok_listaja)