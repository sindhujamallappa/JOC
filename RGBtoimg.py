# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:58:38 2021

@author: Sindhuja Mallappa
"""

import numpy as np
from PIL import Image #PIL is a package
width=5
height=4
#constructing an array as image is a matrix(array of pixels)
#an array of zeros, with dimensions(h,w,3-RGB values ie, 3 bits)
#dtype-datatype which is unsigned integers
array=np.zeros([height,width,3],dtype=np.uint8)
#To construct an image a direct fun in py ie, fromarray
#and supply array as a parameter 
img=Image.fromarray(array)
img.save('test.png') 

 
array1=np.zeros([200,200,3],dtype=np.uint8)
#Changed the values of the array1 through list slicing
array1[:,:100]=[255,128,0]#orange-left part
array1[:,100:]=[0,0,255]#blue-right part
img=Image.fromarray(array1)#Create an image
img.save('test1.png')#saved the image