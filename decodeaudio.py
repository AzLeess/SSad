#!/usr/bin/env python
# coding: utf-8

# In[2]:


from stepic import decode 
from eyed3 import load
from PIL import Image
from os import system

def decode_audio(audio):
    audio=load(audio)
    #create an img to save the text (text we receive from the cover)
    img=open("temp_img.png","wb")
    print(audio.tag.images)
    img.write(audio.tag.images[0].image_data)
    img.close()
    # we save the text and we delete the img 
    img=Image.open("temp_img.png")
    text=decode(img)
    system("del temp_img.png")
    return text


# In[ ]:




