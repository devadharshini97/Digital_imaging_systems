# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:17:23 2022

@author: devad
"""
import numpy as np
from collections import OrderedDict
import cv2

img = cv2.imread('images/wolves.png')
cv2.imshow('wolves_display',img)
cv2.waitKey(0)

height,width,channels=img.shape
top=bottom=10
left=right=10
constant=cv2.copyMakeBorder(img,top, bottom, left, right, cv2.BORDER_CONSTANT,value=[0,0,0]) #padding
numpydata = np.asarray(constant)

unity_id = "dayp"
ascii_values = [ord(char) for char in unity_id]
ascii_values_dup=list(OrderedDict.fromkeys(ascii_values))
print(ascii_values_dup)

for c in range(0,3):
  for a in range(0,len(ascii_values_dup)):   
    result = np.where(numpydata[:,:,c] == ascii_values_dup[a])
    x=result[0]
    y=result[1]
    for i in range(0, len(result[0])):
        constant[x[i]-2:x[i]+3,y[i]-2:y[i]+3,c]= [255]  

cropped= constant[top:height+top, left:width+left] #remove padding
cv2.imshow('Cropped Image', cropped) 
cv2.waitKey(0)

"""constant1=cv2.copyMakeBorder(cropped,top, bottom, left, right, cv2.BORDER_CONSTANT,value=[0,0,0])
cv2.imshow('wolves_display',constant1)
cv2.waitKey(0)"""