import tkinter as Tk
import random
import ia


class pionsEmplacements():

    def __init__(self, currentPlayer):

        self.fenetre = Tk.Tk()
        self.fenetre.title("Jeu de Dame")
        self.chaine = Tk.Label(self.fenetre)
        self.txt1 = Tk.Label(self.fenetre, text='')
        self.txt2 = Tk.Label(self.fenetre, text='')
        self.can1 = Tk.Canvas(self.fenetre, width=400, height=400, bg='dark grey')
        self.Joueur = currentPlayer
        self.noirScore = 0
        self.blancScore = 0
        self.noirsDames=list()
        self.blancsDames = list()
        self.noirs = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 21, 23, 25, 27, 29, 30, 32, 34, 36, 38]
        self.blancs = [61, 63, 65, 67, 69, 70, 72, 74, 76, 78, 81, 83, 85, 87, 89, 90, 92, 94, 96, 98]
        self.cases_noires = list()
        self.cases_noires.extend(self.noirs)
        self.cases_noires.extend(self.blancs)
        self.cases_noires.extend([41, 43, 45, 47, 49, 50, 52, 54, 56, 58])
        self.dame_noire = (1, True)
        self.dame_blanche = (0, True)
        self.automatique=ia.AI()
        self.ordiDebute = random.randint(0, 1)

    def damier_trace(self, case=40):
        [[(self.can1.create_rectangle(j * case, i * case, (j * case) + case, (i * case) + case, fill='darkmagenta') if (
                                                                                                                                   j % 2) == 0 else self.can1.create_rectangle(
            j * case, i * case, (j * case) + case, (i * case) + case, fill='black')) if (i % 2) == 0 else (
            self.can1.create_rectangle(j * case, i * case, (j * case) + case, (i * case) + case, fill='black') if (
                                                                                                                              j % 2) == 0 else self.can1.create_rectangle(
                j * case, i * case, (j * case) + case, (i * case) + case, fill='darkmagenta')) for j in range(10)] for i in
         range(10)]


    def place_pions(self):
        # on marque les scores

        self.txt1.configure(text='Blanc = ' + str(self.blancScore))
        self.txt2.configure(text='Noir = ' + str(self.noirScore))
        if self.Joueur == 1:
            self.chaine.configure(text="Les noirs jouent...", fg='black')
        else:
            self.chaine.configure(text="Les blancs jouent...", fg='black')

        self.placement_init(self.noirs, "SlateGray2")

        self.placement_init(self.blancs, "SlateGray4")


    def placement_init(self, liste_pion, couleur, case=40):
        for pion in liste_pion:

            y = (pion // 10) * case + case / 2
            x = ((pion % 10) * case) + case / 2

            if pion in self.noirsDames or pion in self.blancsDames:

                self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill=couleur)
                self.can1.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="yellow")

            else:
                self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill=couleur)


    def CasesToPlateau(self):

        plateau=[None]
        plateau.extend((1,False) for k in range(20))
        plateau.extend(None for p in range(10))
        plateau.extend((0,False) for k in range(20))
        for k in range(51):

            if self.cases_noires[k] in self.blancsDames:

                plateau[k+1]=self.dame_blanche
            elif self.cases_noires[k] in self.noirsDames:

                plateau[k+1] = self.dame_noire

            elif self.cases_noires[k] in self.noirs:

                plateau[k+1] = (1, False)

            elif self.cases_noires[k] in self.blancs:

                plateau[k+1]=(0, False)

            else :
                plateau[k+1]=None
        return plateau

    def PlateauToCases(self):

        self.cases_noires=list()
        self.blancsDames=list()
        self.noirsDames=list()
        self.noirs=list()
        self.blancs=list()
        #Appel au tuple de l'IA
        TupleMouvement = self.automatique.play(self.CasesToPlateau(), self.ordiDebute)
        if self.ordiDebute:

            self.blancs.remove(self.cases_noires[TupleMouvement[0]-1])
            self.blancs.append(self.cases_noires[TupleMouvement[1]-1])

            #si difference trop elevee.... on remove un pion noir...
            # ajout des dames si la dame n'existe pas et si on est au bord du tableau (l'une des 5 premieres appartient à self.blancs)
        else :

            self.noirs.remove(self.cases_noires[TupleMouvement[0]-1])
            self.noirs.append(self.cases_noires[TupleMouvement[1]-1])
            # si difference trop elevee.... on remove un pion blanc...
            #ajout des dames si la dame n'existe pas et si on est au bord du tableau (l'une des 5 dernieres appartient à self.noirs)

        #mettre à jour self.cases_noires

