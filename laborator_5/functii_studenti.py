#FUNCTIA 5
def lista_prime_pana_la(n: int) -> str:
    prime = []

    #  pana la 2
    for numar in range(2, n + 1):
        este_prim = True  # daca prim

        # verificam
        for divizor in range(2, numar):
            if numar % divizor == 0:
                este_prim = False
                break

        # daca prim
        if este_prim:
            prime.append(str(numar))

    if len(prime) == 0:
        return f"Nu exista numere prime pana la {n}."
    else:
        return f"Numere prime pana la {n}: " + ", ".join(prime)     # daca gol


print(lista_prime_pana_la(20))

# media poderata (8)
def medie_ponderata(valori: list[float], ponderi: list[float]):
    if len(list) != len(ponderi):
        print("error")
    suma_produse = sum(valoare * ponderi for valoare, ponderi in zip(list, ponderi))
    suma_ponderi = sum(ponderi)
    if suma_ponderi == 0:
        return print("error ponderea este 0")

def cmmmc(a,b):
    produs = a*b
    if produs == 0:
        return "Imposibil"
    else:
        while a != b:
            if a > b:
                a-=b
            else
                b-=a
        return produs//a