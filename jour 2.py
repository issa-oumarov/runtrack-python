def My_print_hello():
    print("Hello world")

#-------------------------------------------------------

def My_print_name(name):
    print(name)

My_print_name("Alice")
My_print_name("Bob")
My_print_name("Charlie")
my_name = "Dave"

My_print_name(my_name)

#--------------------------------------------------------

def Add(num1, num2):
    sum = num1 + num2
    print("Sum of", num1, "and", num2, "is", sum)

Add(5, 10)
Add(20, 30)
Add(100, 200)

#---------------------------------------------------------


def GetHello():
    return "Hello la Plateforme"

result = GetHello()
print(result)


#---------------------------------------------------------

def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        print("Invalid operator")

result1 = calcule(10, "+", 5)
print(result1) # affiche 15

result2 = calcule(20, "*", 3)
print(result2) # affiche 60

result3 = calcule(50, "/", 10)
print(result3) # affiche 5.0

#------------------------------------------------------------



def CheckSign(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

        CheckSign(10) # affiche "positif"
CheckSign(-5) # affiche "negatif"
CheckSign(0) # affiche "nul"


#--------------------------------------------------------------


def CheckLanguage(langage):
    if langage == "javascript":
        print("tu es un developpeur web")
    elif langage == "python":
        print("tu es un developpeur IA")
    elif langage == "java":
        print("tu es un developpeur logiciel")
    elif langage == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur developpeur... ")


CheckLanguage("javascript") # affiche "tu es un developpeur web"
CheckLanguage("python") # affiche "tu es un developpeur IA"
CheckLanguage("java") # affiche "tu es un developpeur logiciel"
CheckLanguage("reactjs") # affiche "tu es un developpeur mobile"
CheckLanguage("ruby") # affiche "un jour, je serai le meilleur developpeur... "

#----------------------------------------------------------------


def DisplayFruitOrVegetable(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Je ne connais pas de " + type + " de saison " + saison)


DisplayFruitOrVegetable("fruits", "hiver") # affiche "orange, mandarine et kiwi"
DisplayFruitOrVegetable("fruits", "ete") # affiche "Poire, fraise, cassis"
DisplayFruitOrVegetable("legume", "hiver") # affiche "carotte, topinambour, endive"
DisplayFruitOrVegetable("legume", "ete") # affiche "artichaut, aubergine, navet"
DisplayFruitOrVegetable("poisson", "printemps") # affiche "Je ne connais pas de poisson de saison printemps"


#--------------------------------------------------------------------



def type_triangle(a, b, c):
    # Vérification de la condition de construction du triangle
    if a + b > c and b + c > a and c + a > b:
        # Détermination du type de triangle
        if a == b == c:
            print("Le triangle est équilatéral")
        elif a == b or b == c or c == a:
            if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
                print("Le triangle est rectangle et isocèle")
            else:
                print("Le triangle est isocèle")
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            print("Le triangle est rectangle")
        else:
            print("Le triangle est quelconque")
    else:
        print("Les longueurs ne permettent pas de construire un triangle")


type_triangle(3, 4, 5) # Le triangle est rectangle et isocèle
type_triangle(1, 1, 1) # Le triangle est équilatéral
type_triangle(2, 3, 4) # Le triangle est quelconque
type_triangle(3, 3, 4) # Le triangle est isocèle
type_triangle(5, 5, 10) # Les longueurs ne permettent pas de construire un triangle

#--------------------------------------------------------------------------





