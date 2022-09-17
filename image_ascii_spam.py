# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:17:56 2022

@author: devad
"""

import cv2
import numpy

img1 = cv2.imread('images/wolves.png')
#print(img1[0,0,3])

unity_id = "dayyapp"
ascii_values = [ord(char) for char in unity_id]
print(ascii_values)

height,width,depth = img1.shape
#channels = [0,1,2]
blue_d =0
blue_a =0
blue_y =0
blue_p =0
green_d =0
green_a =0
green_y =0
green_p =0
red_d =0
red_a =0
red_y =0
red_p =0
for h in range(0,height):
    for w in range(0,width):      
         if img1[h,w,0] == 100:
                blue_d = blue_d +1
         if img1[h,w,0] == 97:
                blue_a = blue_a +1
         if img1[h,w,0] == 121:
                blue_y = blue_y +1
         if img1[h,w,0] == 112:
                blue_p = blue_p +1
         if img1[h,w,1] == 100:
               green_d = green_d +1
         if img1[h,w,1] == 97:
               green_a = green_a +1
         if img1[h,w,1] == 121:
               green_y = green_y +1
         if img1[h,w,1] == 112:
               green_p = green_p +1
         if img1[h,w,2] == 100:
               red_d = red_d +1
         if img1[h,w,2] == 97:
               red_a = red_a +1
         if img1[h,w,2] == 121:
               red_y = red_y +1
         if img1[h,w,2] == 112:
               red_p = red_p +1

print(blue_d,blue_a,blue_y,blue_p)
print(green_d,green_a,green_y,green_p)
print(red_d,red_a,red_y,red_p)