import random
import string

#Exo 3
"""kreye yon fonksyon ki pou jenere yon kòd
aleyatwa ki gen n karaktè alfabetik, san
repetisyon."""

alphabet = string.ascii_lowercase
def  unique_alphabetical (length):
    code = ""
    for i in range(length):
        char = random.choice(alphabet)
        while char in code:
            char = random.choice(alphabet)
        code += char
    return code


# Exo 4
"""kreye yon fonksyon ki pou jenere yon köd
aleyatwa ki gen n karaktè alafanimerik, san
repetisyon."""

alphanumeric = string.ascii_lowercase + string.ascii_uppercase +string.digits
def unique_alphanumerical(length):
    code = ""
    for i in range(length):
        char = random.choice(alphanumeric)
        while char in code:
            char = random.choice(alphanumeric)
        code += char
    return code


# Exo 5
"""Ou gen yon lis chenn. Jenere yon SLUG apati
chenn nan. Nan yon SLUG, tout karaktè ki
akseptab yo se: alfanimerik ak "-" """

def slug(chenn):
    rezilta = ""
    for char in chenn:
        if char in (string.ascii_lowercase + string.ascii_uppercase + "-_"):
            rezilta += char
    return rezilta


# Exo 6        
"""Kreye yon fonksyon ki ap separe chak lèt nan yon
mo ak yon vigil"""      
                 
def Separate (word):
    return ",".join(list(word))


# Exo 7
"""Kreye yon fonksyon ki ap kripte yon mo, avèk
endèks li nan alfabè a. Chak karaktè dwe separe
ak yon tire.
>>> "ALO"
>>>
"0-11-14" """

def crypt(word):
    """ """
    position = []
    for char in word.upper():
        position.append(str(string.ascii_uppercase.index(char)))   
    return "-".join(position)


# Exo 8
"""Kreye yon fonksyon ki ap dekripte yon mo ki fèt
ak endeks chak lèt nan alfabè a, separe ak yon
tirè
"0-11-14"
>>> "ALO" """

def decrypt(word):
    position = []
    for char in word.split("-"):
        position.append(str(string.ascii_uppercase[int(char)])) 
    return "".join(position)


# Exo 9
"""Kreye yon fonksyon ki ap pran 2 paramèt, epi ki
pèmite valè yo. Answit li retounen tou 2 valè yo
sou föm Tuple."""

def Permutation (a,b):
    return b, a



#Exo 10
"""Kreye yon fonksyon ki ap pran yon non an
paramèt, epi ki retounen inisyal yo. Atansy' HT ≤
non konpoze ak tirè yo."""

def Initial (name):
    initial = ""
    name= name.replace("-"," ")
    for i in name.split():
        initial += i[0]
    return initial
