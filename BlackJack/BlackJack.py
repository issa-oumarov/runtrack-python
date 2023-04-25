
import random
import tkinter as tk


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f'{self.valeur} de {self.couleur}'


class Jeu:
    def __init__(self):
        self.paquet = []
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def valeur_main(self, main):
        valeur = 0
        as_present = False
        for carte in main:
            if carte.valeur == 'Valet' or carte.valeur == 'Dame' or carte.valeur == 'Roi':
                valeur += 10
            elif carte.valeur == 'As':
                as_present = True
                valeur += 1
            else:
                valeur += int(carte.valeur)
        if as_present and valeur <= 11:
            valeur += 10
        return valeur


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.jeu = Jeu()
        self.main_joueur = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
        self.main_croupier = [self.jeu.tirer_carte(), self.jeu.tirer_carte()]
        self.create_widgets()

    def create_widgets(self):
        self.label_joueur = tk.Label(self, text=f'Main du joueur: {self.main_joueur}')
        self.label_joueur.pack()

        self.label_croupier = tk.Label(self, text=f'Main du croupier: {self.main_croupier[0]}')
        self.label_croupier.pack()

        self.bouton_tirer = tk.Button(self, text='Tirer une carte', command=self.tirer_carte)
        self.bouton_tirer.pack()

        self.bouton_passer = tk.Button(self, text='Passer', command=self.passer)
        self.bouton_passer.pack()

    def tirer_carte(self):
        self.main_joueur.append(self.jeu.tirer_carte())
        self.label_joueur['text'] = f'Main du joueur: {self.main_joueur}'
        if self.jeu.valeur_main(self.main_joueur) > 21:
            self.fin_partie()

    def passer(self):
        while self.jeu.valeur_main(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.tirer_carte())
        self.fin_partie()

    def fin_partie(self):
        self.bouton_tirer['state'] = tk.DISABLED
        self.bouton_passer['state'] = tk.DISABLED
        self.label_croupier['text'] = f'Main du croupier: {self.main_croupier}'

        valeur_joueur = self.jeu.valeur_main(self.main_joueur)
        valeur_croupier = self.jeu.valeur_main(self.main_croupier)

        if valeur_joueur > 21:
            resultat = 'Vous avez perdu'
        elif valeur_croupier > 21 or valeur_joueur > valeur_croupier:
            resultat = 'Vous avez gagné'
        else:
            resultat = 'Vous avez perdu'

        tk.Label(self, text=resultat).pack()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
