# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:53:56 2021

@author: DELL
"""

acl=int(input("Ingrese el # del ACL"))
if acl>=1 and acl<=99:
    print("es un ACL estandar")
elif acl>=100 and acl <=199:
    print("es un ACL extendida")
else: 
    print("No es # de ACL válido")
    