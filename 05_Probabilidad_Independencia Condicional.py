#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Probabilidad
#Tema: Independencia Condicional

#la independencia condicional es una propiedad importante en la teoría de la probabilidad que se refiere a la relación entre dos eventos.
#Dos eventos son independientes condicionalmente si la ocurrencia de uno no afecta la probabilidad del otro, dado un tercer evento. 

import numpy as np

# Definimos una lista de productos
productos = ['A', 'B']

# Definimos las probabilidades a priori de cada producto
probabilidades_a_priori = [0.5, 0.5]

# Usamos la función np.random.choice para simular las ventas de 1000 días
ventas = np.random.choice(productos, p=probabilidades_a_priori, size=1000)  

# Contamos las ventas de cada producto utilizando la función sum de numpy y la comparación de arrays de numpy
ventas_A = (ventas == 'A').sum()    # Sumamos los elementos de ventas que son iguales a 'A'
ventas_B = (ventas == 'B').sum()    # Sumamos los elementos de ventas que son iguales a 'B'

# Imprimimos el número de ventas de cada producto
print(f'Ventas de A: {ventas_A}')
print(f'Ventas de B: {ventas_B}')


# Calculamos las probabilidades individuales dividiendo el número de ventas de cada producto por el total de ventas 
probabilidad_A = ventas_A / 1000
probabilidad_B = ventas_B / 1000

# Calculamos la probabilidad conjunta multiplicando las probabilidades individuales
probabilidad_conjunta = probabilidad_A * probabilidad_B

# Imprimimos la probabilidad conjunta
print(f'Probabilidad conjunta de A y B: {probabilidad_conjunta:.2f}')   # Redondeamos a dos decimales
