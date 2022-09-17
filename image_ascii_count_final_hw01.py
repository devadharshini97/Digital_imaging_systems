# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:14:46 2022

@author: devad
"""

#from PIL import Image
import numpy as np
from collections import OrderedDict
import cv2

img = cv2.imread('images/wolves.png')
numpydata = np.asarray(img)
img_copy= img.copy()

unity_id = "dayyapp"
ascii_values = [ord(char) for char in unity_id]
ascii_values_dup=list(OrderedDict.fromkeys(ascii_values))
print(len(ascii_values_dup))

for a in range(0,len(ascii_values_dup)):
  for c in range(2,-1,-1):
    result = np.where(numpydata[:,:,c] == ascii_values_dup[a])
    print(len(result[0]), end=" ")
    x=result[0]
    y=result[1]
    for i in range(0, len(result[0])):
        img_copy[x[i]-2:x[i]+3,y[i]-2:y[i]+3,c]= [255]
  print(end="\n")

  
cv2.imshow('wolves_display',img_copy)
cv2.waitKey(0)