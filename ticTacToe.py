print("-----------------------------------")
print("Exercice 1 :")
print(" ")

win = False
joueur = 1
tabTicTacToe = [" "," "," "," "," "," "," "," "," "]

# Si la boucle se termine, c'est que la grille à était complété
# (sauf si gagnat au dernier tour, mais ça ne change rien à l'affichage)
for i in range(0,9):

    if(win != True):

        # Affiche la grille du jeu :
        print("|1-",tabTicTacToe[0],"|2-",tabTicTacToe[1],'|3-',tabTicTacToe[2],"|")
        print("-------------------")
        print("|4-",tabTicTacToe[3],"|5-",tabTicTacToe[4],'|6-',tabTicTacToe[5],"|")
        print("-------------------")
        print("|7-",tabTicTacToe[6],"|8-",tabTicTacToe[7],'|9-',tabTicTacToe[8],"|")
        print(" ")

        # Définit si c'est le joueur X ou le joueur O qui joue et permet de jouer à deux alternativement :
        if (joueur == 1):    
            print("C'est au joueur X de jouer !")
            print("Choisissez où placer votre X :")
            emplacement = int(input())
            tabTicTacToe[emplacement-1] = "X"
            joueur = 2
        else :
            print("C'est au joueur O de jouer !")
            print("Choisissez où placer votre O :")
            emplacement = int(input())
            tabTicTacToe[emplacement-1] = "O"
            joueur = 1

        # Vérifie si un des deux joueur à gagné (pas très beau / peut faire mieux) :
        if ( i >= 4 and (
            (tabTicTacToe[0]==tabTicTacToe[1]==tabTicTacToe[2]!=" ") or
            (tabTicTacToe[3]==tabTicTacToe[4]==tabTicTacToe[5]!=" ") or
            (tabTicTacToe[6]==tabTicTacToe[7]==tabTicTacToe[8]!=" ") or
            (tabTicTacToe[0]==tabTicTacToe[4]==tabTicTacToe[8]!=" ") or
            (tabTicTacToe[6]==tabTicTacToe[4]==tabTicTacToe[2]!=" ") or
            (tabTicTacToe[0]==tabTicTacToe[3]==tabTicTacToe[6]!=" ") or
            (tabTicTacToe[1]==tabTicTacToe[4]==tabTicTacToe[7]!=" ") or
            (tabTicTacToe[2]==tabTicTacToe[5]==tabTicTacToe[8]!=" "))):
            if (joueur == 1):
                print("Le joueur O gagne la partie !")
            else :
                print("Le joueur X gagne la partie !")
            win = True

# On vérifie quand même s'il n'y bien pas de vainqueur pour ne pas afficher si on joueur termine avant
if (win!=True):
    print("La partie s'est terminé sans vainqueur...")


# Question 6 : Pour jouer au puissance 4 on pourra garder le même principe (en ayant un tableau qui 
# stock les emplacement des pions des joueurs) mais certaines modifications seront à faire. Il faudra
# premièrement modifier la façon dont s'affiche la grille pour correspondre à celle du puissance 4.
# Il faudra aussi limiter les possibilités des joueurs pour qu'ils ne puissent mettre un pion uniquement
# sur les cases vides les plus basses de chaque colonne. Nous pourront réutiliser la façon de détecter 
# si un joueur à gagner on ajoutant toutes les possibilités (pas ouf) mais il serait préferable
# d'optimiser cela en rendant la chose plus automatique (ce que je n'ai pas fait). Sinon,
# l'architecture générale de l'algorithme pourra complétement resservir presqu'à l'identique. 