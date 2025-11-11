# Bubble sort

lista_de_numere = [64, 34, 25, 12, 22, 11, 90]

# definim o functie bubble_sort
# parametru: lista
# luam primul element si il comparam cu urmatorii
# daca e mai mare, le interschimbam
# cat timp facem? pana cand nu mai sunt interschimbari

def bubble_sort(lista):
      n = len(lista)
      schimbat = True   # avem de facut de schimbari
      while schimbat:
            schimbat = False
            i = 0
            while i < n-1:
                  if lista[i] > lista[i+1]:
                        lista[i], lista[i+1] = lista[i+1], lista[i]     # swap/interschimbare
                        schimbat = True
                  i += 1
      print("Lista sortata este: ", lista)

bubble_sort(lista_de_numere)