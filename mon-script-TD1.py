#gabriel.sauger@loria.fr

####TD1

###EXERCICE 1-2

tirage = ["a","r","b","g","e","s","c","j"]
path = "frenchssaccent.dic"

## ======= Fonctions

#fonction read_file(path) : returns l'ensemble des mots avec le bon nombre de lettres

def read_file(path):
    # charge les données de path dans une liste et retourne la list
    output = list()
    file = open(path,"r")
    for line in file :
        # line := "hello\n"
        mot = line[0:len(line)-1]
    # éliminer les mots de taille > len(tirage)
        if len(mot) <= len(tirage):
            output.append(mot)
        # output.append(line.replace("\n","")
    file.close()
    return output

#fonction isMotPossible(tirage,mot) : returns True si mot peut être écrit avec tirage

def isMotPossible(tirage,mot) :
    # si on ne peut pas écrire le mot avec le tirage :
    copie_tirage = list(tirage)
    for letter in list(mot):
        if letter not in copie_tirage:
            return False
    # si on peut écrire le mot avec le tirage :
        else :
            copie_tirage.remove(letter)
    return True

#fonction find_mots(tirage,liste_mots) : returns l'ensemble des mots possibles

def find_mots(tirage,liste_mots):
    # liste_mots_possibles = {mot in liste_mots | isMotPossible(tirage,mot)}
    return { mot for mot in liste_mots if isMotPossible(tirage,mot) == True}


#fonction find_longest(lexique) : returns le mot le plus long possible

def find_longest(lexique):
    longest = ''
    for word in lexique :
        #compare taille des mots
        if len(word) > len(longest):
            longest = word
    return longest

## ======= Script/Main

# charger les données dans la liste_mots depuis frenchssaccent.dic

liste_mots = read_file(path)

# parcourir les mots et garder ceux que l'on peut écrire

lexique = find_mots(tirage,liste_mots)

# trouver le plus long

print('Le mot le plus long est :')
print(find_longest(lexique))

###EXERCICE 3

## ======= Fonctions

# fonction score(mot) : returns le score du mot

def score(mot):
    score = 0
    for lettre in mot:
        if lettre in 'aeilnorstu':
            score = score + 1
        elif lettre in 'dgm':
            score = score + 2
        elif lettre in 'bcp':
            score = score + 3
        elif lettre in 'fhv':
            score = score + 4
        elif lettre in 'jq':
            score = score + 8
        else :
            score = score + 10
    return score

# fonction max_score(lexique) : returns le mot avec le meilleur score parmis les mots possibles ainsi que son score

def max_score(lexique):
    best_score = 0
    best_mot = ''
    for mot in lexique:
        if score(mot) > best_score:
            best_mot = mot
            best_score = score(mot)
    return best_mot,best_score

## ======= Script/Main

# charger les données dans la liste_mots depuis frenchssaccent.dic

liste_mots = read_file(path)

# parcourir les mots et garder ceux que l'on peut écrire

lexique = find_mots(tirage,liste_mots)

# trouver celui maximisant les points

print('Le mot avec le meilleur score est :')
print(max_score(lexique))

###EXERCICE 4

## ======= Fonctions

from itertools import permutations

# fonction isMotPossible(tirage, mot) : returns True si mot peut être écrit avec tirage, en tenant compte d'un joker

def isMotPossible(tirage, mot):
    # si la longueur du mot est plus grande que le tirage, on le rejette
    if len(mot) > len(tirage):
        return False

    # vérifie si le mot peut être formé en utilisant les lettres du tirage ou en utilisant un joker
    copie_tirage = list(tirage)
    joker_used = False

    for lettre in list(mot):
        if lettre in copie_tirage:
            copie_tirage.remove(lettre)
        elif not joker_used:
            joker_used = True
        else:
            return False

    return True

# fonction generate_permutations_with_joker(tirage, mot) : returns une liste de toutes les permutations possibles en utilisant un joker

def generate_permutations_with_joker(tirage, mot):
    permutations_list = []
    for i in range(len(mot)):
        if mot[i] == '?':
            for lettre in tirage:
                new_mot = mot[:i] + lettre + mot[i+1:]
                permutations_list.append(new_mot)
        else:
            permutations_list.append(mot)
    return permutations_list

# fonction find_mots(tirage, liste_mots) : returns l'ensemble des mots possibles en tenant compte d'un joker

def find_mots(tirage, liste_mots):
    mots_possibles = set()
    for mot in liste_mots:
        if isMotPossible(tirage, mot):
            mots_possibles.add(mot)
        else:
            # ajoute les permutations possibles avec un joker
            for permutation in generate_permutations_with_joker(tirage, mot):
                if isMotPossible(tirage, permutation):
                    mots_possibles.add(permutation)
    return mots_possibles

## ======== Script/Main

# tirage et path définis précédemment

# charger les données dans la liste_mots depuis frenchssaccent.dic
liste_mots = read_file(path)

# parcourir les mots et garder ceux que l'on peut écrire en tenant compte d'un joker
lexique = find_mots(tirage, liste_mots)

# trouver celui maximisant les points
print('Le mot avec le meilleur score en tenant compte d\'un joker est :')
print(max_score(lexique))
