import rsa

#pubkey, privkey = rsa.newkeys(1024)


#pub = pubkey.save_pkcs1()
#pubfile.write(pub.decode())
#pubfile.close()
    
#pri = privkey.save_pkcs1()
#prifile.write(pri.decode())
#prifile.close() 
def private(data) :
    prifile = open('private.pem','rb')
    key = prifile.read()
    prifile.close()
    privkey = rsa.PrivateKey.load_pkcs1(key)
    decMessage = rsa.decrypt(data, privkey).decode()
    return decMessage
def public(data):
    pubfile = open('public.pem','rb')
    pub = pubfile.read()
    pubfile.close()
    pubkey = rsa.PublicKey.load_pkcs1(pub)
    message_cry = encMessage = rsa.encrypt(data.encode(),
                         pubkey)
    return message_cry
# this is the string that we will be encrypting
message = "mayopooooooo"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
 
#print(private(public("hello it's me")))