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
print("Je choisi de permuter la valeur à l'index 3 et celle à l'index 7 :")
valeurTemp = myTable[7]
myTable[7] = myTable[3]
myTable[3] = valeurTemp


print(myTable)