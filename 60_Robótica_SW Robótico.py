#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: SW Robótico

# En robótica, un robot de software (SW) es un robot que existe únicamente en un entorno de simulación o en un entorno virtual.
 
import numpy as np

# Definir la función de movimiento del robot
def move_robot(position):
    # El robot se mueve aleatoriamente hacia adelante o hacia atrás
    new_position = position + np.random.choice([-1, 1]) #choice elige un valor aleatorio de la lista [-1, 1]
    return new_position

# Definir la función de medida del sensor
def sense_wall(position, wall_position, measurement_noise):
    # El sensor devuelve True si el robot está cerca de la pared y False en caso contrario
    distance = abs(position - wall_position)    #en esta linea se calcula la distancia entre la posición del robot y la pared
    measured_distance = distance + np.random.normal(0.0, measurement_noise)     #se agrega ruido a la medida del sensor
    return measured_distance < 1.0  #retorna True si el robot está cerca de la pared y False en caso contrario

# Parámetros del mundo y del robot
wall_position = 10  # Posición de la pared
initial_position = 0    # Posición inicial del robot
measurement_noise = 0.5 # Ruido de la medida

# Simulación
robot_position = initial_position
for t in range(10):
    # Movimiento del robot
    robot_position = move_robot(robot_position)   #mueve el robot
    
    # Medida del sensor
    is_near_wall = sense_wall(robot_position, wall_position, measurement_noise)  #is_near_wall es True si el robot está cerca de la pared y False en caso contrario
    
    # Mostrar resultados
    print(f"Tiempo {t}: Posición del robot: {robot_position}, ¿Está cerca de la pared?: {is_near_wall}")    #muestra la posición del robot y si está cerca de la pared
