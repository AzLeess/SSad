#Encoder césar gauche droite si on donne en entrée par exemple 'Bonjour' elle code le B puis le o ...
def cesar_gd(s,decalage):
    chaine_codee = ""
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('a'))    
        else:
            chaine_codee = chaine_codee + element
            
    return chaine_codee      



print (cesar_gd('tbmvu dbwb fu upj', -1))




#permet de dcoder le chiffrement césar codé par la fct en haut

def decode_cesar_gauche_droite(s,decalage):
    chaine_clair = ""
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice + decalage) % 26
            chaine_clair = chaine_clair + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice + decalage) % 26
            chaine_clair = chaine_clair + chr(indice + ord('a'))
        
        else:
            chaine_clair = chaine_clair + element
            
    return chaine_clair      



print (decode_cesar_gauche_droite('tbmvu dbwb fu upj',-1))
#iqbkj sqlq uj jey



#Encoder césar droite gauche  si on donne en entrée par exemple 'Bonjour' elle code le r puis le u ...

def cesar_dg(s,decalage):
    chaine_codee = ""
    length_s=len(s)
    sliced_s=s[length_s::-1] 
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice + decalage) % 26
            chaine_codee = chaine_codee + chr(indice + ord('a'))
        
        else:
            chaine_codee = chaine_codee + element
            
    return chaine_codee      



print (cesar_dg('RUOJNOB',3))



def decode_cesar_droite_gauche(s,decalage):
    chaine_clair = ""
    length_s=len(s)
    sliced_s=s[length_s::-1]
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice + decalage) % 26
            chaine_clair = chaine_clair + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice + decalage) % 26
            chaine_clair = chaine_clair + chr(indice + ord('a'))
        
        else:
            chaine_clair = chaine_clair + element
            
    return chaine_clair      



print (decode_cesar_droite_gauche('UXRMQRE ',-3))


#Encode avec le décalage droit
def encode_decalage_droite(s):
    chaine_codee = ""
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice + 1) % 26
            chaine_codee = chaine_codee + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice + 1) % 26
            chaine_codee = chaine_codee + chr(indice + ord('a'))
        
        else:
            chaine_codee = chaine_codee + element
            
    return chaine_codee      



print (encode_decalage_droite('z'))




def encode_decalage_gauche(s):
    chaine_codee = ""
    for element in s:
        if 'A' <= element <= 'Z':
            indice = ord(element)-ord('A')
            indice = (indice - 1) % 26
            chaine_codee = chaine_codee + chr(indice + ord('A'))
        elif 'a' <= element <= 'z':
            indice = ord(element)-ord('a')
            indice = (indice - 1) % 26
            chaine_codee = chaine_codee + chr(indice + ord('a'))
        
        else:
            chaine_codee = chaine_codee + element
            
    return chaine_codee      



print (encode_decalage_gauche('z'))




def inverseModulaire(aModulo, bNombre):
    """ Algorithme d'Euclide étendu pour trouver l'inverse modulaire 
        Inverse modulaire de B modulo A ---> B * B^-1 mod A = 1 """
    
    modulo = aModulo
    
    x = 0
    y = 1
    u = 1
    v = 0
    
    while bNombre != 0:
        q = aModulo // bNombre
        r = aModulo % bNombre
        
        m = x - u * q
        n = y - v * q
        
        aModulo = bNombre
        bNombre = r
        x = u
        y = v
        u = m
        v = n
        
    return x % modulo if aModulo == 1 else 0


def pgcd(a,b):
    
    while b!=0:
        r=a%b
        a,b=b,r
    return a

def code_affine(s, a, b):
    

    if pgcd(a,26) != 1:
        encode_decalage_droite(s,b)
    else:
        
        
        chaine_codee = ""
        for element in s:
            if 'A' <= element <= 'Z':    
                indice = ord(element) - ord('A')
                indice = (indice * a + b) % 26
                chaine_codee += chr(indice + ord('A'))
            elif 'a' <= element <= 'z':
                indice = ord(element) - ord('a')
                indice = (indice * a + b) % 26
                chaine_codee += chr(indice + ord('a'))
           
            
    return  chaine_codee




def decode_affine(s, a, b):

    if pgcd(a,26) != 1:
        print('la valeur de a est invalide')
    else:
        
        chaine_codee = ""
        for element in s:
            if 'A' <= element <= 'Z': 
                indice = ord(element) - ord('A')
                indice = ((indice - b)* inverseModulaire(26, a)) % 26
                chaine_codee += chr(indice + ord('A'))
            elif 'a' <= element <= 'z':
                indice = ord(element) - ord('a')
                indice = ((indice - b)* inverseModulaire(26, a)) % 26
                chaine_codee += chr(indice + ord('a'))
        
        
    return  chaine_codee










def affine(s,a,b,type) :
    if type == 1 :
        return code_affine(s, a, b)
    else :
        return decode_affine(s, a, b)

print (code_affine('BONJOUR', 5, 9))
print(affine('salam sahbi', 5, 9,1))

print (decode_affine('OBWCBFQ', 5, 9))
print(affine('vjmjrvjsox', 5, 9,0))




## ajout de la signature aux chaines de caractere crypte 

#def signe ( s , typ,dec1 , dec2) :
#    if typ == 'cesar':
#        if 
#        cesar_dg(s,dec1)
#    elif typ == 'affine':
#    elif typ == 'mirroir':
    

def mirroir (s):
    return s[::-1]

#print (mirroir('salut'))