def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulo(a, b):
    return a % b

def revenuSeconde(salaireHeure, heureJourOuvrable, jourOuvrableAn):
    # Je calcule le salaire annuel
    salaireAnnuel = heureJourOuvrable * jourOuvrableAn * salaireHeure
    # Je calcule le nombre de seconde par an
    nbSecondeAn = 365 * 24 * 60 * 60
    # Je divise mon salaire par le nombre de seconde par an
    return salaireAnnuel / nbSecondeAn

def calculNet(salaireBrut, public):
    pourcentage
    # Je soustrais mon pourcentage au salaire brut
    return salaireBrut - (prc / 100 * salaireBrut)