# 61.1.
# Podaj, ile spośród podanych w pliku ciagi.txt ciągów jest ciągami arytmetycznymi.
# Znajdź wśród nich ciąg o największej różnicy i oblicz jego różnicę. Liczbę ciągów arytme-
# tycznych oraz największą różnicę zapisz w pliku wynik1.txt.

ciagi = []
with open("C://Users//infotech//vscProjects//INFORMATYKA//Informatyka_3at//CKE_ZBIOR//zad_61//ciagi.txt", "r") as plik:
    for linia in plik.readlines():
        liczby=[]
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
                ciagi.append(liczby)
print(ciagi)

max = 0
liczbaArytmetycznych = 0
for c in ciagi:
    roznica = c[1] - c[0]
    for i in range(2, len(c)):
        if c[i] - c[i-1] != roznica:
            break
    else:
         liczbaArytmetycznych += 1
         if roznica > max:
              max = roznica
print(liczbaArytmetycznych, max)

# 61.2.
# Dla każdego podanego ciągu znajdź — jeśli istnieje — największą występującą w nim liczbę,
# która jest pełnym sześcianem jakiejś liczby naturalnej 
# (w pierwszym z przykładowych ciągów jest to 1 = 13 , w drugim — 27 = 33 ).
# Znalezione liczby (po jednej dla każdego ciągu, w którym taka liczba występuje) zapisz
# w pliku wynik2.txt, w kolejności zgodnej z kolejnością ciągów, z których pochodzą.

ciagi = []
with open("C://Users//infotech//vscProjects//INFORMATYKA//Informatyka_3at//CKE_ZBIOR//zad_61//ciagi.txt", "r") as plik:
    for linia in plik.readlines():
        liczby=[]
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
                ciagi.append(liczby)
# print(ciagi)

max = 0
liczbaArytmetycznych = 0
for c in ciagi:
    roznica = c[1] - c[0]
    for i in range(2, len(c)):
        if c[i] - c[i-1] != roznica:
            break
    else:
         liczbaArytmetycznych += 1
         if roznica > max:
              max = roznica
print(liczbaArytmetycznych, max)

n = 1
szesciany = []
while n**3 < 1000000:
     szesciany.append(n**3)
     n+=1
print(szesciany)

# 61.3.
# Plik bledne.txt ma identyczną strukturę jak ciagi.txt, ale zawiera tylko 20 ciągów.
# Wiadomo jednak, że wszystkie występujące w nim ciągi są ciągami arytmetycznymi z jednym błędem: 
# jeden z wyrazów w każdym ciągu został zastąpiony przez liczbę naturalną nienależącą do ciągu.
# Dla każdego ciągu znajdź i wypisz błędny wyraz. Odpowiedzi zapisz w pliku wynik3.txt,
# podając dla każdego ciągu błędną liczbę w osobnym wierszu, w kolejności zgodnej z kolejno-
# ścią ciągów w pliku wejściowym.