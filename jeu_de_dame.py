from ia import *
from pions import *

class JeuDeDame():
    def __init__(self):

        self.ordiJoueur = IA()
        self.emplacementGrille = pionsEmplacements()
        self.emplacementGrille.damier_trace()
        self.emplacementGrille.place_pions()
        self.plateau = self.emplacementGrille.CasesToPlateau()
        print(self.plateau)
        self.nb_tours = 0
        self.selected = -1
        self.Joueur = 0


    def appelIA(self):
        if self.nb_tours<1000:

            self.emplacementGrille.PlateauToCases()
            self.emplacementGrille.damier_trace()
            self.emplacementGrille.place_pions()
            self.Joueur = self.emplacementGrille.ordiDebute
            self.selected = -1
            self.nb_tours+=1
            self.plateau = self.emplacementGrille.CasesToPlateau()
            print("tour==========", self.nb_tours)
            print(self.plateau)
            return self.emplacementGrille.can1.bind("<Button-1>", self.select)

    def select(self, event, case = 40):
        # on détermine la case ou s'est passé la selection
        ligne = (event.y//case)
        colonne = (event.x//case)
        num_case = ligne*10+colonne
        print(ligne, '\n', colonne)
        print(num_case)
        pions = self.emplacementGrille.pions_blancs if self.Joueur == 0 else self.emplacementGrille.pions_noirs

        if self.Joueur == 1-self.emplacementGrille.ordiDebute:
            return self.appelIA()

        if self.Joueur!=1-self.emplacementGrille.ordiDebute and self.selected == -1:
            if num_case in pions:
                self.selected = num_case
            print("coucou", self.emplacementGrille.cases_noires.index(num_case)+1)
            self.ordiJoueur.possibilitees(self.plateau, self.emplacementGrille.cases_noires.index(num_case)+1)
            print("DAME.....", self.emplacementGrille.dame_noires, self.emplacementGrille.dame_blanches)
        print(self.selected)
        if self.Joueur!=1-self.emplacementGrille.ordiDebute :

            print("dest = ", num_case)
            print(self.ordiJoueur.pos)
            if self.emplacementGrille.cases_noires.index(num_case)+1 in self.ordiJoueur.pos:

                initial_position= self.emplacementGrille.cases_noires.index(self.selected)+1
                deplacement_pion = (initial_position, self.emplacementGrille.cases_noires.index(num_case)+1)
                print(deplacement_pion)
                self.emplacementGrille.PlateauToCases(deplacement_pion)
                self.plateau = self.emplacementGrille.CasesToPlateau()
                print("JEU FAIT===========", self.plateau)
                self.emplacementGrille.damier_trace()
                self.emplacementGrille.place_pions()
                self.Joueur = 1-self.emplacementGrille.ordiDebute
                return self.appelIA()

    def interface(self):

        self.emplacementGrille.can1.pack(side=Tk.TOP)
        
        self.emplacementGrille.txt1.pack()
        self.emplacementGrille.txt2.pack()
        bt1 = Tk.Button(self.emplacementGrille.fenetre, text='Quitter', command=self.emplacementGrille.fenetre.destroy)
        bt1.pack(side=Tk.LEFT)
        self.emplacementGrille.damier_trace()
        self.emplacementGrille.place_pions()

        print(self.emplacementGrille.ordiDebute)
        self.emplacementGrille.can1.bind("<Button-1>", self.select)
        if self.emplacementGrille.blancScore == 20:
            self.emplacementGrille.txt1.configure(text='Blancs gagnent')
            self.emplacementGrille.fenetre.destroy()

        elif self.emplacementGrille.noirScore==20 :

            self.emplacementGrille.txt1.configure(text='Noirs gagnent')
            self.emplacementGrille.fenetre.destroy()

        if self.nb_tours==1000:
            self.emplacementGrille.fenetre.destroy()



        self.emplacementGrille.damier_trace()
        self.emplacementGrille.place_pions()
        self.emplacementGrille.fenetre.mainloop()

    
jeu = JeuDeDame()
jeu.interface()


