def lista_prime_pana_la(n: int) -> str:
    prime = []

    #  toate numerele de la 2 până la n
    for numar in range(2, n + 1):
        este_prim = True  # presupunem că numărul este prim

        # verificăm dacă are vreun divizor (altul decât 1 și el însuși)
        for divizor in range(2, numar):
            if numar % divizor == 0:
                este_prim = False
                break

        # dacă este prim, îl adăugăm în listă
        if este_prim:
            prime.append(str(numar))

    if len(prime) == 0:
        return f"Nu există numere prime până la {n}."
    else:
        return f"Numere prime până la {n}: " + ", ".join(prime)     # dacă lista este goala


print(lista_prime_pana_la(20))
