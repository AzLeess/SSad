def encode_decalage(s, op, n):
    if op == 'g':
        mots = s.split(' ')
        i=0
        chaine_codee =''
        while i<= len(mots)-1:
            mot = mots[i]
            if((n % len(mot))== 0):
                s = mot[(n%len(mot)):] + mot[:(n%len(mot))]
                s = '$./&' + s + '&/'
                s = s[0:6]+'$./&'+ s[6:len(s)]
                chaine_codee = chaine_codee + s + ' '
                i=i+1
            else:
                s = mot[(n%len(mot)):] + mot[:(n%len(mot))]
                chaine_codee = chaine_codee + s + ' '
                i=i+1      
        chaine_codee = str.rstrip(chaine_codee)
        chaine_codee=chaine_codee+"_10_"+str(op)+'_'+str(n)
        return chaine_codee
    elif op == 'd':
        mots = s.split(' ')
        i=0
        chaine_codee =''
        while i<= len(mots)-1:
            mot = mots[i]
            if((n % len(mot))== 0):
                s = mot[(-(n%len(mot))):] + mot[:(-(n%len(mot)))]
                s = '$./&' + s + '&/'
                s=s[0:6]+'$./&'+s[6:len(s)]
                chaine_codee = chaine_codee + s + ' '
                i=i+1
            else:
                s = mot[(-(n%len(mot))):] + mot[:(-(n%len(mot)))]
                chaine_codee = chaine_codee + s + ' '
                i=i+1      
        chaine_codee = str.rstrip(chaine_codee)
        chaine_codee=chaine_codee+"_10_"+str(op)+'_'+str(n)
        return chaine_codee
    else:
        print('Invalid operation')
            
def decode_decalage(s, op, n):
    s=s.replace('$./&','')
    s=s.replace('&/','')
    if op == 'g':
        mots = s.split(' ')
        i=0
        chaine_claire =''
        while i<= len(mots)-1:
            mot = mots[i]
            s = mot[(-(n%len(mot))):] + mot[:(-(n%len(mot)))]
            chaine_claire = chaine_claire + s + ' '
            i=i+1      
        chaine_clare = str.rstrip(chaine_claire)
        return chaine_claire  
    elif op == 'd':
        mots = s.split(' ')
        i=0
        chaine_claire =''
        while i<= len(mots)-1:
            mot = mots[i]
            s = mot[(n%len(mot)):] + mot[:(n%len(mot))]
            chaine_claire = chaine_claire + s + ' '
            i=i+1      
        chaine_clare = str.rstrip(chaine_claire)
        return chaine_claire  
    else:
        print('Invalid operation')
        
        
def decryptage(data):
    liste = data.split("_")
    Key = liste[1]
    if (Key == '10') and (liste[2] == "d"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair
    if(Key == '10') and (liste[2] == "g"):
        message_clair = decode_decalage(liste[0],liste[2],int(liste[3]))
        return message_clair
            
                
#print(decode_decalage('$./&ab$./&c&/ $./&ab$./&c&/ lutsa','right',3))
#print(encode_decalage('sjksj sjjjs','right',14))
#print(decryptage('jksjs jjjss_10_right_14'))

#print(encode_decalage('hey rayane hi shinji ssad','left',21))


#print(decryptage('$./&he$./&y&/ aneray ih njishi sads_10_left_21'))
