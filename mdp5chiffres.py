import time
#mdp 5 chiffres
test = '12345'
#calcul tps au début 
start=time.time()

#dic = open("dic5chiffres.txt",'w')

mdp5 = ["0","1","2","3","4","5","6","7","8","9"]

def test(chaine,mot):
      if chaine == mot :
        print("Vous avez trouvé!")
        return True
      else :
        return False
        
def mdp5f(find):
  r=[]
  for l in mdp5:
      chaine = 1
      for l2 in mdp5:
          for l3 in mdp5:
              for l4 in mdp5:
                  for l5 in mdp5:
                      chaine = l+l2+l3+l4+l5
                      if chaine==find :
                          end = time.time()
                          elapsed = end - start
                          r.append(chaine)
                          r.append(f'{elapsed:.3}ms')
                          return r
                        

#calcul tps à la fin
end = time.time()
elapsed = end - start
#print(f'Temps d\'exécution : {elapsed:.2}ms')
