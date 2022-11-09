def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Si b est 0
    if b == 0:
    # Alors je retourne error
        print("error")
    # Et retourne rien
        return
    # Sinon b n'est pas 0
    # Alors je retourne la division
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

"""
nbPersonne = x

if nbPersonne == 1:
    tuRentres()
else if nbPersonne == 3:
    tuRentres()
else if nbPersonne == 5:
    tuRentres()
else:
    tuRentresPas()
"""

"""
tour = 0
# Tant que je ne suis pas au tour 5
while tour != 5:
# Appeler la fonction jouerUnTour
    jouerUnTour()
# J'effectue l'action de passer un tour
    tour = tour + 1
"""

#def input():
    # Renvoie un caractere de type string au hasard

#Exercice:
# Faire un mini jeu qui affige un message lorsque input renvoie le bon caractere
# le caractere doit etre parametrable

"""
def bonCaractere(caractere):
    # On recupere un caractere aleatoire
    caractereInput = input()
    # Tant que ce caractere est diiferent du caractere demander
    while caractereInput != caractere:
    # Alors on recupere un autre caractere aleatoire
        caractereInput = input()
    # Ecrit reussi
    print("Reussi")

def bonCaractereRecursif(caractere):
    caractereInput = input()
    if carctereInput == caractere:
        print(reussi)
        return
    bonCaractere(caractere)
"""

tab = [1, 2, 3, 8, 0]

# Pour recuperer 3 je prends dans tab l'index 3 - 1

print(tab[2]) # Renvoie 3

len(tab) # Renvoie la longueur de tab

prenom = "Nattan"
nom = "Le Guyader"
nomPrenom = nom + prenom # Renvoie Le GuyaderNattan
nomPrenom = nom + " " + prenom # Renvoie Le Guyader Nattan

integerValue = 342
stringIntegerValue = str(342) # Renvoie "342" au lieu de 342

#Exercices
# Faire une fonction qui concatene 2 chianes de caractere, les separant par une virgule

"""
def concatene(char1, char2):
    return char1 + ", " char2
"""

# Faire une fonction qui itere sur tous les index d'un tab renvoyant une chaine de char avec ensembles des occuration d'un chiffre e.g.:
#Pour tableau = [0, 1, 1, 1, 0, 1, 1, 0, 1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesiter pas a implementer la premiere fonction

"""
def indexTab(tab, nb):
    index = ""
    for i in range(len(tab) - 1):
        if tab[i] = nb:
            if index == "":
                index = str(i)
            else:
                index = concatene(index, str(i))
    return index
"""

#tableauMultiType = ["Yo", True, variable, 4 > 2, None, 145]
tableauDim = [0, 1, 2, 3]
tableauDim2 = [0, 1, 21, 3]
tableauMultiDim = [tableauDim, tableauDim2]
tableauMultiDim[1][2] # Renvoie 21

tableauCleVal = {"Cle" : "Valeur"}
tableauCleVal["Cle"] #Renvoie Valeur

# foreach key : valeur in tableauCleVal
    # print(key) #Renvoie "Cle"
    # print(valeur) # Renvoie "Valeur"

# faire une fonction Afficher un message

"""
def afficherMsg(message):
    print(message)
"""

# Tel que
listeUtilisateur = {
    "Nattan" : "motdepasse",
    "Michel" : "password",
    "Toto" : "1234",
    "Robert" : "azerty"
}
# Ecrivez la fonction login(userName, password, listUser) permettant d'afficher un msg de connexion si
# le combo user/password est bon

"""
def login(userName, password, listUser):
    # Pour chaque cle de listUser
    for e in listUser:
        # Si userName est le même que le name dans le tableau et que le password et celui du tableau sont les mêmes
        if userName == e and password == listUser[e]:
            # Alors afficher "vous etes connecte"
            print("Vous etes connecte")
"""

"""
def fibonacci(xDebut, lenMax):
    # Pour chaque valeur jusqu'à lenMax
    for i in range(lenMax):
        # Si on est à la premiere valeur
        if i == 0:
            # Alors on met 0 dans le variable de fin
            suite = "0"
        # Sinon Si on est à la deuxieme valeur
        elif i == 1:
            # Alors on ecrit la valeur de xDebut dans la variable de fin
            suite = concatene(suite, xDebut)
            # Je stock ma premiere valeur
            stock = 0
        # Sinon
        else:
            # J'addtionne les deux derniere valeur et les met dans une variable
            xDebut = xDebut + stock
            # Je stock la valeur precedante
            stock = xDebut - stock
            # on ecrit la valeur qui se trouve dans xDebut dans la variable de fin
            suite = concatene(suite, str(xDebut))
    # Je retourne mon resultat
    return suite
"""




#tableau 2 dim adjacent


