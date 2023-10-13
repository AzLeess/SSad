from stepic import decode 
from eyed3 import load
from PIL import Image
from os import system

def decode(audio):
    audio=load(audio)

    img=open("temp_img.png","wb")
    img.write(audio.tag.images[0].image_data)
    img.close()

    img=Image.open("temp_img.png")
    text=decode(img)
    system("del temp_img.png")
    return str(text)

