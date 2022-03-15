#PYTHON code 
#FILE NAME : main.py
#DESCRIPTION :  code that get the number and location of faces in a photo 
#Required libs  : face_recognition PIL os numpy Click scipy Pillow
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#* : If you are  bitch  change the rights  
#2022/3/15


import face_recognition as fa
from PIL import Image, ImageDraw
import os,numpy


XXXXXX = input("Enter the path of the image like(image1.jpg) : ")
if(os.path.exists(XXXXXX) == False) : exit(XXXXXX+'Image Not Exists')
imagepath = fa.load_image_file(XXXXXX)
imagelo = fa.face_locations(imagepath)

PIL = Image.fromarray(imagepath)
rasm = ImageDraw.Draw(PIL)
for akil in imagelo:   
    rasm.rectangle(((akil[3], akil[0]), (akil[1], akil[2])), outline=(255, 0, 0))
    text_width, text_height = rasm.textsize('BY @FFFFFFM')
    rasm.rectangle(((akil[3], akil[2] - text_height - 10), (akil[1], akil[2])), fill=(255, 0, 0), outline=(255, 0, 255))
    rasm.text((akil[3] , akil[2] - text_height - 5), 'BY @FFFFFFM', fill=(255, 255, 255, 255))
    
rasm.text((40, 40), 'The number of faces in the photo  '+str(len(imagelo)), align ="left")    
del rasm
PIL.save('akil.png')
print('I saved the image to akil.png ')

#PYTHON code 
#FILE NAME : main.py
#DESCRIPTION : A code that get the number and location of faces in a photo 
#Required libs  : face_recognition PIL os numpy Click scipy Pillow
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#* : If you are  bitch  change the rights  
#2022/3/15
