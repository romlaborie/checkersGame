import random

class AI():

    def __init__(self):

        self.pos = list()
        self.prenable = list()
        self.pionsAPrendre=list()
        self.joueur_IA=0
        self.case =40
        self.moves_possible = list()
        self.pionsABouger = list()

    def CherchePionsADeplacer(self, plateau, joueur):

        listeRetour = list()
        for i in range(1, len(plateau)):

            if plateau[i] != None and plateau[i][0]==joueur:
                print(plateau)
                self.moves_possible = self.possibilitees(plateau, i)

                print(self.pos)
                if len(self.pionsAPrendre) > 0:
                    for k in range(10):
                        listeRetour.append(self.moves_possible)
                    self.pionsABouger.extend([i for k in range(10)])
                if len(self.pos) > 0:
                    print(listeRetour)
                    listeRetour.append(self.moves_possible)
                    listeRetour[len(listeRetour) - 1].extend(self.pos)
                    self.pionsABouger.append(i)

        return listeRetour

    def play(self, plateau, premier_joueur):

        self.joueur_IA = 0 if premier_joueur==True else 1

        #gestion aleatoire
        #self.choix = appel à cherchePionAdeplacer

        listeDeCasesPossibles = self.CherchePionsADeplacer(plateau, self.joueur_IA)

        print(self.pionsABouger)
        i = random.randint(0, len(self.pionsABouger)-1)
        print(i)
        selection = self.pionsABouger[i]
        if self.pionsABouger.count(self.pionsABouger[i])>=10:
            self.possibilitees(plateau, selection) #recalcule self.pionsAPrendre
            print("pionsAPrendre =  ", self.pionsAPrendre)

        self.moves_possible = listeDeCasesPossibles[i]
        if selection%10 == 5 and plateau[selection][0]==1:
            if not self.case_libre(plateau, min(self.moves_possible)):
                move = 4+min(self.moves_possible)
            elif self.case_libre(plateau, min(self.moves_possible)) :
                move = min(self.moves_possible)

        elif selection%10 == 6 and plateau[selection][0]==1:
            if not self.case_libre(plateau, max(self.moves_possible)):
                move =6 + max(self.moves_possible)
            elif self.case_libre(plateau, max(self.moves_possible)):
                move = max(self.moves_possible)

        elif selection%10 == 5 and plateau[selection][0]==0:
            if not self.case_libre(plateau, min(self.moves_possible)):
                move = min(self.moves_possible)-6
            else :
                move = min(self.moves_possible)

        elif selection%10 == 6 and plateau[selection][0]==0:
            if not self.case_libre(plateau, max(self.moves_possible)):
                move =max(self.moves_possible)-4
            else:
                move = max(self.moves_possible)

        else :
            k = random.randint(0, len(self.moves_possible) - 1)
            while not self.case_libre(plateau, self.moves_possible[k]):
                k = random.randint(0, len(self.moves_possible) - 1)

            print(k)
            move = self.moves_possible[k]


        self.pionsABouger = list()
        print("TUPLE = ", (selection, move))
        return (selection, move)

        #return tuple qui met à jour le plateau dans l'autre module

    def CheckAttaquePossibleBlanc(self, plateau, dest, coordAttaque):

        if self.case_libre(plateau, dest) and plateau[coordAttaque][0]==1:
            self.pos.append(dest)
            self.prenable.append(dest)
            self.prenable.append(coordAttaque)

    def CheckAttaquePossibleNoir(self, plateau, dest, coordAttaque):

        if self.case_libre(plateau, dest) and plateau[coordAttaque][0]==0:
            self.pos.append(dest)
            self.prenable.append(dest)
            self.prenable.append(coordAttaque)

    def case_libre(self, plateau, c):

        if c>0 and plateau[c]==None:

            return True
        else :
            return False

    def possibilitees(self, plateau, num_selected):
        self.pos=[]
        self.prenable=[]
        self.pionsAPrendre=[]
        print(num_selected)
        # on évalue les positions autorisées
        #attention à 6 puis 5
        if (num_selected-1)%10>=5:

            if plateau[num_selected][1]==True and plateau[num_selected][0]==1:

                c = num_selected + 4
                print(c)
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected - 5
                print(c)
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c - 4
                    self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected + 5
                print(c)
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c + 6
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 6
                print(c)
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c - 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
            elif plateau[num_selected][1]==False and plateau[num_selected][0]==1:

                c = num_selected + 4
                print(c)
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 5
                c2 = c - 4
                self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected + 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 6
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 6
                c2 = c - 5
                self.CheckAttaquePossibleNoir(plateau, c2, c)

            elif plateau[num_selected][1]==True and plateau[num_selected][0]==0:
                c = num_selected - 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 4
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)

                c = num_selected + 4
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)

                c = num_selected + 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 6
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected -6
                if self.case_libre(plateau,c):
                    self.pos.append(c)
                else:
                    c2 = c - 5
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
            elif plateau[num_selected][1]==False and plateau[num_selected][0]==0:
                c = num_selected - 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 4
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected + 4
                c2 = c + 5
                print(c)
                self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected - 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 6
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected + 6
                c2 = c + 5
                print(c)
                self.CheckAttaquePossibleBlanc(plateau, c2, c)

        else :
            if plateau[num_selected][1] == True and plateau[num_selected][0] == 1:

                c = num_selected + 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 4
                    self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected - 4
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected + 6
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 6
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
            elif plateau[num_selected][1] == False and plateau[num_selected][0] == 1:

                c = num_selected + 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 4
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 4
                c2 = c - 5
                self.CheckAttaquePossibleNoir(plateau, c2, c)

                c = num_selected + 6
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleNoir(plateau, c2, c)
                c = num_selected - 5
                c2 = c - 6
                self.CheckAttaquePossibleNoir(plateau, c2, c)

            elif plateau[num_selected][1] == True and plateau[num_selected][0] == 0:
                c = num_selected - 4
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 5
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)

                c = num_selected + 5
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 4
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)

                c = num_selected + 6
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c + 5
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected - 5
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 6
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
            elif plateau[num_selected][1] == False and plateau[num_selected][0] == 0:
                c = num_selected - 4
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 5
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected + 5
                c2 = c + 4
                print(c)
                self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected - 5
                print(c)
                if self.case_libre(plateau, c):
                    self.pos.append(c)
                else:
                    c2 = c - 6
                    self.CheckAttaquePossibleBlanc(plateau, c2, c)
                c = num_selected + 6
                c2 = c + 5
                print(c)
                self.CheckAttaquePossibleBlanc(plateau, c2, c)
        self.pionsAPrendre = list(self.prenable)
        self.prenable.extend(self.pos)

        print("prenable = ", self.prenable)
        print("pos = ", self.pos)

        return self.prenable



