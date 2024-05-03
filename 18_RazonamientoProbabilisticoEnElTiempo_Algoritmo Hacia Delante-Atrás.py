#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema:Algoritmo Hacia Delante-Atrás

# Este algoritmo se utiliza para calcular la probabilidad de un estado oculto en un modelo oculto de Markov

import numpy as np

# Estados: 0 = Sano, 1 = Enfermo
estados = np.array([0, 1])

# Probabilidades iniciales de los estados
prob_iniciales = np.array([0.6, 0.4])

# Matriz de transición de estados 
transicion = np.array([
    [0.7, 0.3],  # Probabilidades de transición desde "Sano"
    [0.4, 0.6],  # Probabilidades de transición desde "Enfermo"
])

# Matriz de emisión (probabilidades de observar cada síntoma dado cada estado)
emision = np.array([
    [0.5, 0.5],  # Probabilidades de emisión desde "Sano"
    [0.1, 0.9],  # Probabilidades de emisión desde "Enfermo"
])

# Observaciones: 0 = Sin síntomas, 1 = Con síntomas
observaciones = np.array([0, 1, 0, 1, 1, 0])

# Se inicializa la matriz de probabilidades con las probabilidades iniciales
probabilidades = prob_iniciales


for observacion in observaciones:
    # se actualizan las probabilidades en base a la observación y la matriz de transición
    probabilidades = np.dot(probabilidades, transicion) * emision[:, observacion]
    # Normalizamos las probabilidades para que sumen 1
    probabilidades /= probabilidades.sum()

# Paso hacia atrás
probabilidades_finales = probabilidades
for observacion in observaciones[::-1]:
    # Actualizamois las probabilidades en base a la observación y la matriz de transición
    probabilidades = np.dot(probabilidades, transicion.T) * emision[:, observacion]
    # Normalizamos las probabilidades para que sumen 1
    probabilidades /= probabilidades.sum()

# Imprimimos las probabilidades finales
print(f"Probabilidades finales: {probabilidades_finales}")

# Predecimos el estado de la enfermedad
prediccion = np.argmax(probabilidades_finales)  # argmax devuelve el índice del valor máximo
print(f"Predicción del estado de la enfermedad: {'Enfermo' if prediccion else 'Sano'}") # Se imprime el resultado