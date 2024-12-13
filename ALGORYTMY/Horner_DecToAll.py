def horner(liczba, podstawa):  
    dziesietny=int(liczba[0])
    for i in range(1,len(liczba)):
        dziesietny=dziesietny*podstawa + int(liczba[i])
    return dziesietny

def decToALL(dziesietna,system_docelowy):
    wynik=""
    while dziesietna>0:
        wynik=str(dziesietna%system_docelowy) + wynik 
        dziesietna=dziesietna // system_docelowy
    return wynik

liczba = "1011"  
podstawa = 2     
system_docelowy = 8  

dziesietna = horner(liczba, podstawa)
print(f"Liczba {liczba} w systemie {podstawa} to {dziesietna} w dziesiętnym.")

wynik = decToALL(dziesietna, system_docelowy)
print(f"Liczba {dziesietna} w systemie {system_docelowy} to {wynik}.")