#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Probabilidad
#Tema: Probabilidad a Priori

#Probabilidad a priori es la probabilidad de que ocurra un evento antes de observar los datos.

import numpy as np

# Supongamos que tienes dos productos: A y B
productos = ['A', 'B']

# Supones que la probabilidad de vender el producto A es 0.7 y la probabilidad de vender el producto B es 0.3
# Estas son tus probabilidades a priori
probabilidades_a_priori = [0.7, 0.3]

# simulamos las ventas de 1000 días
# El resultado es un array de numpy con 1000 elementos, cada uno de los cuales es 'A' o 'B'.
# La probabilidad de que un elemento sea 'A' es 0.7 y la probabilidad de que sea 'B' es 0.3.
ventas = np.random.choice(productos, p=probabilidades_a_priori, size=1000)  

# Contamos las ventas de cada producto
ventas_A = (ventas == 'A').sum()    # Contamos el número de elementos 'A' en el array
ventas_B = (ventas == 'B').sum()    # Contamos el número de elementos 'B' en el array

print(f'Ventas de A: {ventas_A}')   # Imprimimos el número de ventas de A
print(f'Ventas de B: {ventas_B}')   # Imprimimos el número de ventas de B