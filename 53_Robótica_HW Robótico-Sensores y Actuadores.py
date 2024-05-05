#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Robótica
#Tema: HW Robótico: Sensores y Actuadores

#HW Robótico: Sensores y Actuadores se refiere a la interacción de un robot con su entorno a través de sensores y actuadores. 
#Los sensores son dispositivos que permiten a un robot percibir su entorno, mientras que los actuadores son dispositivos que permiten a un robot interactuar con su entorno. En este código, se muestra cómo leer un sensor y activar un actuador en una placa Arduino utilizando la biblioteca pyfirmata.

from pyfirmata import Arduino, util

# Conectamos a la placa Arduino
board = Arduino('COM3')  # Reemplaza 'COM3' con el puerto correcto

# Configuramos un pin como entrada (sensor) y otro como salida (actuador)
sensor_pin = board.get_pin('d:10:i')  # Pin digital 10 como entrada
actuator_pin = board.get_pin('d:13:o')  # Pin digital 13 como salida

# Creamos un iterador para evitar el desbordamiento del buffer
it = util.Iterator(board)
it.start()

# Leemos el valor del sensor
sensor_value = sensor_pin.read()

# Si el sensor detecta algo activamos el actuador
if sensor_value:
    actuator_pin.write(1)