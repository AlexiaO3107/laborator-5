# functii_studenti.py

def suma_cifrelor(n: int) -> str:
    try:
        s = sum(int(c) for c in str(abs(n)))
        return f"Suma cifrelor lui {n} este {s}."
    except Exception:
        return "Eroare: argument invalid."

def cmmdc(a: int, b: int) -> str:
    if a == 0 and b == 0:
        return "Eroare: CMMDC(0, 0) nu este definit."
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    return f"CMMDC({a}, {b}) = {x}."

def cmmmc(a: int, b: int) -> str:
    if a == 0 or b == 0:
        return "Eroare: CMMMC nu este definit pentru valori nule."
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    c = abs(a * b) // gcd(a, b)
    return f"CMMMC({a}, {b}) = {c}."

def numar_divizori(n: int) -> str:
    if n <= 0:
        return "Eroare: n trebuie să fie pozitiv."
    d = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d += 2 if i != n // i else 1
    return f"Numărul de divizori ai lui {n} este {d}."

def lista_prime_pana_la(n: int) -> str:
    if n < 2:
        return "Nu există numere prime până la această valoare."
    def prim(x):
        if x < 2: return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    primes = [str(i) for i in range(2, n + 1) if prim(i)]
    if not primes:
        return "Nu există numere prime."
    return f"Numere prime până la {n}: {', '.join(primes)}"

def filtreaza_pare(lista: list[int]) -> str:
    if not lista:
        return "Lista este goală."
    pare = [str(x) for x in lista if x % 2 == 0]
    return f"Numere pare: {', '.join(pare)}" if pare else "Nu există numere pare."

def produs_scalar(v1: list[float], v2: list[float]) -> str:
    if len(v1) != len(v2):
        return "Eroare: vectorii trebuie să aibă aceeași lungime."
    produs = sum(a * b for a, b in zip(v1, v2))
    return f"Produsul scalar este {produs}."

def medie_ponderata(valori: list[float], ponderi: list[float]) -> str:
    if len(valori) != len(ponderi) or not valori or sum(ponderi) <= 0:
        return "Eroare: liste invalide sau suma ponderilor ≤ 0."
    media = sum(v * p for v, p in zip(valori, ponderi)) / sum(ponderi)
    return f"Media ponderată este {media}."

def rotire_dreapta(lista: list[int], k: int) -> str:
    if not lista:
        return "Lista este goală."
    k %= len(lista)
    rotita = lista[-k:] + lista[:-k]
    return f"Lista rotită: {', '.join(map(str, rotita))}"

def interclaseaza(l1: list[int], l2: list[int]) -> str:
    i = j = 0
    rezultat = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            rezultat.append(l1[i])
            i += 1
        else:
            rezultat.append(l2[j])
            j += 1
    rezultat.extend(l1[i:])
    rezultat.extend(l2[j:])
    return f"Interclasare: {', '.join(map(str, rezultat))}"

def elimina_duplicate(lista: list[int]) -> str:
    vazute = []
    for x in lista:
        if x not in vazute:
            vazute.append(x)
    return f"Fără duplicate: {', '.join(map(str, vazute))}"

def frecventa_litere(text: str) -> str:
    text = text.replace(" ", "")
    if not text:
        return "Nu există caractere de analizat."
    frec = {}
    for c in text:
        frec[c] = frec.get(c, 0) + 1
    perechi = [f"'{k}': {v}" for k, v in frec.items()]
    return ", ".join(perechi)

def cel_mai_frecvent_cuvant(text: str) -> str:
    cuvinte = text.lower().split()
    if not cuvinte:
        return "Nu există cuvinte în text."
    frec = {}
    for c in cuvinte:
        frec[c] = frec.get(c, 0) + 1
    cuv, nr = max(frec.items(), key=lambda x: x[1])
    return f"Cel mai frecvent cuvânt este '{cuv}' (apariții: {nr})."

def este_isograma(text: str) -> str:
    litere = [c.lower() for c in text if c.isalpha()]
    if len(litere) == len(set(litere)):
        return f"'{text}' este isogramă."
    else:
        return f"'{text}' NU este isogramă."

def numere_distincte(lista: list[int]) -> str:
    if not lista:
        return "Lista este goală."
    if len(lista) == len(set(lista)):
        return "Toate numerele din listă sunt distincte."
    return "Lista conține elemente care se repetă."

def timp_in_format(secunde: int) -> str:
    if secunde < 0:
        return "Eroare: numărul de secunde trebuie să fie nenegativ."
    h = secunde // 3600
    m = (secunde % 3600) // 60
    s = secunde % 60
    return f"{secunde} secunde înseamnă {h:02d}:{m:02d}:{s:02d}."

def parola_valida(parola: str) -> str:
    if len(parola) < 8:
        return "Parola este invalidă: prea scurtă."
    if not any(c.isalpha() for c in parola):
        return "Parola este invalidă: nu conține litere."
    if not any(c.isdigit() for c in parola):
        return "Parola este invalidă: nu conține cifre."
    return "Parola este validă."

def in_binar(n: int) -> str:
    if n < 0:
        return "Eroare: numărul trebuie să fie nenegativ."
    return f"Reprezentarea în baza 2 a lui {n} este {bin(n)[2:]}."

def numar_unic(lista: list[int]) -> str:
    if not lista:
        return "Eroare: lista este goală."
    from collections import Counter
    frec = Counter(lista)
    unice = [k for k, v in frec.items() if v == 1]
    if len(unice) != 1:
        return "Eroare: condiția nu este respectată (trebuie exact un element unic)."
    return f"Numărul unic este {unice[0]}."

def sunt_anagrame(a: str, b: str) -> str:
    a_filtrat = sorted(a.replace(" ", "").lower())
    b_filtrat = sorted(b.replace(" ", "").lower())
    if a_filtrat == b_filtrat:
        return f"'{a}' și '{b}' sunt anagrame."
    return f"'{a}' și '{b}' nu sunt anagrame."
