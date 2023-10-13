import re
from numpy import asarray
from PIL import Image

def hide(msg,image_name,dirct):
    image = Image.open(image_name)
    data = asarray(image).copy()
    print ( " pixel originale " + str(data[0][0]))
    #convertir le message en octet
    final_mes=""
    for lettre in msg:
        position_ascii = ord(lettre)
        binaire = bin(position_ascii)[2:]
        while len(binaire)<8 :
            binaire = "0" +binaire
        final_mes += binaire
        #Recupere la longueur et l'inscrit sur 2 octet
        longueur = len(final_mes)
        binaire= bin(longueur)[2:]
        while len(binaire)<16:
            binaire="0"+ binaire
    result_mes = binaire + final_mes

    # data [y][x][rgb]
    y=0
    tour=0
    for line in data :
        x=0
        for colonne in line :
            rgb=0
            for couleur in colonne:
                valeur=data[y][x][rgb]
                binaire=bin(valeur) [2:]
                binair_list = list(binaire)
                del binair_list[-1]
                binair_list.append(result_mes[tour])
                decimal = int("".join(binair_list),2)
                data[y][x][rgb]=decimal
                rgb +=1
                tour +=1
                if tour >= len(result_mes):
                    break
            x+=1
            if tour >= len(result_mes):
                break
        y+=1
        if tour >= len(result_mes):
            break
    print("pixel apres inscirption du message"+str(data[0][0]))
    imagefinal = Image.fromarray(data)
    print(image_name)
    img1 = image_name.split("/")[1]
    nm = dirct+ img1.split(".")[0]+ "_SERCRET.png"
    imagefinal.save(nm)
def discover (image_name):
    image = Image.open(image_name)
    data = asarray(image).copy()

    y=0
    taille=""
    message=""
    tour=0
    taille_new=112
    for line in data :
        x=0
        for colonne in line:
            rgb=0
            for color in colonne:
                valeur = data[y][x][rgb]
                binaire=bin(valeur)[2:]
                last = binaire[-1]
                if tour <16 :
                    taille+=last
                if tour==16:
                    taille_new= int(taille,2)
                if tour-16 <taille_new:
                    message+=last
                if tour-16>= taille_new:
                    break
                tour+=1
                rgb+=1
            if tour-16 >= taille_new :
                break
            x+=1
        if tour-16 >= taille_new :
             break
    y+=1
    octet=[]
    for i in range(len(message)//8):
        octet.append(message[i*8:(i+1)*8])
   
    result=""
    for oct in octet:
        index=int(oct,2)
        lettre_ascii=chr(index)
        #print(lettre_ascii)
        result+=lettre_ascii
    return str(result)[2:]


