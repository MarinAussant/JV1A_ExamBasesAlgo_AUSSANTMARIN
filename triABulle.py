import random

nbElmtTab = 10
myTable = []


#Initialisation de la table avec des nombres aléatoires.
for i in range(0,nbElmtTab):
    myTable.append(random.randint(1,99))

#Exercice 1 :
print("-----------------------------------")
print("Exercice 1 :")
print(" ")

print(myTable)

print(" ")
print("Je choisi de permuter la valeur à l'index 3 et celle à l'index 7.")
valeurTemp = myTable[7]
myTable[7] = myTable[3]
print("Je mets la valeur à l'index 7 dans une variable temporaire 'valeurTemp' puis je mets la valeur à l'index 3 à l'index 7 :")

print(myTable)

print(" ")
myTable[3] = valeurTemp
print("Puis je mets la valeur stocké dans 'valeurTemp' à l'index 3 du tableau :")

print(myTable)


#Exercice 2 :
print(" ")
print(" ")
print("-----------------------------------")
print("Exercice 2 :")
print(" ")

print("Tableau de base :")
print(myTable)

print(" ")
for j in range(0,len(myTable)-1):

    elmtAct = myTable[j]

    if (myTable[j+1]<elmtAct):

        temp = myTable[j+1]
        myTable[j+1] = elmtAct
        myTable[j] = temp

print("Tableau rangé avec une seule itération :")
print(myTable)


#Exercice 3 :
print(" ")
print(" ")
print("-----------------------------------")
print("Exercice 3 :")
print(" ")

#je régénère un tableau ici pour ne pas avoir les conséquences des exo précédents :  
myTable = []
for i in range(0,nbElmtTab):
    myTable.append(random.randint(1,99))

print("Tableau de base :")
print(myTable)

print(" ")
estTrie = False
for l in range(0,len(myTable)):
   
    for k in range(0,len(myTable)-(1+l)):

        elmtAct = myTable[k]
     
        if (myTable[k+1]<elmtAct):

        
            temp = myTable[k+1]
            myTable[k+1] = elmtAct
            myTable[k] = temp

print("Tableau rangé avec tri à bulle:")
print(myTable)

#Exercice 4 :

# Le tri à bulle est considéré lent puisqu'il déplace case par case l'élémet qu'il trouve plus grand à un instant t 
# là ou les algorithmes vu précédemment recherchaient directement la valeur la plus petite (ou la plus grande) avant
# de la placer au début ou à la fin. Ici beaucoup plus d'attributions mémoires sont effectuées à chaque tour de boucle
# ce qui ralentit la résolution total de l'algorithme (entre 2 et 3 fois plus long pour chaque tour environ ? puisque
# 2 attribution en plus minimum). Il est cependant possible d'optimiser cet algorithme, puisque le tableau peut être 
# trié avant la fin de toutes les boucles. Il faudrait vérifier à chaque tour si ce dernier est complétement trié et
# décider de ne plus rentrer dans la boucle.