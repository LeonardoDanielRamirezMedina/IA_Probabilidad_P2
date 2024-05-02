#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Probabilidad
#Tema: Regla de Bayes

# La regla de Bayes es una fórmula que describe cómo actualizar las creencias sobre la probabilidad de un evento dado la evidencia observada 

import numpy as np

#lista de productos
productos = ['A', 'B']


# Estas son tus probabilidades a priori
probabilidades_a_priori = [0.5, 0.5]

#simulamos las ventas de 1000 días
ventas = np.random.choice(productos, p=probabilidades_a_priori, size=1000)

# Contamos las ventas de cada producto
ventas_A = (ventas == 'A').sum()
ventas_B = (ventas == 'B').sum()


# Esta es tu probabilidad condicionada, es decir, la probabilidad de que un cliente compre el producto B dado que ya ha comprado el producto A
probabilidad_B_dado_A = 0.1

# Calculamos la probabilidad de que un cliente compre el producto A y el producto B
probabilidad_A = ventas_A / 1000
probabilidad_B = ventas_B / 1000
probabilidad_A_dado_B = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B   # Regla de Bayes

# Imprimimos la probabilidad de A dado B con la fórmula de la regla de Bayes
print(f'Probabilidad de A dado B (calculada con la regla de Bayes): P(A|B) = P(B|A) * P(A) / P(B) = {probabilidad_B_dado_A} * {probabilidad_A} / {probabilidad_B} = {probabilidad_A_dado_B:.2f}')