def jednolity(wyraz):
    for i in range(len(wyraz) - 1):
        if wyraz[i] != wyraz[i+1]:
            return False
    return True

lista_wyrazow = []
with open("CKE/ZAD_68/dane_napisy.txt") as plik:
    for linia in plik:
        lista_wyrazow.append(linia.split())

print(lista_wyrazow)

licznik = 0
for wyrazy in lista_wyrazow:
    if wyrazy[0] == wyrazy[1]:
        if jednolity(wyrazy[0]):
            licznik += 1

print(licznik)
licznik = 0
for wyrazy in lista_wyrazow:
    if sorted(wyrazy[0]) == sorted(wyrazy[1]):
        licznik+=1
print(licznik)