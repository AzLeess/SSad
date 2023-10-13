#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!/usr/bin/env python
# coding: utf-8

# In[30]:


Table={
    '1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G','8':'H','9':'I','10':'J','11':'K','12':'L','13':'M','14':'N','15':'O',
    '16':'P','17':'Q','18':'R','19':'S','20':'T','21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z','27':'a','28':'b','29':'c',
    '30':'d','31':'e','32':'f','33':'g','34':'h','35':'i','36':'j','37':'k','38':'l','39':'m','40':'n','41':'o','42':'p','43':'q',
    '44':'r','45':'s','46':'t','47':'u','48':'v','49':'w','50':'x','51':'y','52':'z',  '53':'0','54':'1','55':'2','56':'3','57':'4',
    '58':'5','59':'6','60':'7','61':'8','62':'9'
} 
#Palindrome qui traite le cas particulier : Radar (Si une des lettres soit en majiscule)
def check_palindrome(v): 
    reverse = v[::-1]  
    if (v.upper() == reverse.upper()): 
        return True
    return False
def find_key(v): 
    for k, val in Table.items(): 
        if v == val: 
            return k 
    return "Clé n'existe pas"
def encode_cesar_droite_gauche(s,decalage):
    chaine_codee = ""
    s = s[::-1]  
    chaine_codee = ""
    if decalage % 62 == 0:
        for element in s:
            if find_key('A') <= find_key(element) <= find_key('9'):
                indice = find_key(element)
                indice=int(indice)
                indice = ((indice + decalage) % 62)
                indice = str(indice)
                chaine_codee = chaine_codee + Table[indice]
        chaine_codee = '$./&'+ chaine_codee
        chaine_codee = chaine_codee + '$./&' 
        chaine_codee=chaine_codee[0:5]+'&/'+chaine_codee[5:len(chaine_codee)]
    else:
        for element in s:
            if find_key('A') <= find_key(element) <= find_key('9'):
                indice = find_key(element)
                indice=int(indice)
                indice = ((indice + decalage) % 62)
                indice = str(indice)
                chaine_codee = chaine_codee + Table[indice]
            else:
                chaine_codee = chaine_codee + element              
    chaine_codee = chaine_codee + '_00_'   + str(decalage) + '_d'  
    return chaine_codee   
def encode_cesar_gauche_droite(s,decalage):
    chaine_codee = ""
    if decalage % 62 == 0:
        for element in s:
            if find_key('A') <= find_key(element) <= find_key('9'):
                indice = find_key(element)
                indice = int(indice)
                indice = ((indice + decalage) % 62)
                indice = str(indice)
                chaine_codee = chaine_codee + Table[indice]
        chaine_codee = '$./&' + chaine_codee
        chaine_codee = chaine_codee + '$./&'
        chaine_codee=chaine_codee[0:5]+'&/'+chaine_codee[5:len(chaine_codee)]
    else:
        for element in s:
            if find_key('A') <= find_key(element) <= find_key('9'):
                indice = find_key(element)
                indice=int(indice)
                indice = ((indice + decalage) % 62)
                indice = str(indice)
                chaine_codee = chaine_codee + Table[indice]
            else:
                chaine_codee = chaine_codee + element              
    chaine_codee = chaine_codee + '_00_'   + str(decalage) + '_g'  
    return chaine_codee      
def decode_cesar_droite_gauche(s,decalage):
    chaine_clair = ""
    s = s[::-1]
    for element in s:
        if find_key('A') <= find_key(element) <= find_key('9'):
            indice = find_key(element)
            indice=int(indice)
            indice = ((indice + decalage) % 62)
            indice = str(indice)
            chaine_clair = chaine_clair + Table[indice]
        else:
            chaine_clair = chaine_clair + element     
    return chaine_clair        
def decode_cesar_gauche_droite(s,decalage):
    chaine_clair = ""
    for element in s:
        if find_key('A') <= find_key(element) <= find_key('9'):
            indice = find_key(element)
            indice=int(indice)
            indice = ((indice + decalage) % 62)
            indice = str(indice)
            chaine_clair = chaine_clair + Table[indice]
        else:
            chaine_clair = chaine_clair + element     
    return chaine_clair 

def decode_miroir(message_crypté):
#Maintenant pr le décryptage on supprime les caractéres spéciaux ajoutés et on ré-inverse le texte de nouveau
    message_crypté = message_crypté.replace('/&', '')
    message_crypté = message_crypté.replace('^^&~', '')
    message_crypté = message_crypté.replace('&/.$', '')
    message_decrypté = message_crypté[::-1]
    return message_decrypté 
def encode_miroir(texte):
#Spliter le texte avec les blancs et mettre chaque mots dans la liste words
    words = texte.split()
#Dans cette partie on cherche les mots palindrome dans la liste
#un palindrome subit des modification:
#ajout d'une sous chaine au début
#ajout d'une sous chaine aprés la fin
#ajout d'une sous chaine au milieu
    i=0
    while i <= len(words)-1:   
        if check_palindrome(words[i]):
            words[i] = '$./&'+ words[i]
            words[i] = words[i]+'$./&'
            palind = words[i]
            palind_2=palind[0:7]+'&/'+palind[7:8]+ '~&^^' +palind[8:len(palind)]
            words[i] = palind_2
            i=i+1
        else:
            i=i+1    
