#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Algoritmo EM

#El algoritmo EM (Expectation-Maximization) es un algoritmo de optimización que se utiliza para encontrar los parámetros de un modelo estadístico en presencia de datos faltantes o variables latentes.

from sklearn.mixture import GaussianMixture #se utiliza para ajustar un modelo de mezcla gaussiana a los datos
import numpy as np  #se utiliza para realizar operaciones matemáticas

# Datos de alturas y pesos de personas
datos = np.array([
    [170, 70],
    [160, 60],
    [180, 80],
    [150, 50],
    [175, 75],
    [165, 65]
])

# Creamos un modelo de mezcla gaussiana con dos componentes para representar dos grupos
gmm = GaussianMixture(n_components=2)   

# Ajustamos el modelo a los datos usando el algoritmo EM
gmm.fit(datos)

# Predecimos las etiquetas de los datos
etiquetas = gmm.predict(datos)

# Imprimimos las etiquetas junto con los datos correspondientes
for dato, etiqueta in zip(datos, etiquetas):
    print(f"Dato: {dato}, Etiqueta: {etiqueta}")