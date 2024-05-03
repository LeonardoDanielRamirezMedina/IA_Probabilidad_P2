#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Procesos Estacionarios

#Los procesos estacionarios son aquellos que no cambian con el tiempo. se utilizan para modelar señales aleatorias que no cambian con el tiempo.

import numpy as np
import matplotlib.pyplot as plt #utilizamos la librería matplotlib para graficar

#proceso estacionario con una media de 0 y una varianza de 1
media = 0
varianza = 1
muestras = np.random.normal(media, np.sqrt(varianza), 1000) #se generan 1000 muestras de una distribución normal

media_muestras = np.mean(muestras)  #mean se utiliza para calcular la media de las muestras
varianza_muestras = np.var(muestras)    #var se utiliza para calcular la varianza de las muestras

print(f'Media de las muestras: {media_muestras:.2f}')   #se imprime la media de las muestras
print(f'Varianza de las muestras: {varianza_muestras:.2f}') #se imprime la varianza de las muestras

plt.plot(muestras)      #se grafican las muestras
plt.title('Proceso estacionario')   #se coloca un título a la gráfica
plt.xlabel('Tiempo')    #se coloca un título al eje x
plt.ylabel('Valor')    #se coloca un título al eje y
plt.show()  #se muestra la gráfica

#la grafica muestra que las muestras no cambian con el tiempo, lo que indica que es un proceso estacionario