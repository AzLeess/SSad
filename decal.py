
#lire = open('crypte.txt','r')
#fichier_dec = open("crypte1.txt",'w')

file =[]
#for line in lire :
#    file.append(line)

#txt = "".join(file)
#print(txt)

def hasRepeatedChars(s):
    for i in range(len(s)):
        if i != s.rfind(s[i]):
            return True
    return False

def encode_decalage(s, op, n):
    l1=[]
    if hasRepeatedChars(s):
        l1=list(s)
        for i in range(1,len(l1)-1) :
            spec = l1[i]
            spec_2=spec[0:7]+'&/'+spec[7:12]+ '~&^^' +spec[12:len(spec)]
            l1[i]=spec_2
            
        s=''.join(l1)
    if op == 'g':
        chaine_codee=s[n:] + s[:n]
        chaine_codee=chaine_codee+"_10_"+str(op)+'_'+str(n)
        return chaine_codee
    elif op == 'd':
        chaine_codee=s[-n:] + s[:-n]
        chaine_codee=chaine_codee+"_10_"+str(op)+ '_'+str(n)
        return chaine_codee
    else:
            print('Invalid operation')
    
    


def decode_decalage(s, op, n):
    s = s.replace('&/', '')
    s = s.replace('~&^^', '')
    s = s.replace('/', '')
    s = s.replace('&', '')
    s = s.replace('^', '')
    s = s.replace('~', '')
    if op == 'g':
        code_claire=s[-n:] + s[:-n]
        return code_claire
    elif op == 'd':
        code_claire=s[n:] + s[:n]
        return code_claire
    else:
        print('Invalid operation')


def decryptage_decode(data):
    liste = data.split("_")
    print(liste)
    Key = liste[1]
    if (Key == '10') and (liste[2] == "d"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair
    if(Key == '10') and (liste[2] == "g"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair




chs = ''' alors maya n'est pas sympa 
        et puis elle est tetue'''
#deco = encode_decalage(txt,'d',4)
#print(encode_decalage(txt,'d',4))
#print(decode_decalage('dbo&/~&^^n&/~&^^j&/~&^^o&/~&^^u&/~&^^r&/~&^^ &/~&^^d&/~&^^h&/~&^^d&/~&^^d&/~&^^h&/~&^^ &/~&^^s&/~&^^a&/~&^^l&/~&^^u&/~&^^t&/~&^^ &/~&^^s&/~&^^a&/~&^^l&/~&^^a&/~&^^m&/~&^^ &/~&^^c&/~&^^a&/~&^^v&/~&^^a&/~&^^ &/~&^^?&/~&^^ &/~&^^e&/~&^^t&/~&^^ &/~&^^t&/~&^^o&/~&^^i&/~&^^ &/~&^^h&/~&^^m&/~&^^l&/~&^^_10_d_1','d',1))
#print(decryptage("rbnjou_10_d_1"))

#print(encode_decalage('hi ddd','g',4))
#print(decryptage_decode(encode_decalage('hi ddd','g',-4)))
#print(decryptage(deco))
#l = deco.split("/n")
#for i in l :
#    fichier_dec.write(i)


#fichier_dec.close()
#lire.close()

                      

