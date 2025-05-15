with open("CKE/zad_73/tekst.txt") as plik:
    tekst = plik.readline()
print(tekst)
ile = 0
napisy = tekst.split()
for napis in napisy:
    for i in range(len(napis) - 1):
        if napis[i] == napis[i+1]:
            ile += 1
            break
print(ile)
slownik = {}
for znak in tekst:
    if znak != " " and znak != "\n":
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1

suma = slownik.values()
zmiennaaaa = 0
for v in slownik.values():
    zmiennaaaa += v
print(zmiennaaaa)

lista = sorted(slownik.items())
for kr in lista:
    print(kr[0], ":", kr[1], round(100 * kr[1]/zmiennaaaa, 2), "%")

# print(sum(suma))

samogloski = ['A', 'E', 'I', 'O', 'U', 'Y']
maks = 0
ileNapisow = 0
for napis in napisy:
    n = 0
    for litera in napis:
        if litera not in samogloski:
            n +=1
            if n > maks:
                maks = n
            else:
                n = 0
print(maks + 1)