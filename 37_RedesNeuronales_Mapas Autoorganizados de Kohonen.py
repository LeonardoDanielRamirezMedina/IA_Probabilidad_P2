#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Mapas Autoorganizados de Kohonen

# Los mapas autoorganizados de Kohonen son una técnica de aprendizaje no supervisado que se utiliza para visualizar y clasificar datos.

from sklearn.datasets import load_wine  #se utiliza para cargar el conjunto de datos de vinos
from sklearn.preprocessing import StandardScaler    #se utiliza para normalizar los datos
from minisom import MiniSom   #se utiliza para crear un mapa autoorganizado de Kohonen
import numpy as np  #se utiliza para realizar operaciones numéricas

# Establecemos la precisión de la salida a dos decimales
np.set_printoptions(precision=2)    #.set_printoptions se utiliza para establecer las opciones de impresión

# Cargamos el conjunto de datos de vinos
wine = load_wine()  #.load_wine se utiliza para cargar el conjunto de datos de vinos

# Normalizamos los datos
scaler = StandardScaler()
data = scaler.fit_transform(wine.data)  #.fit_transform se utiliza para normalizar los datos

# Entrenamos un mapa autoorganizado de Kohonen
som = MiniSom(7, 7, data.shape[1], sigma=1.0, learning_rate=0.5)    #.MiniSom se utiliza para crear un mapa autoorganizado de Kohonen
som.train_random(data, 5000)    #.train_random se utiliza para entrenar el mapa con datos aleatorios

# Clasificamos los vinos con el mapa autoorganizado
winemap = som.win_map(data) #.win_map se utiliza para clasificar los vinos con el mapa autoorganizado

# Imprimimos el mapa de vinos de manera organizada
print("Mapa de vinos:")
for i, wines in winemap.items():  #en este caso, i es el grupo y wines son los vinos en ese grupo  
    print(f"Grupo {i}:")
    for wine in wines:
        print(wine)