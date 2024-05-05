#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: Generación de Mapas: SLAM

#la generación de mapas es una técnica utilizada en robótica para construir un mapa de un entorno desconocido mientras se localiza el robot en ese entorno.

from robotics import Map, Landmark, Robot   # map es el mapa, Landmark es el punto de referencia y Robot es el robot
import numpy as np
import matplotlib.pyplot as plt

# Crear un mapa con landmarks (puntos de referencia)
landmarks = [Landmark(5, 5), Landmark(10, 5), Landmark(15, 5)]
world_map = Map(landmarks)

# Crear un robot con posición y orientación inicial
robot = Robot(x=0, y=0, heading=np.pi/4)

# Movimientos y mediciones simuladas
movements = [(np.sqrt(2), np.pi/4), (np.sqrt(2), -np.pi/4), (np.sqrt(2), 0)]
measurements = [(4.5, 4.5), (9.5, 4.5), (14.5, 4.5)]

# Actualización del SLAM
for i in range(len(movements)):
    # Movemos el robot y tomar una medida
    robot.move(movements[i][0], movements[i][1])
    robot.measure(world_map)

    # Actualizamos el mapa utilizando la medida
    robot.update_map(world_map, measurements[i])

# Visualizar el mapa y la trayectoria del robot
plt.figure(figsize=(10, 5)) #Tamaño de la figura
world_map.plot()    #Muestra el mapa
robot.plot_trajectory()   #Muestra la trayectoria del robot
plt.legend()    #Muestra la leyenda
plt.grid()  #Muestra la cuadrícula
plt.show()  #Muestra el mapa y la trayectoria del robot
