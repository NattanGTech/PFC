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

def withdrawFees(total, percent):
    # calcul du montant des taxes a retirer
    fees = total * (percent / 100)
    # Je retourne mon total sans les taxes
    return total - fees

def calculNet(salaireBrut, public):
    # Si j'occupe un poste de la fonction publique
    if public:
    # Alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut, 15)
    # Sinon, c'est que je suis un travailleur privé
    # Alors je retourne le salaire brut - 23% de taxes
    return withdrawFees(salaireBrut, 23)

nbPersonne = x

if nbPersonne == 1:
    tuRentres()
else if nbPersonne == 3:
    tuRentres()
else if nbPersonne == 5:
    tuRentres()
else:
    tuRentresPas()