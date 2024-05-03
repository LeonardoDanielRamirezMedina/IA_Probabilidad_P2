#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Modelos Ocultos de Markov

#Los modelos ocultos de Markov (HMM) son un tipo de modelo estadístico que se utiliza para describir secuencias de observaciones.

import numpy as np

# Estados ocultos: 0 = Durmiendo, 1 = Comiendo, 2 = Jugando
estados = np.array([0, 1, 2])

# Probabilidades iniciales de los estados
prob_iniciales = np.array([0.5, 0.3, 0.2])  # se crea un array con las probabilidades iniciales de los estados

# Matriz de transición de estados 
transicion = np.array([
    [0.6, 0.2, 0.2],  # Probabilidades de transición desde "Durmiendo"
    [0.3, 0.4, 0.3],  # Probabilidades de transición desde "Comiendo"
    [0.2, 0.3, 0.5],  # Probabilidades de transición desde "Jugando"
])

# Matriz de emisión (probabilidades de observar cada observación dado cada estado)
emision = np.array([
    [0.8, 0.2],  # Probabilidades de emisión desde "Durmiendo"
    [0.4, 0.6],  # Probabilidades de emisión desde "Comiendo"
    [0.5, 0.5],  # Probabilidades de emisión desde "Jugando"
])

# Observaciones: 0 = No ronronea, 1 = Ronronea
observaciones = np.array([0, 1, 0, 1, 1, 0])

# Inicializar la matriz de probabilidades con las probabilidades iniciales
probabilidades = prob_iniciales

# Paso hacia delante
for observacion in observaciones:
    # Actualizamos las probabilidades en base a la observación y la matriz de transición
    probabilidades = np.dot(probabilidades, transicion) * emision[:, observacion]
    # Normalizamos las probabilidades para que sumen 1
    probabilidades /= probabilidades.sum()

# Imprimimos las probabilidades finales
print(f"Probabilidades finales: {probabilidades}")

# Predecir el estado del gato
prediccion = np.argmax(probabilidades)  # argmax devuelve el índice del valor máximo
print(f"Predicción del estado del gato: {'Durmiendo' if prediccion == 0 else 'Comiendo' if prediccion == 1 else 'Jugando'}")    