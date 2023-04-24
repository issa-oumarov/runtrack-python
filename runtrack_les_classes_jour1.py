class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation()
print(operation)
#_______________________________________________________________

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation(12, 3)
print(f"Le nombre1 est {operation.nombre1}")
print(f"Le nombre2 est {operation.nombre2}")
#_______________________________________________________________

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)

operation = Operation(12, 3)
operation.addition()
#________________________________________________________________

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

print(personne1.sePresenter())
print(personne2.sePresenter())
#_________________________________________________________________

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

animal = Animal()
print(f"L'âge de l'animal {animal.age} ans")
animal.vieillir()
print(f"L'âge de l'animal {animal.age} ans")
#__________________________________________________________________

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

animal = Animal()
animal.nommer("Luna")
print(f"L'animal se nomme {animal.prenom}")
#___________________________________________________________________

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec longueur=10 et largeur=5
rect = Rectangle(10, 5)

# Modification de la longueur et de la largeur
rect.set_longueur(20)
rect.set_largeur(10)

# Vérification que les modifications ont été prises en compte
print(rect.get_longueur()) # 20
print(rect.get_largeur()) # 10
#______________________________________________________________________

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: Le nombre de pages doit être un nombre entier positif.")
#_______________________________________________________________________

class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: Le nombre de pages doit être un nombre entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Erreur: Le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Erreur: Le livre n'a pas été emprunté.")
#_________________________________________________________________________

class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nombre_de_credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__nombre_de_credits += credits
            self.__level = self.__studentEval()
        else:
            print("Erreur: Le nombre de crédits doit être supérieur à zéro.")

    def __studentEval(self):
        if self.__nombre_de_credits >= 90:
            return "Excellent"
        elif self.__nombre_de_credits >= 80:
            return "Très bien"
        elif self.__nombre_de_credits >= 70:
            return "Bien"
        elif self.__nombre_de_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom =", self.__nom)
        print("Prenom =", self.__prenom)
        print("id =", self.__numero_etudiant)
        print("Niveau =", self.__level)

# Création d'un étudiant John Doe avec le numéro d'étudiant 145
john = Student("John", "Doe", 145)

# Ajout de crédits à John
john.add_credits(10)
john.add_credits(10)
john.add_credits(10)

# Affichage des informations de John
john.studentInfo()
#_____________________________________________________________________________

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("Erreur: Le réservoir doit contenir plus de 5 litres pour démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir