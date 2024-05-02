#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Probabilidad
#Tema: Probabilidad Condicionada y Normalización

#La probabilidad condicionada es una probabilidad que se calcula cuando ya se conoce cierta información adicional.
#la normalización es un proceso que se utiliza para ajustar los valores de una distribución de probabilidad para que sumen 1.

import numpy as np  # Importamos numpy

#lista que contiene los productos
productos = ['A', 'B']


#probabilidades a priori que son las probabilidades de que un cliente compre cada producto
probabilidades_a_priori = [0.7, 0.3]

#se generan 1000 ventas aleatorias de productos
ventas = np.random.choice(productos, p=probabilidades_a_priori, size=1000)

# Contamos las ventas de cada producto
ventas_A = (ventas == 'A').sum()    # Contamos las ventas de A
ventas_B = (ventas == 'B').sum()    # Contamos las ventas de B


#probabilidad condicionada de que un cliente que compra A también compre B
probabilidad_condicionada = 0.1


ventas_A_y_B = ventas_A * probabilidad_condicionada # Calculamos el número esperado de clientes que compran A y B

# Normalizar es dividir cada valor por la suma de todos los valores
# Normalizamos las ventas para que sumen 1
ventas_totales = ventas_A + ventas_B    # Calculamos el número total de ventas
ventas_A_normalizadas = ventas_A / ventas_totales   # Normalizamos las ventas de A
ventas_B_normalizadas = ventas_B / ventas_totales   # Normalizamos las ventas de B

print(f'Ventas de A: {ventas_A}, Ventas normalizadas de A: {ventas_A_normalizadas:.2f}')    # Imprimimos las ventas de A y las ventas normalizadas de A
print(f'Ventas de B: {ventas_B}, Ventas normalizadas de B: {ventas_B_normalizadas:.2f}')    # Imprimimos las ventas de B y las ventas normalizadas de B
print(f'Ventas de A y B: {ventas_A_y_B}')   # Imprimimos las ventas de A y B