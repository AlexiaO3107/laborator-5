[tema 2.py](https://github.com/user-attachments/files/23185535/tema.2.py)
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
    nota_maxima = max(note)
    nota_minima = min(note)
    print("\nElevii cu nota maximă:")
    for i in range(len(note)):
        if note[i] == nota_maxima:
            print(f"{elevi[i]} - {note[i]}")

    print("\nElevii cu nota minimă:")
    for i in range(len(note)):
        if note[i] == nota_minima:
            print(f"{elevi[i]} - {note[i]}")
            media = sum(note) / len(note)
            print(f"\nMedia clasei este: {media:.2f}")
            print("\nElevii promovați (nota ≥ 5):")
            for i in range(len(note)):
                if note[i] >= 5:
                    print(elevi[i])
elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"
for i in range(len(note)):
    note[i] += 1
    if note[i] > 10:
        note[i] = 10
        print("Notele după creșterea cu 1 punct:", note)
        elevi.append(elev_nou)
        note.append(nota_elev_nou)

        print("\nListe actualizate după adăugarea noului elev:")
        print("Elevi:", elevi)
        print("Note:", note)
    if elev_de_sters in elevi:
        poz = elevi.index(elev_de_sters)
        elevi.pop(poz)
        note.pop(poz)
        print(f"\n{elev_de_sters} a fost eliminat din listă.")
    else:
        print(f"\n{elev_de_sters} nu se află în listă.")
    print("\nLista actualizată de elevi și note:")
    for i in range(len(elevi)):
        print(f"{elevi[i]} are nota {note[i]}")
    interogari_nume = ["Ana", "Mara", "Elena", "stop"]
    i = 0
    while i < len(interogari_nume):
        nume = interogari_nume[i]
        if nume == "stop":
            break
        if nume in elevi:
            poz = elevi.index(nume)
            print(f"{nume} are nota {note[poz]}")
        else:
            print(f"{nume} nu se află în listă.")
        i += 1
        promovati = 0
        respinși = 0

        for n in note:
            if n >= 5:
                promovati += 1
            else:
                respinși += 1

        print(f"\nNumăr promovați: {promovati}")
        print(f"Număr respinși: {respinși}")
        note_promovati = [n for n in note if n >= 5]

        if len(note_promovati) > 0:
            media_promovati = sum(note_promovati) / len(note_promovati)
            print(f"\nMedia promovaților este: {media_promovati:.2f}")
        else:
            print("\nNu există elevi promovați.")

