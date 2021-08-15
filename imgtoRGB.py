# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:43:56 2021

@author: Sindhuja Mallappa
"""

from PIL import Image
im=Image.open('test1.png') #open the particular image
rgb_im=im.convert('RGB') #conver the img to rgb matrix
#getpixel is a fuc which gets the RGB value from the matrix of a given img
r,g,b=rgb_im.getpixel((1,1)) #storing the 3 values in 3 variables
#change the x & y coordinates 
r,g,b1=rgb_im.getpixel((150,1))
print(r,g,b)#prints the rgb 
print(r,g,b1)