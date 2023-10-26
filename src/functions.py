import string
import random

def link_gen(mogitype : str) -> str :
    slink = mogitype
    
    size = 5
    charlist = string.ascii_letters + string.digits
    char = ''.join(random.choice(charlist) for i in range(size))
    
    return slink + char

print(link_gen("2v2"))