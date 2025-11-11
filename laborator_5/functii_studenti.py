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