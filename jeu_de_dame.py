import ia

#probleme pour l'interaction : l'IA veut toujours commecner
#cleaner
#définir le gagnant

class JeuDeDame():
    def __init__(self):
        

        self.ordiJoueur = ia.AI()
        self.plateau = [None]*51
        for k in range(1, 21):
            self.plateau[k] = (1, False)
        for p in range(31, 51):
            self.plateau[p] = (0, False)
        print(self.plateau)
        self.nb_tours = 0
        self.selected = -1

        self.Joueur = 0


    def appelIA(self, case, premierJoueur):
        if self.nb_tours<1000:

            deplacement_pion = self.ordiJoueur.play(self.plateau, premierJoueur)
            print(deplacement_pion)
            move = deplacement_pion[1] * 2 - 1 if (
                    deplacement_pion[1] % 10 <= 5) else deplacement_pion[1] * 2-2
            initial_position = deplacement_pion[0] * 2 - 1 if (
                    deplacement_pion[0] % 10 <= 5) else deplacement_pion[0] * 2-2
            tupleAdeplacer = self.plateau[deplacement_pion[0]]
            if premierJoueur == 0 and move in [1,3,5,7,9]:

                tupleAdeplacer=(premierJoueur, True)
                self.ordiJoueur.deplacementDameNoir(move, initial_position)

            elif premierJoueur==1 and move in [90,92,94,96,98]:

                tupleAdeplacer=(premierJoueur, True)
                self.ordiJoueur.deplacementDameBlanc(move, initial_position)

            print(tupleAdeplacer)
            self.plateau[deplacement_pion[0]] = None
            self.plateau[deplacement_pion[1]] = tupleAdeplacer

            print("diff = ", abs(move - initial_position))

            if abs(move-initial_position) in range(17,24):

                print("j'ai mangé")
                print((move+initial_position)//2)
                print(self.ordiJoueur.pions_n)
                print(self.ordiJoueur.pions_b)
                if move in self.ordiJoueur.pions_b and (move+initial_position)//2 in self.ordiJoueur.pions_n:
                    print("coucou je mange un noir")
                    self.ordiJoueur.pions_n.remove((move + initial_position) // 2)
                    self.ordiJoueur.pions_n.append(-1)
                    self.ordiJoueur.blanc += 1
                elif move in self.ordiJoueur.pions_n and (move+initial_position)//2 in self.ordiJoueur.pions_b:
                    print("coucou je mange un blanc")

                    self.ordiJoueur.pions_b.remove((move+initial_position)//2)
                    self.ordiJoueur.pions_b.append(-1)
                    self.ordiJoueur.noir+=1
                print("plateau avec un none en moins ", self.plateau)
                if abs(move - initial_position) < 20:
                    print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9])
                    self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9] = None
                    print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9])
                else:
                    print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11])
                    self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11] = None
                    print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11])
                print("plateau avec un none en plus ", self.plateau)

            num_case = self.ordiJoueur.selected
            colonne = num_case % 10
            ligne = num_case // 10
            y = ligne * case + case / 2
            x = colonne * case + case / 2

            if num_case in self.ordiJoueur.pions_b:
                pion = self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill='SlateGray2')

            else:
                pion = self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill='SlateGray4')

            print("selection ordi=", move)
            self.ordiJoueur.deplacement(initial_position, move - 1)
            print(move)
            deltaY = (move // 10) * case + case / 2 - y
            deltaX = (move % 10) * case + case / 2 - x
            self.can1.move(pion, deltaX, deltaY)
            self.Joueur = 1 - self.ordiJoueur.joueur_IA
            self.selected = -1
            self.damier()
            self.place_pions()
            self.nb_tours+=1
            print("tour==========", self.nb_tours)
            return self.can1.bind("<Button-1>", self.select)

    def select(self, event, case = 40):
        # on détermine la case ou s'est passé la selection
        ligne = (event.y//case)
        colonne = (event.x//case)
        num_case = ligne*10+colonne
        print(ligne, '\n', colonne)
        print(num_case)
        pions = self.ordiJoueur.pions_b if self.Joueur == 1 else self.ordiJoueur.pions_n
        if self.Joueur == self.ordiJoueur.joueur_IA:
            return self.appelIA(case, 1-self.ordiDebute)

        if self.selected == -1:
            if num_case in pions:
                self.selected = num_case
            print("coucou", num_case)
            self.ordiJoueur.possibilitees(num_case)
            print("DAME.....", self.ordiJoueur.dame_n, self.ordiJoueur.dame_n)
        print(self.selected)
        if self.Joueur!=self.ordiJoueur.joueur_IA:
            y = ligne * case + case / 2
            x = colonne * case + case / 2
            if self.ordiJoueur.deplacement(num_case, selection= self.selected) :

                initial_position= self.selected // 2 +1
                deplacement_pion = (initial_position,  num_case//2+1)
                print(deplacement_pion)
                move = num_case
                tupleAdeplacer = self.plateau[deplacement_pion[0]]
                if self.Joueur == 1 and num_case in [90,92,94,96,98]:

                    tupleAdeplacer = (self.Joueur, True)
                    self.ordiJoueur.deplacementDameNoir(num_case, self.selected)

                elif self.Joueur == 0 and num_case in [1,3,5,7,9]:

                    tupleAdeplacer = (self.Joueur, True)
                    self.ordiJoueur.deplacementDameBlanc(num_case, self.selected)

                print(tupleAdeplacer)
                self.plateau[deplacement_pion[0]] =None
                self.plateau[deplacement_pion[1]] = tupleAdeplacer

                print("diff = ", abs(deplacement_pion[1]-deplacement_pion[0]))
                if abs(move - initial_position) in [k for k in range(16,25)]:

                    print("j'ai mangé")
                    print("plateau avec un none en moins ", self.plateau)
                    if move in self.ordiJoueur.pions_b and (
                            move + initial_position) // 2 in self.ordiJoueur.pions_n:
                        print("coucou je mange un noir")
                    # self.ordiJoueur.pions_n.remove((move + initial_position) // 2)
                        # self.ordiJoueur.pions_n.append(-1)
                        self.ordiJoueur.blanc += 1
                    elif move in self.ordiJoueur.pions_n and (
                                move + initial_position) // 2 in self.ordiJoueur.pions_b:
                        print("coucou je mange un blanc")

                            # self.ordiJoueur.pions_b.remove((move + initial_position) // 2)
                            # self.ordiJoueur.pions_b.append(-1)
                        self.ordiJoueur.noir += 1
                    if abs(move - initial_position) < 20:
                        print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9])
                        self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9] = None
                        print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 9])
                    else:
                        print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11])
                        self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11] = None
                        print(self.plateau[max(deplacement_pion[1], deplacement_pion[0]) - 11])
                    print("plateau avec un none en plus ", self.plateau)

                if num_case in self.ordiJoueur.pions_b:
                    pion = self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill='SlateGray2')

                else:
                    pion = self.can1.create_oval(x - 15, y - 15, x + 15, y + 15, fill='SlateGray4')

                self.can1.moveto(pion, move%10*case+case/2, move//10*case+case/2)

                self.damier()
                self.place_pions()
                self.Joueur = self.ordiJoueur.joueur_IA
                return self.appelIA(case, 1-self.ordiDebute)

    def interface(self, case = 40):

        self.can1.pack(side=Tk.TOP)
        
        self.chaine.configure(text="", fg='red')
        self.chaine.pack()
        
        self.txt1.pack()
        self.txt2.pack()
        bt1 = Tk.Button(self.fenetre, text='Quitter', command=self.fenetre.destroy)
        bt1.pack(side=Tk.LEFT)
        self.damier()
        self.place_pions()
        print(self.plateau)

        print(self.ordiDebute)
        self.can1.bind("<Button-1>", self.select)
        if self.ordiJoueur.blanc == 20:
            self.txt1.configure(text='Blancs gagnent')
            self.fenetre.destroy()

        elif self.ordiJoueur.noir==20 :

            self.txt1.configure(text='Noirs gagnent')
            self.fenetre.destroy()


        self.damier()
        self.place_pions()
        self.fenetre.mainloop()

    
jeu = JeuDeDame()
jeu.interface()


