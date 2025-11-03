# text = "...Lorem ipsum dolor sit amet, consectetur?! adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#
# # elimiare semne de punctuatie ?!.,
# text = text.replace("?", "").replace("!", "").replace(".", "").replace(",", "")
# print(text)
#
# # structuri decizionale: if, elif, else
#
# # if conditie:
# #     bloc de cod pentru True
# # elif alta_conditie:   # else if (altfel daca)
# #     bloc de cod pentru alta conditie True
# # else:
# #     bloc de cod pentru False
#
# numar = 0
#
# if numar > 0:
# 	print("Numarul este pozitiv")
# elif numar < 0:
# 	print("Numarul este negativ")
# else:
# 	print("Numarul este zero")
#
# # se da o nota, sa se afiseze daca a promovat sau nu
# nota = 8
# if nota >= 5:
# 	print("Promovat")
# else:
# 	print("Nepromovat")
#
# # se da un numar, sa se afiseze daca e par sau impar
# # un numar e par daca restul impartirii la 2 e 0
# # modulo: % operator care returneaza restul impartirii
# # conditia pentru paritate: numar % 2 == 0
#
# numar = 70
# if numar % 2 == 0:
# 	print("Numarul este par")
# else:
# 	print("Numarul este impar")
#
# # structuri repetitive: while, for
#
# # while: folosit cand nu stim dinainte de cate ori trebuie sa repetam un bloc de cod
# # sintaxa:
# # while conditie:
# #     bloc de cod
#
# numar = 5
# while numar > 0:
# 	print(numar)
# 	numar -= 1  # echivalent cu numar = numar - 1
#
# # cate cifre are un numar
# numar = 12345
# # cand numaram ceva, ne trebuie o variabila pentru a tine evidenta
# numar_cifre = 0
#
# # ca sa parcurgem cifrele unui numar, il impartim la 10 pana cand devine 0
# # numar = 10002
# # numar : 10 = 10002 : 10 = 1000 rest 2
# # numar : 10 = 1000 : 10 = 100 rest 0
# # ...
# # numar : 0 - oprim
#
# while numar > 0:
# 	numar = numar // 10   # tai o cifra din numar
# 	numar_cifre += 1
#
# print(numar_cifre)
#
# # for: folosit cand stim dinainte de cate ori trebuie sa repetam un bloc de cod
# # sintaxa:
# # for variabila in secventa:
# #     bloc de cod
#
# # range(start, stop, pas) - genereaza o secventa de numere
# # start - de unde incepem (inclusiv)
# # stop - unde ne oprim (exclusiv)
# # pas - cu cat crestem (optional, default 1)
#
# for i in range(0, 100, 2):
# 	print(i, end=" ")
#
# print()
# # sir de caractere - string
# # parcurgerea caracterelor unui string cu for
# text = "Hello world!"
# for caracter in text:
# 	print(caracter)
# print("----------------------")
# # parcurgere a caracterelor cu index
# for index in range(0, len(text), 1):
# 	print(text[index])

# range are valori predefinite
# start = 0 implicit
# pas = 1 implicit
# range(10) e echivalent cu range(0, 10, 1)

# afisam vocalele dintr-un text
print("----------------------")
text = "Azi este o zi frumoasa"
vocale = "aeiouAEIOU"
# 1. parcurgem textul caracter cu caracter
#   cu for

for index in range(len(text)):
	# index = pozitia caracterului curent
	# text[index] = caracterul curent
	# print(text[index])

	# 2. verificam daca caracterul curent e vocala
	# in - verifica daca un element se afla intr-o colectie (string, lista, set, dictionar)
	if text[index] in vocale:
		print(text[index])

# verificam daca sirul de caractere este gol
text1 = ""
text2 = "Hello"
# metoda 1 cu len()
# sirul e gol daca lungimea lui e 0
if len(text1) == 0:
	print("text1 e gol")

# metoda 2 verificam direct sirul
# un sir gol e considerat False in context boolean
if text1:
	print("text1 nu e gol")
else:
	print("text1 e gol")

# daca sirul poate sa fie cnp
# numarul de caractere trebuie sa fie exact 13 caractere  if len(cnp) == 13:
# trebuie sa contina doar cifre

cnp = "12A347890123"
conditie_1 = len(cnp) == 13

conditie_2 = True
for caracter in cnp:
	if caracter not in "0123456789":
		conditie_2 = False

if conditie_1 and conditie_2:
	print("CNP valid")
else:
	print("CNP invalid")

# numaram cate vocale sunt intr-un text
numar_vocale = 0
text = "Azi este o zi frumoasa"
vocale = "aeiouAEIOU"
for caracter in text:
	if caracter in vocale:
		numar_vocale += 1
print(numar_vocale)