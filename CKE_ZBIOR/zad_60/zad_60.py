# Zadanie 60.
# Wiązka zadań lista
# W pliku liczby.txt danych jest 200 różnych liczb całkowitych z przedziału [2, 1 000
# 000], każda w osobnym wierszu pliku. Napisz program (lub kilka programów), który poda
# odpowiedzi do poniższych zadań. Odpowiedzi zapisz do pliku wyniki.txt.


# 60.1.
# Policz, ile jest w pliku wejściowym liczb mniejszych niż 1000, oraz podaj dwie takie liczby,
# które pojawiają się w pliku jako ostatnie (możesz założyć, że będą co najmniej dwie).

# lista = []
# with open("C:/Users/infotech/vscProjects/INFORMATYKA/CKE_ZBIOR/zad_60/liczby.txt", "r") as plik:
#     for liczba in plik.readlines():
#         lista.append(int(liczba))
#     licznik = 0
#     l1=0
#     l2=0
#     for i in lista:
#         if i<1000:
#             licznik+=1
#             l1=l2
#             l2=i
#     print(licznik,l1,l2)

# 60.2.
# Wśród liczb występujących w pliku wejściowym znajdź te, które mają dokładnie 18 dzielni-
# ków naturalnych (wliczając w nie 1 i samą liczbę). Dla każdej znalezionej liczby wypisz,
# oprócz jej wartości, listę wszystkich jej dzielników, posortowaną rosnąco.

# def funkcja(liczba):
#     lista = []
#     for i in range(1, int(liczba**0.5) + 1):
#         if liczba % i == 0:
#             lista.append(i)
#             if i != liczba // i:
#                 lista.append(liczba // i)
#     return lista

# with open("C:/Users/infotech/vscProjects/INFORMATYKA/CKE_ZBIOR/zad_60/liczby.txt", "r") as plik:
#     liczby = [int(l.strip()) for l in plik.readlines()]

# lista_z_18_dzielnikow = []

# for liczba in liczby:
#     lista = funkcja(liczba)
#     if len(lista) == 18:
#         lista_z_18_dzielnikow.append((liczba, sorted(lista)))

# for liczba, lista in lista_z_18_dzielnikow:
#     print(liczba , lista, "\n")

# 60.3.
# Znajdź największą liczbę w pliku, która jest względnie pierwsza ze wszystkimi pozostałymi, 
# czyli taką, która z żadną z pozostałych liczb nie ma wspólnego dzielnika innego niż 1.

# def nwd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x

# with open("C:/Users/infotech/vscProjects/INFORMATYKA/CKE_ZBIOR/zad_60/liczby.txt", "r") as plik:
#     liczby = [int(l.strip()) for l in plik.readlines()]

# najwieksza = 0
# for i in range(len(liczby)):
#     ok = True
#     for j in range(len(liczby)):
#         if i != j and nwd(liczby[i], liczby[j]) > 1:
#             ok = False
#             break
#     if ok and liczby[i] > najwieksza:
#         najwieksza = liczby[i]

# print(najwieksza)