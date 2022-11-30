
win = False
joueur = 1
tabTicTacToe = [" "," "," "," "," "," "," "," "," "]

def affichageGrille (tab) :

    print("-------------------------")
    for i in range (0,3):

        print("|",i*3 + 1,"-",tab[i*3],"|",i*3 + 2,"-",tab[i*3 + 1],"|",i*3 + 3,"-",tab[i*3 + 2],"|")
        print("-------------------------")
        
    print(" ")

def demandeJoueur(numJoueur, tab) :

    if (numJoueur == 1):    
        print("C'est au joueur X de jouer !")
        print("Choisissez où placer votre X :")
        emplacement = int(input())
        tab[emplacement-1] = "X"
        numJoueur = 2

    else :
        print("C'est au joueur O de jouer !")
        print("Choisissez où placer votre O :")
        emplacement = int(input())
        tab[emplacement-1] = "O"
        numJoueur = 1

    return [numJoueur,tab]


def isWin(tab) :
    
    for i in range (0,3):

        if ((
            (tab[i*3]==tab[i*3 + 1]==tab[i*3 +2]!=" ") or
            (tab[i]==tab[i+3]==tab[i+6]!=" ") or
            (tab[1]==tab[4]==tab[7]!=" ") or
            (tab[2]==tab[5]==tab[8]!=" "))):
            affichageGrille(tab)
            if (joueur == 1):
                print("Le joueur O gagne la partie !")
            else :
                print("Le joueur X gagne la partie !")
            return True


for i in range(0,9):

    if(win != True):

        affichageGrille(tabTicTacToe)

        tempTab = demandeJoueur(joueur,tabTicTacToe)
        joueur = tempTab[0]
        tabTicTacToe = tempTab[1]

        if isWin(tabTicTacToe):
            win = True

if (win!=True):
    print("La partie s'est terminé sans vainqueur...")

