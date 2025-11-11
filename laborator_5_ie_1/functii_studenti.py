from typing import List
def rotire_dreapta(lista: List[int], k: int) -> str:
     if not lista:
         return "Lista este goală."
     k = k % len(lista)
     if k == 0:
         lista_rotita = lista
     else:
         lista_rotita = lista[-k:] + lista[:-k]
     return "Lista rotită: " + ", ".join(str(x) for x in lista_rotita)