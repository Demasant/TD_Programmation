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
        """Computes the derivative of the tree with respect to a variable"""
        if self.is_leaf():
            if self.__label == var:
                return Tree('1')
            else:
                return Tree('0')
        elif self.__label == '+':
            return Tree('+', self.child(0).deriv(var), self.child(1).deriv(var))
        elif self.__label == '*':
            return Tree('+', Tree('*', self.child(0).deriv(var), self.child(1)),
                        Tree('*', self.child(0), self.child(1).deriv(var)))

    def substitute(self, t1, t2):
        """Substitutes all occurrences of t1 with t2"""
        if self == t1:
            return t2
        else:
            new_children = [child.substitute(t1, t2) for child in self.__children]
            return Tree(self.__label, *new_children)

    def simplify(self):
        """Performs simplification of the tree"""
        if self.is_leaf():
            return self
        elif self.__label == '+':
            if self.child(0) == Tree('0'):
                return self.child(1).simplify()
            elif self.child(1) == Tree('0'):
                return self.child(0).simplify()
            else:
                return Tree('+', self.child(0).simplify(), self.child(1).simplify())
        elif self.__label == '*':
            if self.child(0) == Tree('0') or self.child(1) == Tree('0'):
                return Tree('0')
            elif self.child(0) == Tree('1'):
                return self.child(1).simplify()
            elif self.child(1) == Tree('1'):
                return self.child(0).simplify()
            else:
                return Tree('*', self.child(0).simplify(), self.child(1).simplify())
        else:
            return self




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

    print("Depth:", arbre.depth())
    print("Derivative with respect to 'b':", arbre.deriv('b'))
    print("Substitute 'a' with 'c':", arbre.substitute(Tree('a'), Tree('c')))
    print("Simplified tree:", arbre.simplify())