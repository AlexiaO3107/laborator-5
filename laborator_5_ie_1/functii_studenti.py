#4. numar_divizori(n: int) -> str
#Determină numărul divizorilor pozitivi ai lui n.
#Pentru n <= 0, mesaj de eroare.
#Exemplu: "Numărul de divizori ai lui 6 este 4."

def numar_divizori(n: int) -> str:
    if n <= 0:
        return "Eroare: numarul trebuie sa fie mai mare decat 0"
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return f"Numărul de divizori ai lui {n} este {count}."