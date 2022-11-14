# On admet une fonction random qui renvoie un chiffre aleatoire entre un max et un min (random(min, max))
import random

# Definir une fonction pierreFeuilleCiseau sans parametre
# qui retourne un message pour savoir si l'utilisateur à gagne, perdu ou egalite
def pierreFeuilleCiseau():
#     Assigne a la variable bestOff le retour de l'execution de la fonction input avec en parametre le message "Le premier à combien ?"
    bestOff = int(input("Le premier à combien ?"))
#     Initialiser la variable scoreJoueur a 0
    scoreJoueur = 0
#     Initialiser la variable scoreBot a 0
    scoreBot = 0
#     Initialiser la variable nbManche a 0
    nbManche = 0
#     Tant que le scoreJoueur n'est pas egal a bestOff et que le scoreBot n'est pas egal a bestOff
    while scoreJoueur != bestOff and scoreBot != bestOff:
#         Alors
#         Incrementer la variable nbManche de 1
        nbManche += 1
#         Assigne a la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message "Pierre, Feuille, Ciseau ?"
        choixJoueur = input("Pierre, Feuille, Ciseau ?")
#         Tant que le choixJoueur n'est pas egal a "Pierre" et n'est pas egal a "Feuille" et n'est pas egal a "Ciseau"
        while choixJoueur != "Pierre" and choixJoueur != "Feuille" and choixJoueur != "Ciseau":
#             Alors assigne a la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message "Pierre, Feuille, Ciseau ?"
            choixJoueur = input("Incorrect ! Pierre, Feuille, Ciseau ?")
#         Assigne a la variable choixPossible une liste qui comprend "Pierre", "Feuille" et "Ciseau"
        choixPossible = ["Pierre", "Feuille", "Ciseau"]
#         Assigne a la variable choixBot la correspondance dans la liste choixPossible du retour de l'execution de la fonction random avec comme parametre 0 et 2
        choixBot = choixPossible[random.randint(0, 2)]
#         Si le choixjouer est egal au choixBot
        if choixJoueur == choixBot:
#             Alors
#             Afficher le message "Egalité" et le score (scoreJoueur - scoreBot)
            print(f"Egalite, le scrore est de {scoreJoueur} - {scoreBot}")
#         Sinon si le choixJoueur est egal a "Pierre" et le choixBot est egal a "Ciseau"
#         Ou le choixJoueur est egal a "Ciseau" et le choixBot est egal a "Feuille"
#         Ou le choixJoueur est egal a "Feuille et le choixBot est egal a "Pierre"
        elif choixJoueur == "Pierre" and choixBot == "Ciseau" or choixJoueur == "Ciseau" and choixBot == "Feuille" or choixBot == "Feuille" or choixJoueur == "Pierre":
#             Alors
#             Ajouter 1 a la variable scoreJoueur
            scoreJoueur += 1
#             Afficher le message "Gagne" et le score (scoreJoueur - scoreBot)
            print(f"Gagne, le scrore est de {scoreJoueur} - {scoreBot}")
#         Sinon
        else:
#             Alors
#             Ajouter 1 a la variable scoreBot
            scoreBot += 1
#             Afficher le message "Perdu" et le score (scoreJoueur - scoreBot)
            print(f"Perdu, le scrore est de {scoreJoueur} - {scoreBot}")
#     Si le scoreJouer est egal a bestOff
    if scoreJoueur == bestOff:
#         Alors afficher le message "Gagne Fin de la partie" et le nombre de round
        print(f"Gagne, Fin de la partie, Duree : {nbManche} manche")
#     Sinon
    else:
#         Alors afficher le message "Perdu Fin de la partie" et le nombre de round
        print(f"Perdu, Fin de la partie, Duree : {nbManche} manche")
#     Assigne a la variable restart le retour de l'execution de la fonction input avec en parametre le message "Voulez-vous rejouer ? Oui / Non"
    restart = input("Voulez-vous rejouer ? Oui / Non")
#     Si le restart est egal a "Oui"
    if restart == "Oui":
#         Alors reexecuter la fonction pierreFeuilleCiseau()
        pierreFeuilleCiseau()

pierreFeuilleCiseau()