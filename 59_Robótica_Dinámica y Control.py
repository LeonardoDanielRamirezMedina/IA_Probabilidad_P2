#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: Dinámica y Control

# La dinámica se refiere al estudio de las fuerzas y movimientos de los robots, mientras que el control se refiere a la aplicación de algoritmos para guiar el comportamiento de los robots.

import numpy as np
import matplotlib.pyplot as plt # se importa la librería matplotlib para visualizar la trayectoria del robot

# Clase del Robot
class Robot:
    def __init__(self, initial_position):   #initial_position es la posición inicial del robot
        self.position = initial_position    #self.position es la posición del robot
        self.velocity = 0.0    #self.velocity es la velocidad del robot

    # Función para actualizar la posición del robot
    def update_position(self, dt):  #dt es el paso de tiempo
        self.position += self.velocity * dt 

# Parámetros del robot
initial_position = 0.0  # Posición inicial del robot en el eje x

# Crear el robot
robot = Robot(initial_position)

# Parámetros de control
k_p = 0.5  # Ganancia proporcional

# Posición deseada del robot
target_position = 3.0  # Posición deseada en el eje x

# Simulación de control
dt = 0.1  # Paso de tiempo
total_time = 10.0  # Tiempo total de simulación
num_steps = int(total_time / dt)

# Listas para almacenar la trayectoria del robot
x_trajectory = [robot.position]

# Simulación de control proporcional
for _ in range(num_steps):
    # Calcular el error de posición
    error = target_position - robot.position
    # Aplicar control proporcional
    control = k_p * error
    # Establecer la velocidad del robot
    robot.velocity = control
    # Actualizar la posición del robot
    robot.update_position(dt)
    # Almacenar la posición actual del robot
    x_trajectory.append(robot.position)

# Visualización de la trayectoria del robot
plt.plot(x_trajectory, label='Trayectoria del robot')   #muestra la trayectoria del robot
plt.axhline(target_position, color='r', linestyle='--', label='Posición deseada')   #muestra la posición deseada
plt.xlabel('Tiempo')    #muestra el tiempo  
plt.ylabel('Posición (eje x)')  #muestra la posición en el eje x
plt.title('Control Proporcional de Robot Móvil')    #muestra el título
plt.legend()        #muestra la leyenda
plt.grid()  #muestra la cuadrícula
plt.show()  #muestra la gráfica
