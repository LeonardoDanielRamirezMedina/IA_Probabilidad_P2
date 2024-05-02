#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Manto de Markov


#El manto de Markov es un modelo estocástico que describe una secuencia de eventos donde la probabilidad de que ocurra un evento depende del evento anterior.

import numpy as np  # Importamos la librería NumPy para trabajar con matrices y operaciones matemáticas

# Definimos la matriz de transición del proceso de Markov
#estado 0: hay un 90% de probabilidad de permanecer en el estado 0 y un 10% de probabilidad de pasar al estado 1
#estado 1: hay un 50% de probabilidad de pasar al estado 0 y un 50% de probabilidad de permanecer en el estado 1
matriz_transicion = np.array([
    [0.9, 0.1],  # Probabilidades de transición desde el estado 0
    [0.5, 0.5]   # Probabilidades de transición desde el estado 1
])


# El primer estado en nuestra secuencia de eventos es 0
estado_actual = 0

# Simulamos el proceso de Markov durante 10 pasos
#En las siguientes lineas se simula el proceso de Markov durante 10 pasos, imprimiendo el estado actual en cada paso.
for _ in range(10):
    print(f"Estado actual: {estado_actual}")
    estado_actual = np.random.choice([0, 1], p=matriz_transicion[estado_actual])    # Elegimos el siguiente estado basado en la matriz de transición