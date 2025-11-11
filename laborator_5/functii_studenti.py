def cmmmc(a ,b):
    produs = a * b
    if produs == 0:
        return "Imposibil"
    else:
        while a != b:
            if a > b:
                a-=b
            else:
                b-=a
        return produs//a

