#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: Localización: Monte-Carlo

# Monte-Carlo Localization se basa en la idea de que podemos estimar la posición de un robot utilizando un conjunto de partículas. Cada partícula representa una posible posición del robot. 
#En cada paso de tiempo, actualizamos la posición de las partículas basándonos en las mediciones del robot y en el movimiento esperado. Las partículas que mejor se ajustan a las mediciones y al movimiento esperado se mantienen, mientras que las partículas que no se ajustan bien se eliminan. Al final, la posición del robot se estima como el promedio de las posiciones de las partículas restantes.

import numpy as np

# Definir la función de probabilidad
def likelihood(map, particle, measurement):
    # Calcular la medición esperada dada la posición
    expected_measurement = map[particle]

    # Calcular la probabilidad de la medición dada la medición esperada
    # Usamos una distribución gaussiana para modelar el error de medición
    probability = np.exp(-0.5 * (measurement - expected_measurement)**2)

    return probability

# Definir la función de localización de Monte Carlo
def monte_carlo_localization(map, measurements, N=1000):    #monte_carlo_localization es la función que se encarga de realizar la localización de Monte Carlo
    particles = np.random.choice(len(map), N)   #particles es una variable que se encarga de generar un número aleatorio de partículas
    weights = np.ones(N) / N    #weights es una variable que se encarga de generar un peso aleatorio

    for measurement in measurements:    #measurement es una variable que se encarga de realizar la medición
        weights *= np.array([likelihood(map, particle, measurement) for particle in particles]) 
        weights /= np.sum(weights)
        particles = np.random.choice(particles, N, p=weights)   

    return particles    #Regresa las partículas