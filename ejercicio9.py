# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:41:10 2020

@author: luna
"""


import numpy as np

def promedio_compras_distintas1500(compra): #función que calcula el promedio
    valor_compra= compra
    compras=0
    while valor_compra!= 0:
        if valor_compra == 1500:
            valor_compra=compra
            print('La compra de 1500 no entra en el promedio')
        else: 
            valor_compra=+ valor_compra
            compras=+1 
            promedio_compras= valor_compra/compras
    return promedio_compras 

compras = np.zeros(5000) #limito a 5000 compras ingresadas

print('Quiere agregar un valor de compra?(si/no)')
respuesta= str.lower(input(''))
while respuesta== 'si':
    for compra in compras:
        compra= float(input('Ingrese valor de compra: '))
        promedio= promedio_compras_distintas1500(compra)
        print(promedio)
        print('Quiere agregar un valor de compra?(si/no)')
        respuesta= str.lower(input(''))


     