#Maintenant on va récupérer les mots de la liste ce qui fait on aura une texte comme le premier mais avec des palindromes qui 
#ont subit des modifications
    texte = ''
    i=0
    while i <= len(words)-1:    
        texte = texte + words[i] + ' '
        i=i+1    
#ceci permet de codes les blancs avec un caractére spéciale vu que notre fonction miroir ne les traitent pas
#Maintenat pour coder il nous reste rien que inverser la variable texte
    miroir = texte[::-1]
    miroir = miroir +'_01'
    miroir=str.lstrip(miroir)
    return miroir

def decryptage(data):
    liste = data.split("_")
    Key = liste[1]
    if (Key == '00')and (int(liste[2]) % 62 == 0) and (liste[3] == 'g'):
        nb_decalage = int(liste[2])
        liste[0] = liste[0].replace('$./&',"")
        liste[0]=liste[0].replace("&/","")
        message_clair = decode_cesar_gauche_droite(liste[0],-(nb_decalage))
    elif (Key == '00')and (int(liste[2]) % 62 != 0) and (liste[3] == 'g'):
        nb_decalage = int(liste[2])
        message_clair = decode_cesar_gauche_droite(liste[0],-(nb_decalage)) 
    elif (Key == '00')and (int(liste[2]) % 62 == 0) and (liste[3] == 'd'):
        nb_decalage = int(liste[2])
        liste[0] = liste[0].replace('$./&',"")
        liste[0]=liste[0].replace("&/","")
        message_clair = decode_cesar_droite_gauche(liste[0],-(nb_decalage))
    elif (Key == '00')and (int(liste[2]) % 62 != 0) and (liste[3] == 'd'):
        nb_decalage = int(liste[2])
        message_clair = decode_cesar_droite_gauche(liste[0],-(nb_decalage))     
    elif Key == '01':
        message_clair=decode_miroir(liste[0])
    else:
        return ''
        
    return message_clair


def encode_cesar(message,sens,b):
    if ( sens == "g"): 
        return encode_cesar_gauche_droite(message,b)
    else :
        return encode_cesar_droite_gauche(message,b)
        




#print(decode_cesar_droite_gauche("sq SbcVdéZéh_00_360_d",360))
#print(encode_miroir("Bonjour radar 33"))
#print(encode_cesar_droite_gauche("téléphone 24",360))
#print(encode_cesar_gauche_droite("elle oui salam c'est 33",2))
#print(decryptage(encode_miroir("Bonjour radar 33")))
   
def cesar_fi(filename,sens,dec,codage):
    crypted = open(filename.split(".")[0]+"_c.txt",'w')
    if codage =='code':
        file = open(filename,"r")
        for line in file.readlines():
            if sens == 'g':
                current = encode_cesar_gauche_droite(line.strip("\n"),dec)
                crypted.write(current+"\n")
            else :
                encode_cesar_droite_gauche(line.strip("\n"),dec)
                crypted.write(current+"\n")
    else:
        file = open(filename,"r")
        for line in file.readlines():
            decrypted = decryptage(line.strip("\n"))
            crypted.write(decrypted+'\n')
    file.close()
    crypted.close()

#cesar_fi("crypte.txt","g",3,'code')
#cesar_fi("crypte_c.txt","g",3,'decode')

#print(open("crypte.txt","r").readlines())

#print(decode_miroir("&/^^&~./&$33&/.$ &/.$r^^&~a/&dar&/.$ ruojnoB"))

#print(encode_cesar("kayak  sjsjs jsjs","d",4))
#print(decryptage(encode_cesar("kayak  sjsjs jsjs","g",4)))
# %%



# affinee 

def decode_affine(s):
    chaine_code = ""
    liste = s.split("_")
    print(liste)
    decode = liste[0]
    a = int(liste[2])
    b= int(liste[3])
    if pgcd(a,26) != 1:
        print('la valeur de a est invalide')
    else:
            if a==1:
                return encode_cesar_gauche_droite(s,b)
            else:

                for element in decode:
                    if 'A' <= element <= 'Z': 
                        indice = ord(element) - ord('A')
                        indice = ((indice - b)* inverseModulaire(26, a)) % 26
                        chaine_code += chr(indice + ord('A'))
                    elif 'a' <= element <= 'z':
                        indice = ord(element) - ord('a')
                        indice = ((indice - b)* inverseModulaire(26, a)) % 26
                        chaine_code += chr(indice + ord('a'))
                    else :
                       chaine_code += element 



        
    return  chaine_code


def code_affine(s, a, b):
    chaine_codee = ""   
    # cas pgcd 
    while( pgcd(a,26) != 1):
        a=a+1
    if a==1:
        return encode_cesar_droite_gauche(s,b)
    else:     
                
        for element in s:
            if 'A' <= element <= 'Z':    
                indice = ord(element) - ord('A')
                indice = (indice * a + b) % 26
                chaine_codee += chr(indice + ord('A'))
            elif 'a' <= element <= 'z':
                indice = ord(element) - ord('a')
                indice = (indice * a + b) % 26
                chaine_codee += chr(indice + ord('a'))
            else :
                       chaine_codee += element
            chaine_codee = chaine_codee+"_af_"+str(a)+"_"+str(b)
            return  chaine_codee
def pgcd(a,b):
    
    while b!=0:
        r=a%b
        a,b=b,r
    return a


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


def decryptage_affine(data):
    liste = data.split("_")
    Key = liste[1]
    if (Key == '10') and (liste[2] == "d"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair
    if(Key == '10') and (liste[2] == "g"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair

