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


#Exercice 2 :
print(" ")
print(" ")
print("-----------------------------------")
print("Exercice 2 :")
print(" ")