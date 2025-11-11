<<<<<<< HEAD
#16.
def timp_in_format(secunde: int) -> str:
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde înseamnă {h}:{m}:{s}."

print(timp_in_format(555))
print(timp_in_format(-5))
=======

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

print(produs_scalar([1, 2, 3], [4, 5, 6]))

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
# Exemplu
a = 12
b = 18
print(f"Cel mai mic multiplu comun al lui {a} și {b} este {cmmc(a, b)}")
>>>>>>> c66a0608550b971401cb989164af585bfe633344
