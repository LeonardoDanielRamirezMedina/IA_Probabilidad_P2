#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Modelos Ocultos de Markov

#Los modelos ocultos de Markov (HMM) son un tipo de modelo estadístico que se utiliza para describir secuencias de observaciones.

import numpy as np

# Inicializamos el estado inicial del vehículo
posicion_inicial = 0  
velocidad_inicial = 70  
estado_inicial = np.array([posicion_inicial, velocidad_inicial])    # Se crea un array con la posición y la velocidad inicial

# Inicializamos la matriz de estado
A = np.array([[1, 1], [0, 1]])  # El arreglo contiene la posición y la velocidad

# Inicializamos la matriz de observación
H = np.array([[1, 0]])  # Solo podemos observar la posición

# Inicializamos el ruido del proceso
Q = np.array([[1, 0.1], [0.1, 1]])  # El ruido del proceso es la covarianza de la posición y la velocidad

# Inicializamos el ruido de la observación
R = np.array([[10]])    # El ruido de la observación es la covarianza de la posición

# Inicializamos el error de la estimación
P = np.array([[10, 0], [0, 10]])    # El error de la estimación es la covarianza de la posición y la velocidad

# Generamos algunas observaciones ruidosas de la posición del vehículo
observaciones = np.arange(0, 100, 10) + np.random.normal(0, 10, size=10)

# Inicializamos el estado estimado y el error de la estimación
estado_estimado = estado_inicial
P_estimado = P  # Se inicializa el estado estimado y el error de la estimación

# Aplicamos el Filtro de Kalman, que se usa para estimar el estado de un sistema lineal a partir de observaciones ruidosas
for observacion in observaciones:
    # Predicción
    estado_predicho = np.dot(A, estado_estimado)    #.dot es el producto de matrices
    P_predicho = np.dot(A, np.dot(P_estimado, A.T)) + Q   #.T es la transpuesta de la matriz

    # Actualización
    y = observacion - np.dot(H, estado_predicho)    # Se calcula la diferencia entre la observación y la predicción
    S = np.dot(H, np.dot(P_predicho, H.T)) + R  # Se calcula la covarianza de la observación
    K = np.dot(P_predicho, H.T) / S # Se calcula la ganancia de Kalman
    estado_estimado = estado_predicho + K * y   # Se actualiza el estado estimado
    P_estimado = P_predicho - np.dot(K, np.dot(H, P_predicho))  # Se actualiza el error de la estimación

    # Imprimimos el estado estimado
    print(f"Posición estimada: {estado_estimado[0]}, Velocidad estimada: {estado_estimado[1]}")