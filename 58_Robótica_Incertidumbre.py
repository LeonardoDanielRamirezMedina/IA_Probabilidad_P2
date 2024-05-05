#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: Incertidumbre

# la incertidumbre es una característica fundamental en robótica, ya que los sensores y actuadores de los robots no son perfectos y siempre existe un grado de error en las medidas y acciones realizadas por el robot.

import numpy as np

# Clase del Robot
class Robot:
    def __init__(self, initial_position, measurement_noise, motion_noise):  #initial_position es la posición inicial del robot, measurement_noise es el ruido de la medida y motion_noise es el ruido del movimiento
        self.position = initial_position    #self.position es la posición del robot
        self.measurement_noise = measurement_noise  #self.measurement_noise es el ruido de la medida
        self.motion_noise = motion_noise    #self.motion_noise es el ruido del movimiento

    # Función para mover el robot
    def move(self, distance):
        # Agregar ruido al movimiento del robot
        self.position += distance + np.random.normal(0.0, self.motion_noise)    #self.position es la posición del robot

    # Función para tomar una medida
    def sense(self):
        # Agregar ruido a la medida del sensor
        measured_position = self.position + np.random.normal(0.0, self.measurement_noise)   #measured_position es la posición medida
        return measured_position    #Retorna la posición medida

# Parámetros del robot
initial_position = 0    # posición inicial del robot
measurement_noise = 0.1   # ruido de la medida
motion_noise = 0.1  # ruido del movimiento

# Crear un robot
robot = Robot(initial_position, measurement_noise, motion_noise)

# Simulación de movimiento y medidas del robot
for t in range(10):
    # Movimiento del robot
    robot.move(1)   #mueve el robot
    
    # Medida del sensor
    measured_position = robot.sense()   #measured_position es la posición medida
    
    # Mostrar resultados
    print("Tiempo:", t) #muestra el tiempo
    print("Posición verdadera del robot:", robot.position)  # muestra la posición verdadera del robot
    print("Medida del sensor con incertidumbre:", measured_position)    # muestra la medida del sensor con incertidumbre
    print("==========================")
