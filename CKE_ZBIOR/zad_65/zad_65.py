def nwd(a,b):
    while b !=0:
        temp = b
        b = a % b
        a = temp
    return a

liczniki = []
mianowniki = []
with open ("C://Users//infotech//vscProjects//INFORMATYKA//Informatyka_3at//CKE_ZBIOR//zad_65//dane_ulamki.txt", "r") as plik:
    for linia in plik.readlines():
        liczby = linia.split()
        liczniki.append(liczby[0])
        mianowniki.append(liczby[1])
print(liczniki)
print(mianowniki)
minimalny_ulamek = [liczniki[0],mianowniki[0]]
ulamek = []
for i in range(1,len(liczniki)):
    liczba = liczniki[i]/mianowniki[i]
    if liczba <= minimalny_ulamek[0]/minimalny_ulamek[1]:
        if liczba == minimalny_ulamek[0]/minimalny_ulamek[1]:
            if minimalny_ulamek[0]>liczniki[i]:
                minimalny_ulamek[0] = liczniki[0]
                minimalny_ulamek[1] = mianowniki[0]
        else:
            minimalny_ulamek[0] = liczniki[i]
            minimalny_ulamek[1] = mianowniki[i]
print(minimalny_ulamek)
licznik = 0
for i in range(len(liczniki)):
    if nwd(liczniki[i],mianowniki[i]) == 1:
        licznik += 1
print(licznik)

# zadanie 65.3

suma_licznikow = 0
for i in range(liczniki):
    licznik = liczniki[i]
    mianownik = mianowniki[i]
    while nwd(licznik,mianownik) != 1:
        liczba = nwd(licznik,mianownik)
        licznik = licznik // liczba
        mianownik = mianownik // liczba
    suma_licznikow += licznik
print(suma_licznikow)