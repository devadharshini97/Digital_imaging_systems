# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:27:27 2022

@author: devad
"""
import cv2
import numpy as np

img = cv2.imread('images/wolves.png')
#img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1= img
img2 = img
#print(img1[0,0,3])

unity_id = "dayyapp"
ascii_values = [ord(char) for char in unity_id]
print(ascii_values)

height,width,depth = img1.shape
channels = [0,1,2]
def cal_occurences():   
    for c in range(0,1):
     blue_d=0
     blue_a=0
     blue_y=0
     blue_p=0
     #sample= np.where(img1==100, blue_d=blue_d +1)
     #print(sample)
     for h in range(0,height):
           for w in range(0,width):   
              if (img1[h,w,c] == 100):
                     blue_d = blue_d +1
                     img2[h-2:h+2,w-2:w+2,c] = [255]
              if (img1[h,w,c] == 97).any():
                     blue_a = blue_a +1
                     img2[h-2:h+2,w-2:w+2,c] = [255]
              if (img1[h,w,c] == 121).any():
                     blue_y = blue_y +1
                     img2[h-2:h+2,w-2:w+2,c] = [255]
              if (img1[h,w,c] == 112).any():
                     blue_p = blue_p +1
                     img2[h-2:h+2,w-2:w+2,c] = [255]
     print(blue_d,2*blue_a,2*blue_y,2*blue_p)
     cv2.imshow('255',img2)  
     cv2.waitKey(0)
       
cal_occurences()


#pixels = list(img1.getdata())
#print(pixels)