# Date inițiale
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

# PARTEA A – Afișare și prelucrare

# A1. Listează elevii cu notele lor
print("Lista elevilor și notele lor:")
for i in range(len(elevi)):
    print("Elevul " + str(elevi[i]) + " are nota: " + str(note[i]))

# A2. Nota maximă și minimă
nota_maxima = max(note)
nota_minima = min(note)
print("\nNota maximă este: " + str(nota_maxima))
print("Elevii cu nota maximă sunt:")
for idx in range(len(note)):
    if note[idx] == nota_maxima:
        print(" - " + elevi[idx])

print("\nNota minimă este: " + str(nota_minima))
print("Elevii cu nota minimă sunt:")
for idx in range(len(note)):
    if note[idx] == nota_minima:
        print(" - " + elevi[idx])

# A3. Media clasei
suma_note = sum(note)
media_clasei = suma_note / len(note)
print("\nMedia clasei este: {:.2f}".format(media_clasei))

# A4. Promovați (nota ≥ 5)
print("\nElevii promovați (nota ≥ 5):")
for idx in range(len(note)):
    if note[idx] >= 5:
        print(" - " + elevi[idx])

# PARTEA B – Actualizări

# B5. +1 punct fiecărei note (maxim 10)
for idx in range(len(note)):
    note[idx] = min(note[idx] + 1, 10)
print("\nNotele după creștere cu 1 punct (max 10):")
print(note)

# B6. Adaugă elevul predefinit
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("\nDupă adăugarea lui " + elev_nou + ":")
print("Elevi:", elevi)
print("Note:", note)

# B7. Șterge elevul predefinit
if elev_de_sters in elevi:
    poz_sters = elevi.index(elev_de_sters)
    elevi.pop(poz_sters)
    note.pop(poz_sters)
    print("\nElevul " + elev_de_sters + " a fost șters din listă.")
else:
    print("\nElevul " + elev_de_sters + " NU există în listă, deci nu poate fi șters.")

# B8. Afișează din nou lista elev–notă
print("\nLista actualizată de elevi și note:")
for idx in range(len(elevi)):
    print("Elevul " + str(elevi[idx]) + " are nota: " + str(note[idx]))


# PARTEA C – Căutări și statistici

# C9. Căutări de nume cu while (până la 'stop')
i = 0
lungime_interogari = len(interogari_nume)
while i < lungime_interogari and interogari_nume[i] != "stop":
    nume_cautat = interogari_nume[i]
    if nume_cautat in elevi:
        pozitie = elevi.index(nume_cautat)
        nota_elev = note[pozitie]
        print("Elevul " + str(nume_cautat) + " are nota: " + str(nota_elev))
    else:
        print("Elevul " + str(nume_cautat) + " NU există în clasa actuală.")
    i += 1

# C10. Număr promovați / respinși
trecuti = 0
corigenti = 0
for n in note:
    if n >= 5:
        trecuti += 1
    else:
        corigenti += 1
print("\nNumărul de elevi trecuți este: " + str(trecuti))
print("Numărul de elevi corigenți este: " + str(corigenti))

# C11. Media promovaților
note_de_trecere = []
for n in note:
    if n >= 5:
        note_de_trecere.append(n)
print("Lista cu note de trecere: " + str(note_de_trecere))

if len(note_de_trecere) > 0:
    suma_note_trecere = sum(note_de_trecere)
    nr_note_trecere = len(note_de_trecere)
    media_trecuti = suma_note_trecere / nr_note_trecere
    print("Media notelor de trecere este: {:.2f}".format(media_trecuti))
else:
    print("Nu există note de trecere (toți elevii sunt sub 5 sau clasa este goală).")
    media_trecuti = 0
