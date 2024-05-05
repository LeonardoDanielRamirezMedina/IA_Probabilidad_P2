#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Agrupamiento No Supervisado

#El agrupamiento no supervisado es una técnica de aprendizaje automático que se utiliza para identificar grupos de datos similares en un conjunto de datos sin etiquetar.

from sklearn.cluster import KMeans  #se utiliza para implementar el algoritmo K-Means
import numpy as np  
import matplotlib.pyplot as plt #se utiliza para graficar los datos

# Datos de ejemplo
datos = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Creamos un modelo K-Means con dos clusters
kmeans = KMeans(n_clusters=2)

# Ajustamos el modelo a los datos
kmeans.fit(datos)

# Obtenemos las coordenadas de los centros de los clusters
centros = kmeans.cluster_centers_

# Predecimos las etiquetas de los datos
etiquetas = kmeans.labels_

# Graficamos los datos y los centros de los clusters
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas)  #scatter es para graficar puntos
plt.scatter(centros[:, 0], centros[:, 1], c='red')  #centros de los clusters

# Agregamos títulos a la gráfica
plt.title('Agrupamiento K-Means')   #título
plt.xlabel('Característica 1')    #etiqueta eje x
plt.ylabel('Característica 2')  #etiqueta eje y

plt.show()  #mostrar la gráfica