#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: Cinemática Inversa

# la cinemática inversa es el proceso de determinar las posiciones de las articulaciones de un robot a partir de una posición deseada del extremo del robot.

import numpy as np

# Función de cinemática inversa para un brazo robótico de 2DOF
def inverse_kinematics(x, y, l1, l2):
    # Calcular la distancia al extremo del brazo
    d = np.sqrt(x**2 + y**2)    #d es la distancia al extremo del brazo
    
    # Calcular el ángulo de la primera articulación (theta1)
    theta1 = np.arctan2(y, x) - np.arccos((l1**2 + d**2 - l2**2) / (2 * l1 * d))        #theta1 es el ángulo de la primera articulación
    
    # Calcular el ángulo de la segunda articulación (theta2)
    alpha = np.arccos((l1**2 + l2**2 - d**2) / (2 * l1 * l2))   #alpha es el ángulo de la segunda articulación
    theta2 = np.pi - alpha  #theta2 es el ángulo de la segunda articulación
    
    return theta1, theta2

# Posición deseada del extremo del brazo
target_x = 4    #target_x es la posición deseada del extremo del brazo
target_y = 2    

# Longitudes de los eslabones del brazo
l1 = 3  #l1 es la longitud del eslabón 1
l2 = 2      #l2 es la longitud del eslabón 2

# Calcular la cinemática inversa
theta1, theta2 = inverse_kinematics(target_x, target_y, l1, l2) #inverse_kinematics es la función que se encarga de calcular la cinemática inversa

# Mostrar resultados
print("Ángulo de la articulación 1 (theta1):", np.degrees(theta1))  #np.degrees convierte el ángulo de radianes a grados
print("Ángulo de la articulación 2 (theta2):", np.degrees(theta2))  
