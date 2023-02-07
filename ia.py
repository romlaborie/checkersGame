import random

class AI():

    def __init__(self):

        self.pos = list()
        self.prenable = list()
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
                self.pos.extend(self.moves_possible)
                print(self.pos)
                if len(self.prenable) > 0:
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
            self.possibilitees() #recalcule self.prenable
            print("prenable =  ", self.prenable)

        self.moves_possible = listeDeCasesPossibles[i]
        if self.selected%10 == 9:
            if not self.case_libre(min(self.moves_possible)):
                move = 9+min(self.moves_possible)
            else :
                move = min(self.moves_possible)

        elif self.selected%10 == 1 :
            if not self.case_libre(max(self.moves_possible)):
                move =11 + max(self.moves_possible)
            else:
                move = max(self.moves_possible)

        else :
            k = random.randint(0, len(self.moves_possible) - 1)
            while not self.case_libre(self.moves_possible[k]):
                k = random.randint(0, len(self.moves_possible) - 1)

            print(k)
            move = self.moves_possible[k]
        print("blancs ", self.pions_b)
        print("noirs ", self.pions_n)
        if self.joueur_IA == 1:
            print("select = ", self.selected)
            self.pions_b.remove(self.selected)
            self.pions_b.append(move)
            self.pionsABouger = list()
            print(move)
        else:
            print("select = ", self.selected)
            self.pions_n.remove(self.selected)
            self.pions_n.append(move)
            self.pionsABouger = list()
            print(move)



        # self.moves_possible=list()
        self.choix = self.selected//2+1 #if self.selected%20>10 else self.selected//2-1


        return (self.choix , move//2+1) # if move%20>10 else move//2-1)

        #return tuple qui met à jour le plateau dans l'autre module

    def CheckAttaquePossibleBlanc(self, dest, coordAttaque):

        if self.case_libre(dest) and coordAttaque in self.pions_n:
            self.pos.append(dest)
            self.prenable.append(dest)
            self.prenable.append(coordAttaque)

    def CheckAttaquePossibleNoir(self, dest, coordAttaque):

        if self.case_libre(dest) and coordAttaque in self.pions_b:
            self.pos.append(dest)
            self.prenable.append(dest)
            self.prenable.append(coordAttaque)

    def PionMange(self, dest, listePionsAManger, listePionsARafraichir, selection):
        print("destination ", dest)
        print("selection ", selection)
        listePionsAManger[listePionsAManger.index((dest+selection)//2)]=-1

        listePionsARafraichir[listePionsARafraichir.index(selection)] = dest

    def deplacementPionBlanc(self, dest, selectJoueur):
        selection =  selectJoueur
        self.pions_b[self.pions_b.index(selection)] = dest

    def deplacementPionNoir(self, dest, selectJoueur):
        selection =  selectJoueur
        self.pions_n[self.pions_n.index(selection)] = dest

    def deplacementDameBlanc(self, dest, selectJoueur):
        selection = selectJoueur
        if selection in self.dame_b:

            self.dame_b[self.dame_b.index(selection)] = dest
        else :
            self.creationDameBlanche(dest)

    def deplacementDameNoir(self, dest, selectJoueur):
        selection = selectJoueur
        if selection in self.dame_n:

            self.dame_n[self.dame_n.index(selection)] = dest
        else:
            self.creationDameNoire(dest)

    def creationDameNoire(self, dest):
        self.dame_n.append(dest)

    def creationDameBlanche(self, dest):
        self.dame_b.append(dest)

    def deplacement(self, dest, selection):

        ligne = dest // 10
        print("prenable = ", self.prenable)
        print("dest = ", dest)
        self.prenable.extend(self.pos)
        if dest in self.prenable:
            if selection in self.pions_b:
                print("diff =", dest-selection)
                if abs(dest-selection) > 11:
                    print("jesuislàetmangenoir")
                    self.PionMange(dest, self.pions_n, self.pions_b, selection)
                    self.blanc+=1
                else:
                    print("jesuislà")
                    self.deplacementPionBlanc(dest, selection)
                if ligne == 9 :
                    self.creationDameBlanche(dest)

            elif selection in self.pions_n:
                print("diff =", dest - selection)
                if abs(dest-selection)>11:
                    print("jesuislàetmangeblanc")
                    self.PionMange(dest, self.pions_b, self.pions_n, selection)
                    self.noir+=1
                else:
                    print("jesuisicietnoir")
                    self.deplacementPionNoir(dest, selection)
                if ligne == 0 :
                    self.creationDameNoire(dest)
            if selection in self.dame_b:
                if abs(dest-selection) >11:
                    self.PionMange(dest, self.pions_n, self.dame_b, selection)
                    self.blanc+=1
                else:
                    self.deplacementDameBlanc(dest, selection)
            elif selection in self.dame_n:
                if abs(dest-selection) >11:
                    self.PionMange(dest, self.pions_b, self.dame_n, selection)
                    self.noir+=1
                else:
                    self.deplacementDameNoir(dest, selection)

            print(self.dame_n)
            print(self.dame_b)
            print(self.pions_n)
            print(self.pions_b)
            return True
        else:
            return False

    def case_libre(self, plateau, c):

        if plateau[c]==None:

            return True
        else :
            return False

    def possibilitees(self, plateau, num_selected):
        self.pos=[]
        self.prenable=[]
        
        print(num_selected)
        # on évalue les positions autorisées
        #attention à 6 puis 5
        if plateau[num_selected][1]==True and plateau[num_selected][0]==1:

            c = num_selected + 4
            print(c)
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c + 5
                self.CheckAttaquePossibleNoir(c2, c)

            c = num_selected - 4
            print(c)
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c - 5
                self.CheckAttaquePossibleNoir(c2, c)

            c = num_selected + 5
            print(c)
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c + 6
                self.CheckAttaquePossibleNoir(c2, c)
            c = num_selected - 5
            print(c)
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c - 6
                self.CheckAttaquePossibleNoir(c2, c)
        elif plateau[num_selected][1]==False and plateau[num_selected][0]==1:

            c = num_selected + 4
            print(c)
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c + 5
                self.CheckAttaquePossibleNoir(c2, c)
            c = num_selected - 4
            c2 = c - 5
            self.CheckAttaquePossibleNoir(c2, c)

            c = num_selected + 5
            print(c)
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c + 6
                self.CheckAttaquePossibleNoir(c2, c)
            c = num_selected - 5
            c2 = c - 6
            self.CheckAttaquePossibleNoir(c2, c)

        elif plateau[num_selected][1]==True and plateau[num_selected][0]==0:
            c = num_selected - 5
            print(c)
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c - 4
                self.CheckAttaquePossibleBlanc(c2, c)

            c = num_selected + 5
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c + 4
                self.CheckAttaquePossibleBlanc(c2, c)

            c = num_selected + 5
            print(c)
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c + 6
                self.CheckAttaquePossibleBlanc(c2, c)
            c = num_selected - 5
            if self.case_libre(plateau,c):
                self.pos.append(c)
            else:
                c2 = c - 6
                self.CheckAttaquePossibleBlanc(c2, c)
        elif plateau[num_selected][1]==False and plateau[num_selected][0]==0:
            c = num_selected - 4
            print(c)
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c - 5
                self.CheckAttaquePossibleBlanc(c2, c)
            c = num_selected + 4
            c2 = c + 5
            print(c)
            self.CheckAttaquePossibleBlanc(c2, c)
            c = num_selected - 5
            print(c)
            if self.case_libre(plateau, c):
                self.pos.append(c)
            else:
                c2 = c - 6
                self.CheckAttaquePossibleBlanc(c2, c)
            c = num_selected + 5
            c2 = c + 6
            print(c)
            self.CheckAttaquePossibleBlanc(c2, c)

        print("prenable = ", self.prenable)

        return self.prenable



