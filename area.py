# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:09:33 2021

@author: Sindhuja Mallappa
"""

import scipy.misc
from PIL import Image
import numpy as np
import random

img=scipy.misc.read('map-01.png')
count_pun=0
count_in=0
count=0

while(count<=10000):
    #In py X & Y values are reversed (x-horizontal y-vertical values)
    x=random.randint(0,2735)
    y=random.randint(0,2480)