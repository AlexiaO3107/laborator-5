#Functie Filtreaza Pare (6)
def filtreaza_pare(lista):
    ok=0
    for numar in lista:
        if numar%2!=0:
            lista.remove(numar)
        if numar%2==0:
            ok=1
    if ok==0:
        return "nu exista numere pare."
    return lista



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

# media poderata (8)
def medie_ponderata(valori: list[float], ponderi: list[float]):
    if len(lista) != len(ponderi)
        print("error")
    suma_produse = sum(valoare * pondere for valoare, ponderi in zip(lista, ponderi))
    suma_ponderi = sum(ponderi)
    if suma_ponderi == 0:
        return print("error ponderea este 0")

def cmmmc(a,b):
    produs = a*b
    if produs == 0:
        return "Eroare"
    else:
        while a != b:
            if a > b:
                a-=b
            else
                b-=a
        return produs//a
