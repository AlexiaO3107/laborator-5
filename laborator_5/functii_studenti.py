#Functie Filtreaza Pare (6)
def filtreaza_pare(lista):
    ok=0
    for numar in lista:
        if numar%2!=0:
            lista.pop(numar)
        if numar%2==0:
            ok=1
    if ok==0:
        return "nu exista numere pare"
    return lista


