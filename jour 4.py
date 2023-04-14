def ma_liste_fruits():
    fruits = ["pomme", "cerise", "orange"]
    return fruits
liste_fruits = ma_liste_fruits()
print(liste_fruits)
#______________________________________________________________________

def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    print(fruits[1])
afficher_deuxieme_element()
#______________________________________________________________________

def liste_fruits():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("melon")
    print(fruits)
liste_fruits()
#______________________________________________________________________

def liste_fruits():
    fruits = ["pomme", "cerise", "orange, Melon"]
    fruits.insert(2, "Mangue")
    print(fruits)
liste_fruits()
#______________________________________________________________________

L = [1, 2, 3, 4, 5]
print(L)
save = L[0]
L[0] = L[4]
L[4] = save
print(L)
#______________________________________________________________________

L = [6, 12, 18, 5]
l = len(L)
aux = L[0]
L[0] = L[l-1]
L[l-1] = aux
print (L)
#______________________________________________________________________

L = [8,24,48,2,16]
long = len(L)
mult3 = 0
for i in range(long):
    if L[i] % 3 == 0:
        print (i, L[i])
#_______________________________________________________________________

L = [8,24,27,48,2,16,9,7,84,91]
long = len(L)
somme = 0
for i in range(long):
    if L[i] % 2 == 0:
        somme = somme + L[i]
        print(somme)
#_______________________________________________________________________
L = [8,24,27,48,2,16,9,7,84,91]
long = len(L)
max = L[0]
min = L[0]
for i in range (long):
    if L[i] > max:
        max = L[i]
    else:
        if L[i] < min:
            min = L[i]
        print(max, min)
#_______________________________________________________________________

L = [8,24,27,48,2,16,9,7,84,91]
produit = 1
for i in L:
    if i >= 25 and i <= 90:
        produit *= i
        print(produit)
#_______________________________________________________________________

L = [7,11,42,39,2]
for i in range(len(L)):
    L[i] += 1
    print(L)