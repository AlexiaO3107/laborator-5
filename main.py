# Bubble sort

# ne definim functia de bubble sort
# sortam o lista de numere, parametru lista

# pasii
# parcurgem lista pana la penultimul element
# verificam fiecare element cu urmatorul
# daca sunt in ordine, trecem mai departe
# daca nu sunt in ordine, le interschimbam
# facem asta cat timp lista nu e sortata sau cat timp am facut vreo interschimbare

lista = [64, 34, 25, 12, 22, 11, 90]
# [, 34,, 25, 12, 22, 11,64 90]

def bubble_sort(lista):
	interschimbat = True
	while interschimbat:
		interschimbat = False
		i = 0
		while i < len(lista) - 1:
			if lista[i] > lista[i+1]:
				# interschimbam
				lista[i], lista[i+1] = lista[i+1], lista[i]
				interschimbat = True
			i += 1
	print("Lista sortata:", lista)
	return lista

bubble_sort(lista)
