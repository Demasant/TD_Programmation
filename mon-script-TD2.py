####TD2

###EXERCICE 1&2

import math as mt

## ======= Class

class Fraction:
    #pour referencer l'objet on met self en argument
    #il n'y a pas de receveur pour la fonction __init__
    def __init__(self, n, d):
        """Initialize the fraction object with numerator and denominator"""
        self.num = n
        self.denum = d

    def printFraction(self):
        """Prints nicely the fraction"""
        #2 methodes possibles :
        #print(str(self.num)+'/'+str(self.denum))
        #print("{}/{}".format(self.num,self.denum))
        print("{}/{}".format(self.num,self.denum))

    def to_str(self):
        """Returns a string of the fraction"""
        return("{}/{}".format(self.num,self.denum))

    def add(self,fraction):
        """Returns new fraction that is sum of self and fraction"""
        new_num = self.num * fraction.denum + self.denum * fraction.num
        new_denum = self.denum*fraction.denum
        return Fraction(new_num,new_denum)

    def mult(self,fraction):
        """Returns new fraction that is with mulitplication of self and fraction"""
        new_num = self.num*fraction.num
        new_denum = self.denum * fraction.denum
        return Fraction(new_num,new_denum)

    def simplify(self):
        """Returns simplified version of self"""
        pgcd = mt.gcd(self.num,self.denum)
        new_num = self.num//pgcd
        new_denum = self.denum//pgcd
        #on peut aussi utiliser int(self.num / pgcd)
        return Fraction(new_num,new_denum)

    def isEqual(self, fraction):
        """Returns true if self is equivalent to fraction"""
        irr1 = self.simplify()
        irr2 = fraction.simplify()
        if irr1.num == irr2.num and irr1.denum == irr2.denum:
            return True
        return False


## ======= Script/Main


if __name__ == "__main__":
    frac_1 = Fraction(4,6)
    frac_1.printFraction()
    frac_2 = Fraction(2,5)
    frac_add = frac_1.add(frac_2)
    frac_add.printFraction()
    frac_mult = frac_1.mult(frac_2)
    frac_mult.printFraction()
    frac_simp = frac_1.simplify()
    frac_simp.printFraction()

###EXERCICE 3

## ======= Fonctions

def H(n):
    """Returns the value of H(n)"""
    res = Fraction(0,1)
    for k in range(1,n+1):
        res = res.add(Fraction(1,k))
    res = res.simplify()
    return res

## ======= Script/Main
Hrep = H(10000)
Hrep.printFraction()




