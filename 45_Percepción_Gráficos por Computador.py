#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Gráficos por Computador

import matplotlib.pyplot as plt # lo utilizamos para crear gráficos

# Eventos y sus probabilidades
eventos = ['Evento A', 'Evento B', 'Evento C', 'Evento D']  
probabilidades = [0.1, 0.3, 0.4, 0.2]   # Probabilidades de los eventos

# Crear gráfico de barras
plt.bar(eventos, probabilidades)    # Creamos gráfico de barras
plt.title('Probabilidad de varios eventos') # Título del gráfico
plt.xlabel('Eventos')   # Etiqueta del eje x
plt.ylabel('Probabilidad')  # Etiqueta del eje y
plt.show()  # Mostrar gráfico