#Functie Filtreaza Pare (6)
def filtreaza_pare(lista):
    numere_pare = []
    for numar in lista:
        if numar % 2 == 0:
            numere_pare.append(numar)
        if not numere_pare:
            return "nu exista numere pare."
        return numere_pare

def sumacif(n):
    s = 0
    c=n
    if n == 0:
        return 0
    else:
        while n!=0:
            s = s+(n%10)
            n//=10
    print (f"Suma cifrelor lui {c} este {s}")
sumacif(1234)

