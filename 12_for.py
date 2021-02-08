# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:32:04 2021

@author: DELL
"""
listasw=[]
listasr=[]
listasp=[]
lista=["R1",'R2','R3',
       'S1','S2','S3',
       'R4','R5','PC',
       'Ps5']
for i in lista:
     if 'S' in i:
       listasw.append(i)
     elif 'R' in i:
       listasr.append(i)
     else:
       listasp.append(i)
print ('switches:',listasw,'routers:',listasr,'dispositivos finales:',listasp)
       
     