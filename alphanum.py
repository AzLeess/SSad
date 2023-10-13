#mdp5 alphanumérique
from distutils.command.build_scripts import first_line_re
import string
import time
string.printable

#calcul tps au début 
start=time.time()

#print(string.printable)

#test = input ("saisissez un mot de passe: ")

def test(chaine,mot):
      if chaine == mot :
        print("Vous avez trouvé!")

def md5a(mdp):
    liste=list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*,-.^_")
    r = []
    i=0
    for l in liste:
        #print ("working on "+str(l))
        chaine = 1
        start=time.time()
        for l2 in liste:
            for l3 in liste:
                for l4 in liste:
                    for l5 in liste:
                        i=i+1
                        chaine = l+l2+l3+l4+l5
                        if mdp == chaine:
                            end = time.time()
                            elapsed = end - start
                            r.append(chaine)
                            r.append(f'{elapsed:.2}ms')
                            return r
#file.write(" il y a "+ str(i)+" instances")

def dic_attack(filename,psw):
    f=open(filename,"r")
    for line in f:
        start=time.time()
        if psw==line.strip("/n") :
            end = time.time()
            elapsed = end - start
            return [line.strip("/n"),elsapsed]
        end = time.time()
        elapsed = end - start
    return ['#####',elapsed]
#print(dic_attack('dic5chiffre.txt','11111'))
#calcul tps à la fin
end = time.time()
elapsed = end - start
#print(f'Temps d\'exécution : {elapsed:.2}ms')
