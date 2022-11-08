def add(a, b)
    return a + b

def sub(a, b)
    return a - b

def multiply(a, b)
    return a * b

def divide(a, b)
    return a / b

def modulo(a, b)
    return a % b

def revenuSeconde(salaireHeure, heureJourOuvrable, jourOuvrableAn)
    return (heureJourOuvrable * jourOuvrableAn) * (salaireHeure) / 365 / 24 / 60 / 60

def calculNet(salaireBrut, Prc)
    return salaireBrut - (Prc / 100 * salaireBrut)