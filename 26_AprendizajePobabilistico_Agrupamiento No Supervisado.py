#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Agrupamiento No Supervisado

# El agrupamiento no supervisado es una técnica de aprendizaje automático que se utiliza para identificar grupos de datos similares en un conjunto de datos sin etiquetar.

from sklearn.cluster import KMeans  #se utiliza para implementar el algoritmo K-Means
import numpy as np

# Datos de los hábitos de compra de los clientes. son la frecuencia de compra y el monto gastado
datos = np.array([
    [5, 200],  # Cliente 1: compra 5 veces al mes, gasta $200
    [2, 50],   # Cliente 2: compra 2 veces al mes, gasta $50
    [1, 20],   # Cliente 3: compra 1 vez al mes, gasta $20
    [10, 500], # Cliente 4: compra 10 veces al mes, gasta $500
    [4, 100],  # Cliente 5: compra 4 veces al mes, gasta $100
    [6, 300]   # Cliente 6: compra 6 veces al mes, gasta $300
])

# Creamos un modelo K-Means con dos clusters. los clusters son los grupos de clientes
kmeans = KMeans(n_clusters=2)

# Ajustamos el modelo a los datos
kmeans.fit(datos)       

# Predecimos las etiquetas de los datos
etiquetas = kmeans.predict(datos)   # Las etiquetas son los clusters a los que pertenecen los clientes

# Imprimimos las etiquetas junto con los datos correspondientes
for i, (dato, etiqueta) in enumerate(zip(datos, etiquetas), 1):
    print(f"Cliente {i}: {dato}, Grupo: {etiqueta}")