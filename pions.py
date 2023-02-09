import tkinter as Tk
import random
import ia


class pionsEmplacements():

    def __init__(self):

        self.ordiJoueur = ia.AI()
        self.fenetre = Tk.Tk()
        self.fenetre.title("Jeu de Dame")
        self.txt1 = Tk.Label(self.fenetre, text='')
        self.txt2 = Tk.Label(self.fenetre, text='')
        self.can1 = Tk.Canvas(self.fenetre, width=400, height=400, bg='dark grey')
        self.Joueur = 0
        self.noirScore = 0
        self.blancScore = 0
        self.dame_noires=list()
        self.dame_blanches = list()
        self.pions_noirs=[1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 21, 23, 25, 27, 29, 30, 32, 34, 36, 38]
        self.pions_blancs= [61, 63, 65, 67, 69, 70, 72, 74, 76, 78, 81, 83, 85, 87, 89, 90, 92, 94, 96, 98]
        self.cases_noires = list()
        self.cases_noires.extend(self.pions_noirs)
        self.cases_noires.extend([41, 43, 45, 47, 49, 50, 52, 54, 56, 58])
        self.cases_noires.extend(self.pions_blancs)

        self.dame_noire = (1, True)
        self.dame_blanche = (0, True)
        self.automatique=ia.AI()
        self.ordiDebute = random.randint(0, 1)
        self.ordiDebute=0 #force à ce que le vrai joueur aient les blancs


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

        self.placement_init(self.pions_noirs, "SlateGray4")

        self.placement_init(self.pions_blancs, "SlateGray2")


    def placement_init(self, liste_pion, couleur, case=40):
        for pion in liste_pion:

            y = (pion // 10) * case + case / 2
            x = ((pion % 10) * case) + case / 2

            if pion in self.dame_noires or pion in self.dame_blanches:

                self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill=couleur)
                self.can1.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="yellow")

            else:
                self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill=couleur)


    def CasesToPlateau(self):

        plateau=[None]*51
        # plateau.extend([(1,False) for k in range(20)])
        # plateau.extend([None for p in range(10)])
        # plateau.extend([(0,False) for k in range(20)])
        for k in range(50):
            print(k)
            if self.cases_noires[k] in self.dame_blanches:

                plateau[k+1]=self.dame_blanche
            elif self.cases_noires[k] in self.dame_noires:

                plateau[k+1] = self.dame_noire

            elif self.cases_noires[k] in self.pions_noirs:

                plateau[k+1] = (1, False)

            elif self.cases_noires[k] in self.pions_blancs:

                plateau[k+1]=(0, False)

            else :
                plateau[k+1]=None
        return plateau

    def PlateauToCases(self, TupleMouvement=(None, None)):

        #Appel au tuple de l'IA
        if TupleMouvement == (None, None) :
            TupleMouvement = self.automatique.play(self.CasesToPlateau(), self.ordiDebute)
            if self.ordiDebute==0:
                print(self.cases_noires[TupleMouvement[0]-1])
                print(self.cases_noires[TupleMouvement[1] - 1])
                self.pions_noirs.remove(self.cases_noires[TupleMouvement[0]-1])
                self.pions_noirs.append(self.cases_noires[TupleMouvement[1]-1])

                if abs(TupleMouvement[1]-TupleMouvement[0])==9 :
                    if (TupleMouvement[0]-1)%10 < 5 :

                        self.pions_blancs.remove(self.cases_noires[max(TupleMouvement)-4-1])
                    else :

                        self.pions_blancs.remove(self.cases_noires[min(TupleMouvement)+4-1])
                elif abs(TupleMouvement[1]-TupleMouvement[0])==11 :
                    if (TupleMouvement[0]-1)%10 < 5 :

                        self.pions_blancs.remove(self.cases_noires[max(TupleMouvement)-5-1])
                    else :

                        self.pions_blancs.remove(self.cases_noires[min(TupleMouvement)+5-1])
                if TupleMouvement[1] <= 5:
                    if self.cases_noires[TupleMouvement[0] - 1] in self.dame_blanches:

                        self.dame_noires.remove(self.cases_noires[TupleMouvement[0] - 1])
                        self.dame_noires.append(self.cases_noires[TupleMouvement[1] - 1])
                    else:
                        self.creationDameNoire(self.cases_noires[TupleMouvement[1] - 1])

                elif self.cases_noires[TupleMouvement[0] - 1] in self.dame_blanches:

                    self.dame_noires.remove(self.cases_noires[TupleMouvement[0] - 1])
                    self.dame_noires.append(self.cases_noires[TupleMouvement[1] - 1])

                # ajout des dames si la dame n'existe pas et si on est au bord du tableau (l'une des 5 premieres appartient à self.blancs)
            else :

                self.pions_blancs.remove(self.cases_noires[TupleMouvement[0]-1])
                self.pions_blancs.append(self.cases_noires[TupleMouvement[1]-1])
                if abs(TupleMouvement[1]-TupleMouvement[0])==9 :
                    if (TupleMouvement[0]-1)%10 < 5 :

                        self.pions_noirs.remove(self.cases_noires[max(TupleMouvement)-4-1])
                    else :

                        self.pions_noirs.remove(self.cases_noires[min(TupleMouvement)+4-1])
                elif abs(TupleMouvement[1]-TupleMouvement[0])==11 :
                    if (TupleMouvement[0]-1)%10 < 5 :

                        self.pions_noirs.remove(self.cases_noires[max(TupleMouvement)-5-1])
                    else :

                        self.pions_noirs.remove(self.cases_noires[min(TupleMouvement)+5-1])
                # si difference trop elevee.... on remove un pion blanc...
                if TupleMouvement[1]>=46:

                    if self.cases_noires[TupleMouvement[0] - 1] in self.dame_noires:

                        self.dame_blanches.remove(self.cases_noires[TupleMouvement[0]-1])
                        self.dame_blanches.append(self.cases_noires[TupleMouvement[1]-1])
                    else:
                        self.creationDameBlanche(self.cases_noires[TupleMouvement[1]-1])

                elif self.cases_noires[TupleMouvement[0] - 1] in self.dame_noires:

                    self.dame_blanches.remove(self.cases_noires[TupleMouvement[0] - 1])
                    self.dame_blanches.append(self.cases_noires[TupleMouvement[1] - 1])

        else :
            if self.ordiDebute == 1:
                print(self.cases_noires[TupleMouvement[0] - 1])
                print(self.cases_noires[TupleMouvement[1] - 1])
                self.pions_noirs.remove(self.cases_noires[TupleMouvement[0] - 1])
                self.pions_noirs.append(self.cases_noires[TupleMouvement[1] - 1])

                if abs(TupleMouvement[1] - TupleMouvement[0]) == 9:
                    if (TupleMouvement[0] - 1) % 10 < 5:

                        self.pions_blancs.remove(self.cases_noires[max(TupleMouvement) - 4 - 1])
                    else:

                        self.pions_blancs.remove(self.cases_noires[min(TupleMouvement) + 4 - 1])
                elif abs(TupleMouvement[1] - TupleMouvement[0]) == 11:
                    if (TupleMouvement[0] - 1) % 10 < 5:

                        self.pions_blancs.remove(self.cases_noires[max(TupleMouvement) - 5 - 1])
                    else:

                        self.pions_blancs.remove(self.cases_noires[min(TupleMouvement) + 5 - 1])
                if TupleMouvement[1] <= 5:
                    if self.cases_noires[TupleMouvement[0] - 1] in self.dame_blanches:

                        self.dame_noires.remove(self.cases_noires[TupleMouvement[0] - 1])
                        self.dame_noires.append(self.cases_noires[TupleMouvement[1] - 1])
                    else:
                        self.creationDameNoire(self.cases_noires[TupleMouvement[1] - 1])

                elif self.cases_noires[TupleMouvement[0] - 1] in self.dame_blanches:

                    self.dame_noires.remove(self.cases_noires[TupleMouvement[0] - 1])
                    self.dame_noires.append(self.cases_noires[TupleMouvement[1] - 1])

                # ajout des dames si la dame n'existe pas et si on est au bord du tableau (l'une des 5 premieres appartient à self.blancs)
            else:

                self.pions_blancs.remove(self.cases_noires[TupleMouvement[0] - 1])
                self.pions_blancs.append(self.cases_noires[TupleMouvement[1] - 1])
                if abs(TupleMouvement[1] - TupleMouvement[0]) == 9:
                    if (TupleMouvement[0] - 1) % 10 < 5:

                        self.pions_noirs.remove(self.cases_noires[max(TupleMouvement) - 4 - 1])
                    else:

                        self.pions_noirs.remove(self.cases_noires[min(TupleMouvement) + 4 - 1])
                elif abs(TupleMouvement[1] - TupleMouvement[0]) == 11:
                    if (TupleMouvement[0] - 1) % 10 < 5:

                        self.pions_noirs.remove(self.cases_noires[max(TupleMouvement) - 5 - 1])
                    else:

                        self.pions_noirs.remove(self.cases_noires[min(TupleMouvement) + 5 - 1])
                # si difference trop elevee.... on remove un pion blanc...
                if TupleMouvement[1] >= 46:

                    if self.cases_noires[TupleMouvement[0] - 1] in self.dame_noires:

                        self.dame_blanches.remove(self.cases_noires[TupleMouvement[0] - 1])
                        self.dame_blanches.append(self.cases_noires[TupleMouvement[1] - 1])
                    else:
                        self.creationDameBlanche(self.cases_noires[TupleMouvement[1] - 1])

                elif self.cases_noires[TupleMouvement[0] - 1] in self.dame_noires:

                    self.dame_blanches.remove(self.cases_noires[TupleMouvement[0] - 1])
                    self.dame_blanches.append(self.cases_noires[TupleMouvement[1] - 1])
            self.damier_trace()
            self.place_pions()

        #ajout des dames si la dame n'existe pas et si on est au bord du tableau (l'une des 5 dernieres appartient à self.noirs)

        #mettre à jour self.cases_noires

    def creationDameNoire(self, dest):
        self.dame_noires.append(dest)

    def creationDameBlanche(self, dest):
        self.dame_blanches.append(dest)
