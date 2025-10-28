# sirul_de_caractere = "Exemplu de sir de caractere"
# for caracter in sirul_de_caractere:
# 	print(caracter)
# print(sirul_de_caractere[0])

# LISTE
lista_de_numere = [10, 20, 30, 40, 50]
lista_diversa = [1, "text", 3.14, True, [1, 2, 3]]

# indexarea elementelor din lista
# primul element are indexul 0

print(lista_de_numere[0])
print(lista_de_numere[-1])

print(lista_de_numere[2])


# segmentare/ slicing liste
sublista = lista_de_numere[1:4:2]  # elementele cu index
print(sublista)

# operatorii + si *

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
print(lista_1+lista_2)

# inmultirea cu un numar intreg = repetare
print(lista_1*3)
sir = "abc"
print(sir*4)

# adaugare element in lista
# append(element)
# adauga elementul la finalul listei
lista_1.append(10)
print(lista_1)

# insert(index, element)
lista_1.insert(2, 77)
print(lista_1)


# stergere elemente din lista
# pop(index)
# sterge si returneaza elementul de la indexul dat

element_sters = lista_1.pop(2)
print(lista_1)
print(element_sters)

# remove(element)
# sterge prima aparitie a elementului dat
lista_1 = [1, 2, "3", 2, 4, 3]
lista_1.remove("3")
print(lista_1)

# gasirea elementelor in lista
# index(element)
# returneaza indexul primei aparitii a elementului dat
lista_1 = [1, 2, "3", 2, 4, 3]
index_element = lista_1.index(2)
print(index_element)

# count(element)
# returneaza de cate ori apare elementul in lista
print(lista_1.count(3))

# sort()
# modifica lista initiala
lista_de_numere = [50, 20, 10, 40, 30]
print(lista_de_numere)
lista_de_numere.sort()
print(lista_de_numere)
lista_de_numere.sort(reverse=True)
print(lista_de_numere)

print("------------------")
# sorted(lista)
# returneaza o alta cu elementele sortate
lista_de_numere = [50, 20, 10, 40, 30]
print(lista_de_numere)

lista_sortata = sorted(lista_de_numere)
print(lista_sortata)
print(lista_de_numere)

# len(lista)
# returneaza numarul de elemente din lista
print(len(lista_de_numere))

# max(lista)
# returneaza valoarea maxima din lista
print(max(lista_de_numere))

# min(lista)
# returneaza valoarea minima din lista
print(min(lista_de_numere))

# sum(lista)
# returneaza suma elementelor din lista
print(sum(lista_de_numere))

# media aritmetica a elementelor din lista
media = sum(lista_de_numere) / len(lista_de_numere)
print(media)

print("------------------")
lista_de_numere = [10, 20, 30, 40, 50]
# parcurgerea elementelor din lista
# metoda 1 - for element in lista
for element in lista_de_numere:
	print(element)

print("------------------")
# afisati elementele mai mari decat 30
for element in lista_de_numere:
	if element > 30:
		print(element)

lista_de_numere = [101, 202, 32, 43, 50]
# lista_de_numere[0] = 10
# lista_de_numere[1] = 20
# lista_de_numere[2] = 30
# lista_de_numere[3] = 40
# lista_de_numere[4] = 50
print("------------------")
# metoda 2 - for index in range(len(lista))
for index in range(len(lista_de_numere)):
	print(index, lista_de_numere[index])
# afisati elementele pare de pozitiile impare
print("------------------")
for index in range(len(lista_de_numere)):
	# pozitia e index
	# valoarea e lista_de_numere[index]
	if lista_de_numere[index] % 2 == 0 and index % 2 == 1:
		print(lista_de_numere[index])

# parcurgere cu while
lista_de_numere = [10, 20, 30, 40, "stop", 50]
print("------------------")

# pozitie cu pozitie
index = 0
while lista_de_numere[index] != "stop":
	print(lista_de_numere[index])
	index += 1