#!/usr/bin/env python
# coding: utf-8

# In[1]:


from stepic import encode 
from eyed3 import load
from PIL import Image
#save our message in the photo and add that photo as a cover to the song
def code_audio(data,img_name,audio):
    #open the song
    audio=load("static/uploads/"+audio)
    # put our text in the photo and save it
    img=Image.open(img_name)
    img_stegano=encode(img,data.encode())
    img_stegano.save(img_name)
    #add the photo as a cover 
    audio.initTag()
    audio.tag.images.remove(u'')
    print(img_name)
    audio.tag.images.set(3,open(img_name,"rb").read(),"image/png")
    audio.tag.save()


# In[ ]:




