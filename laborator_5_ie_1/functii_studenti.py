#1.Suma cifrelor
def suma_cifrelor(n: int) -> str:
    n=abs(n)
    suma=0
    for cifra in str(n):
        suma=suma+int(cifra)
    return f"Suma cifrelor lui {n} este {suma}."