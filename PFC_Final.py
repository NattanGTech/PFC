"""
DEBUT

On admet une fonction random qui renvoie un chiffre aleatoire entre un max et un min (random(min, max))
On admet une fonction input qui recupere l'entree d'un joueur

Definir une fonction pierreFeuilleCiseau sans parametre
qui retourne un message pour savoir si l'utilisateur à gagne, perdu ou egalite
    Assigne a la variable bestOff le retour de l'execution de la fonction input avec en parametre le message "Le premier à combien ?" transformer en integer
    Initialiser la variable scoreJoueur a 0
    Initialiser la variable scoreBot a 0
    Initialiser la variable nbManche a 0
    Tant que le scoreJoueur n'est pas egal a bestOff et que le scoreBot n'est pas egal a bestOff
        Alors
        Incrementer la variable nbManche de 1
        Assigne a la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message "Pierre, Feuille, Ciseau ?"
        Tant que le choixJoueur n'est pas egal a "Pierre" et n'est pas egal a "Feuille" et n'est pas egal a "Ciseau"
            Alors assigne a la variable choixJoueur le retour de l'execution de la fonction input avec en parametre le message "Incorrect ! Pierre, Feuille, Ciseau ?"
        Assigne a la variable choixPossible une liste qui comprend "Pierre", "Feuille" et "Ciseau"
        Assigne a la variable choixBot la correspondance dans la liste choixPossible du retour de l'execution de la fonction random avec comme parametre 0 et 2
        Si le choixjouer est egal au choixBot
            Alors
            Afficher le message "Egalité" et le score (scoreJoueur - scoreBot)
        Sinon si le choixJoueur est egal a "Pierre" et le choixBot est egal a "Ciseau"
        Ou le choixJoueur est egal a "Ciseau" et le choixBot est egal a "Feuille"
        Ou le choixJoueur est egal a "Feuille et le choixBot est egal a "Pierre"
            Alors
            Ajouter 1 a la variable scoreJoueur
            Afficher le message "Gagne" et le score (scoreJoueur - scoreBot)
        Sinon
            Alors
            Ajouter 1 a la variable scoreBot
            Afficher le message "Perdu" et le score (scoreJoueur - scoreBot)
    Si le scoreJouer est egal a bestOff
        Alors afficher le message "Gagne Fin de la partie" et le nombre de round
    Sinon
        Alors afficher le message "Perdu Fin de la partie" et le nombre de round
    Assigne a la variable restart le retour de l'execution de la fonction input avec en parametre le message "Voulez-vous rejouer ? Oui / Non"
    Si le restart est egal a "Oui"
        Alors reexecuter la fonction pierreFeuilleCiseau()

Execution de la fonction pierreFeuilleCiseau()

FIN
"""