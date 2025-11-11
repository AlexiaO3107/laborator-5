#16.
def timp_in_format(secunde: int) -> str:
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde înseamnă {h}:{m}:{s}."

def produs_scalar(v1: list[float], v2: list[float]) -> str:
    """
    Calculează produsul scalar al celor doi vectori (liste de aceeași lungime).
    Dacă lungimile diferă, returnează un mesaj de eroare.
    Exemplu: "Produsul scalar este 14.0."
    """
    if len(v1) != len(v2):
        return "Eroare: vectorii trebuie să aibă aceeași lungime."


    produs = sum(a * b for a, b in zip(v1, v2))

    return f"Produsul scalar este {produs}."

#functia nr.3
def cmmmc(a: int, b: int) -> str:
    if a == 0 or b == 0:
        return "Eroare: unul dintre numere este 0."
def cmmc(a, b):
    multiplu = max(a, b)
    while True:
        if multiplu % a == 0 and multiplu % b == 0:
            return multiplu
        multiplu += 1

def numar_divizori(n: int) -> str:
    if n <= 0:
        return "Eroare: numarul trebuie sa fie mai mare decat 0"
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return f"Numărul de divizori ai lui {n} este {count}."
#Functia 19
from collections import Counter
from typing import List
def numar_unic(lista: List[int]) -> str:
    if not lista:
        return "Eroare: lista este goală."
    frecvente = Counter(lista)
    o_data = [num for num, cnt in frecvente.items() if cnt == 1]
    de_doua_ori = [num for num, cnt in frecvente.items() if cnt == 2]
    if len(o_data) == 1 and len(o_data) + len(de_doua_ori) == len(frecvente):
        return str(o_data[0])
    else:
        return "Eroare: condiția nu este respectată."
print(numar_unic([1, 2, 3, 2, 1]))
