# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:02:26 2022

@author: devad
"""

from PIL import Image
import numpy as np
from collections import OrderedDict

img = Image.open('images/wolves.png')
numpydata = np.asarray(img)
sam= img.copy()

unity_id = "d"
ascii_values = [ord(char) for char in unity_id]
ascii_values_dup=list(OrderedDict.fromkeys(ascii_values))
print(len(ascii_values_dup))

for a in range(0,len(ascii_values_dup)):
  for c in range(0,1):
    result = np.where(numpydata[:,:,c] == ascii_values_dup[a])
    print(len(result[0]), end=" ")
    x=result[0]
    y=result[1]
    for i in range(0, len(result[0])):
        sam[x[i]-2:x[i]+2,y[i]-2:y[i]+2,c]= [255]
    
  print(end="\n")

  
sam.show()