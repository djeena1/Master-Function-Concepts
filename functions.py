import random
import string

#Exo 3 : kreye yon fonksyon ki pou jenere yon kòd
aleyatwa ki gen n karaktè alfabetik, san
repetisyon.

alphabet = string.ascii_lowercase
def  unique_alphabetical (length):
    code = ""
    for i in range(length):
        char = random.choice(alphabet)
        while char in code:
            char = random.choice(alphabet)
        code += char
    return code
