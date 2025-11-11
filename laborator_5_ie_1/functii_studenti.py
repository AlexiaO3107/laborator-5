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