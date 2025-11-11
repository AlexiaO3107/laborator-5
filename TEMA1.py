if __name__ == "__main__":
      text = "În fiecare zi, tehnologia avansează cu pași uriași, oferindu-ne noi posibilități de învățare, comunicare și dezvoltare personală, dar și provocări legate de responsabilitate și echilibru."

      lungime=len(text)
      mijloc=lungime//2
      primaparte=text[:mijloc]
      adouaparte=text[mijloc:]
      primaparte=primaparte.upper()
      primaparte=primaparte.strip()
      adouaparte_inversata=adouaparte[::-1]
      adouaparte_inversata = adouaparte_inversata.strip()
      caractere=[',','.','?','!']
      sir_fara_caractere=adouaparte_inversata
      for caracter in caractere:
           sir_fara_caractere=sir_fara_caractere.replace(caracter,'')
      if sir_fara_caractere:
          sir_fara_caractere = sir_fara_caractere[0].upper() + sir_fara_caractere[1:]
      final=primaparte+ ' ' +sir_fara_caractere
      print(final)
