#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Red Bayes. Dinámica: Filtrado de Partículas

# El tema Red Bayes. Dinámica: Filtrado de Partículas se utiliza para estimar la posición de un robot en un entorno desconocido utilizando un conjunto de partículas.

import numpy as np

# Parámetros del problema
num_particulas = 1000  # Número de partículas
num_pasos = 50  # Número de pasos de tiempo
ruido_movimiento = 0.1  # Ruido en el movimiento del robot
ruido_medida = 0.5  # Ruido en las medidas del robot

# Inicializar las partículas
particulas = np.random.rand(num_particulas, 2) # Se crean partículas aleatorias en un espacio de 2 dimensiones

# Puntos de referencia
puntos_referencia = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Se crean 4 puntos de referencia

# Función para medir la distancia a los puntos de referencia
def medir_distancia(pos, puntos_referencia):    # Se crea una función para medir la distancia a los puntos de referencia
    return np.sqrt(((pos - puntos_referencia)**2).sum(axis=1))  # Se calcula la distancia euclidiana entre la posición y los puntos de referencia

# Simular el movimiento y las medidas del robot
pos_real = np.array([0.5, 0.5]) # Se inicializa la posición real del robot
for paso in range(num_pasos):   # Se simula el movimiento y las medidas del robot

    pos_real += np.random.normal(0, ruido_movimiento, size=2)   # Se simula el movimiento del robot

    # Medimos la distancia a los puntos de referencia
    medidas_real = medir_distancia(pos_real, puntos_referencia) + np.random.normal(0, ruido_medida, size=4) 

    # Movemos las partículas
    particulas += np.random.normal(0, ruido_movimiento, size=(num_particulas, 2))   #normal se utiliza para generar números aleatorios con una distribución normal

    # Pesar las partículas
    medidas_particulas = np.array([medir_distancia(p, puntos_referencia) for p in particulas])  # Se miden las distancias a los puntos de referencia
    pesos = np.exp(-0.5 * ((medidas_particulas - medidas_real)**2).sum(axis=1) / ruido_medida**2)   # Se calculan los pesos de las partículas
    pesos /= pesos.sum()    # Se normalizan los pesos

    # Resamplear las partículas
    indices = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos) # Se resamplean las partículas, es decir, se seleccionan las partículas con reemplazo
    particulas = particulas[indices]    # Se actualizan las partículas

# Estimar la posición del robot
estimacion = particulas.mean(axis=0)    #.mean se utiliza para calcular la media de las partículas
print(f"Posición real: {pos_real}, Estimación: {estimacion}")   # Se imprime la posición real y la estimación del robot