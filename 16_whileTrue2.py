# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:33:21 2021

@author: DELL
"""

while True:
    x=input("ingrese un numero para contar: ")
    if x =='q' or x== 'quit':
        break 
    x=int(x)
    y=1
    while True:
      print(y)
      y=y+1
      if y>x:
        break