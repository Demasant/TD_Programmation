####TD3

###EXERCICE

## ======= Class

class Tree:
    def __init__(self, label, *children):
        self.__label = label
        #self.label = label
        self.__children = children

    def getLabel(self):
        """Returns label in nod"""
        return self.__label

    def getChildren(self):
        """Returns tuple of tree"""
        return self.__children

    def nb_children(self):
        """Returns number of children"""
        return len(self.__children)

    def child(self,i):
        """Returns the ith subtree"""
        if i >= self.nb_children():
            raise IndexError
        return self.__children[i]

    def is_leaf(self):
        """Returns True if tree is leaf"""
        return self.nb_children() == 0

    def __str__(self):
        """Turns Tree into str"""
        out = "({})".format(self.__label)
        if self.is_leaf():
            return out
        out += "("
        for child in self.__children:
            out += child.__str__() + ";"
        out += ")"
        return out

    def __eq__(self,tree2):
        return self.__label == tree2.__label and self.__children == tree2.__children

    def depth(self):
        """Returns the depth of the tree"""
        if self.is_leaf():
            return 0
        L = list()
        for child in self.__children:
            L.append(depth(child))
        return max(L) + 1

    def deriv(self, var):
        """Calcule la dérivée de l'arbre par rapport à une variable"""
        if self.is_leaf():
            if self.__label == var:
                return Tree('1')
            else:
                return Tree('0')
        elif self.__label == '+':
            return Tree('+', self.child(0).deriv(var), self.child(1).deriv(var))
        elif self.__label == '*':
            return Tree('+',
                        Tree('*', self.child(0).deriv(var), self.child(1)),
                        Tree('*', self.child(0), self.child(1).deriv(var)))
        else:
            return Tree('0')






## ======= Fonctions

## ======= Script/Main

if __name__ == "__main__" :

    branche_1 = Tree('a')
    branche_2 = Tree('b')
    arbre = Tree('f',branche_1,branche_2)
    print(type(arbre.getChildren()))
    print(arbre.getLabel())

    print(arbre.__str__())
    child_1 = arbre.child(0)
    print(child_1.__str__())
    print(child_1.is_leaf())


# Création de l'arbre représentant le polynôme 3*X^2 + 5*X + 7
    polynome = Tree('+',
                    Tree('+',
                         Tree('+', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                         Tree('*', Tree('5'), Tree('X'))),
                    Tree('7'))

    # Calcul de la dérivée par rapport à X
    derivee = polynome.deriv('X')

    # Affichage de la dérivée
    print("La dérivée du polynôme 3*X^2 + 5*X + 7 par rapport à X est :", derivee)