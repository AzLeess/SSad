from stepic import encode 
from eyed3 import load
from PIL import Image 

def code (data,img_name,audio):
    audio=load(audio)
    
    img=Image.open(img_name)
    img_stegano=encode(img,data.encode()) 
    img_stegano.save(img_name)
    if not audio.tag :
        audio.initTag()
    audio.tag.images.set(3,open(img_name,"rb").read(),"image/png")
    audio.tag.save()
    audio.close()
    return True
