#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema:Filtrado, Predicción, Suavizado y Explicación

#este tema se aplica para predecir el estado de un sistema en el futuro, dado un conjunto de observaciones pasadas.

import numpy as np

# Estados del tiempo: 0 = No lluvia, 1 = Lluvia
estados = np.array([0, 1])

# Probabilidades iniciales de los estados
prob_iniciales = np.array([0.5, 0.5])

# Matriz de transición de estados (probabilidades de pasar de un estado a otro)
transicion = np.array([
    [0.7, 0.3],  # Probabilidades de transición desde "No lluvia"
    [0.3, 0.7],  # Probabilidades de transición desde "Lluvia"
])

# Observaciones: 0 = No lluvia, 1 = Lluvia
observaciones = np.array([0, 1, 0, 0, 1, 1, 0])

# se inicializa la matriz de probabilidades con las probabilidades iniciales
probabilidades = prob_iniciales

# Realizar el filtrado
for observacion in observaciones:
    # se actualizan las probabilidades en base a la observación y la matriz de transición
    probabilidades = transicion[observacion] * probabilidades
    # se normalizan las probabilidades para que sumen 1
    probabilidades /= probabilidades.sum()

# se imprimen las probabilidades finales
print(f"Probabilidades finales: {probabilidades}")

# se predice el estado del tiempo para el próximo día
prediccion = np.argmax(probabilidades)  # argmax devuelve el índice del valor máximo
print(f"Predicción para el próximo día: {'Lluvia' if prediccion else 'No lluvia'}") # Se imprime el resultado
