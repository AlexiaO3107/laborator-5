#Functie Filtreaza Pare (6)
def filtreaza_pare(lista):
    ok=0
    for numar in lista:
        if numar%2==0:
            print(numar)
            ok=1
    if ok==0:
        print("Nu exista numere pare.")
