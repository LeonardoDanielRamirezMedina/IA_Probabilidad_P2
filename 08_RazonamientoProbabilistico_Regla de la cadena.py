#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Regla de la Cadena

# La regla de la cadena es un principio fundamental en probabilidad que se utiliza para calcular la probabilidad de varios eventos
# que ocurren en secuencia. En el contexto de las venta

import numpy as np

# lista de productos
productos = ['A', 'B', 'C']

# Estas son tus probabilidades a priori
probabilidades_a_priori = [0.4, 0.3, 0.3]

#simulamos las ventas de 1000 días
ventas = np.random.choice(productos, p=probabilidades_a_priori, size=1000)

# Contamos las ventas de cada producto
ventas_A = (ventas == 'A').sum()    # Contamos cuántas veces se vendió el producto A
ventas_B = (ventas == 'B').sum()    # Contamos cuántas veces se vendió el producto B
ventas_C = (ventas == 'C').sum()    # Contamos cuántas veces se vendió el producto C

# Supongamos que sabemos que las probabilidades condicionales son las siguientes:
# P(B|A) = 0.2, P(C|B) = 0.3
probabilidad_B_dado_A = 0.2   # Probabilidad de que un cliente compre el producto B dado que ya ha comprado el producto A
probabilidad_C_dado_B = 0.3  # Probabilidad de que un cliente compre el producto C dado que ya ha comprado el producto B

# Usamos la regla de la cadena para calcular la probabilidad de que un cliente compre el producto A, luego B y luego C
# La regla de la cadena dice que P(A y B y C) = P(A) * P(B|A) * P(C|B)
probabilidad_A = ventas_A / 1000
probabilidad_A_B_C = probabilidad_A * probabilidad_B_dado_A * probabilidad_C_dado_B  # Regla de la cadena

print(f'Probabilidad de A, luego B, luego C: {probabilidad_A_B_C:.2f}') # Imprimimos la probabilidad de A, luego B, luego C
