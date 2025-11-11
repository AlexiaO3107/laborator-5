#

# Functii sau subprograme

# Sintaxa
def nume_functie(parametru1, parametr_2):   # parametrii optionali
    # bloc de cod
    # ...
    return # optional

# exemplu functie care aduna 2 numere
def aduna_numere(numar1, numar2):
    print("Se aduna numerele in functia aduna_numere")
    suma = numar1 + numar2
    return suma

def functie_de_testare():
    print("Aceasta este o functie de testare")

# parametrii cu *args
# folosim cand nu stim cati parametrii vom primi

def suma_numere(*args):
    print(args)
    for numar in args:
        print(numar)
    return sum(args)

# parametrii cu **kwargs
# keyword arguments - dictionar de parametrii
def afisare_informatii(**kwargs):
    print(kwargs)
    for cheie, valoare in kwargs.items():
        print(f"{cheie}: {valoare}")

# parametru pozitional cu /
# restrictionam modul de apelare a functiei
def functie_parametru_pozitional(parametru1, parametru2, /):
    print(f"Parametru 1: {parametru1}, Parametru 2: {parametru2}")

# parametrii predefiniti
def functie_parametru_predefinit(x, parametru1=10, parametru2=5):
    print(f"Parametru 1: {parametru1}, Parametru 2: {parametru2}")
    print(f"x: {x}")

# variabile globale si locale

# variabile globale - definite in afara oricarei functii sau in main
# variabile locale - definite in interiorul unei functii

# in python, se cauta intai in variabilele locale, apoi in cele globale

def f1():
    x = 5
    print(f"Interior f1: {x}")
def f2():
    print(f"Interior f2: {x}")

# in python avem 2 tipuri muttabile si immutable
# muttabile: liste, dictionare, seturi
# immutable: int, float, str, tuple
def functie_care_modifica_parametrii(lista, numar):
    # daca nu vrem sa se modifice lista, facem o copie

    numar *= 1000

    for i in range(len(lista)):
        lista[i] *= numar

    print("in functie")
    print(lista)
    print(numar)

# exemplu functie care verifica daca un numar e prim sau nu
# trebuie sa aiba doar 2 divizori: 1 si el insusi   13 : 1 = 13 rest 0    13: 13 = 1 rest 0
# numaram numarul de divizori
# parametrii (datele de intrare): numar
# return True - daca e prim, False - daca nu e prim
def prim(numar):
    nr_divizori = 0
    for i in range(1, numar+1):
        if numar % i == 0:
            nr_divizori += 1
    if nr_divizori == 2:
        return True
    else:
        return False

if __name__ == '__main__':
    # print(aduna_numere(5, 10))
    # print(aduna_numere(9, 11))
    # functie_de_testare()
    # print(suma_numere(10,2))
    # afisare_informatii(nume="Ion", varsta=30)
    # functie_parametru_pozitional(20, 10)
    # x = 10
    # f1()
    # f2()
    # print(f"main:{x}")
    # lista = [1, 2, 3]
    # numar = 10
    # print("inainte de functie")
    # print(lista)
    # print(numar)
    # functie_care_modifica_parametrii(lista, numar)
    # print("dupa functie")
    # print(lista)
    # print(numar)
    #

    print(prim(110))
    # fie o lista de numere, sa se afiseze doar numerele prime
    lista_de_numere = [10, 15, 23, 42, 7, 9, 11, 13, 4]
    for numar in lista_de_numere:
        if prim(numar):
            print(numar)