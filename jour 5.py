"""
prenom = input("Entrez votre prénom : ")
print("Hello " + prenom)
"""
#___________________________________________________________
def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print('-' * width)
        else:
            print('|' + ' '*(width-2) + '|')
draw_rectangle(10, 3)

#___________________________________________________________   

def draw_carpet(n):
    for j in range(n, -1, -1):
        for i in range(n, -1, -1):
            if i == j:
                print(end='' '')
            elif j+i == n:
                print(end='' ' ')
            else:
                print( end='' '#')
        print()
draw_carpet(10)
#___________________________________________________________ 

