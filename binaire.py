from pickle import READONLY_BUFFER
import time 

#calcul tps au début 


bina = open("bin3.txt",'w')
dic = ['000','001','010','011',"100",'101','111']
#Mdp 3 lettres

#test = input ("saisissez un mot de passe: ")

def test(chaine,mot):
      if chaine == mot :
        print("Vous avez trouvé!")

def mdp3(mdp):
    mdp3 = ["0","1"]
    r=[]
    start=time.time()
    for l in mdp3:
        for l2 in mdp3:
            for l3 in mdp3:
                chaine = l+l2+l3
                if mdp == chaine :
                    end = time.time()
                    elapsed = end - start
                    r.append(mdp)
                    r.append(f'{elapsed:.8}ms')
                    return r
bina.close()
def dic_attack(dic,psw):
    for line in dic:
        if psw==line.strip("\n"):
            return line
    return '#####'
#print(" this is the pwd "+dic_attack('dic5chiffres.txt','10111'))
start=time.time()
#print(" this is the pwd "+dic_attack('bin3.txt','010'))
#calcul tps à la fin
end = time.time()
elapsed = end - start
#print(f'Temps d\'exécution : {elapsed:.2}ms')




def md5a(mdp):
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