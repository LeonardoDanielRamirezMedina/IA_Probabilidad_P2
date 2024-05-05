#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Hamming, Hopfield, Hebb, Boltzmann

#hamming se utiliza para reconocimiento de patrones, hopfield se utiliza para almacenar y recuperar patrones, hebb se utiliza para el aprendizaje de asociación, y boltzmann se utiliza para el aprendizaje de máquinas de Boltzmann.

from sklearn.neural_network import MLPClassifier    #se utiliza para crear una red neuronal multicapa
from sklearn.preprocessing import StandardScaler    #se utiliza para normalizar los datos
import numpy as np  #se utiliza para realizar operaciones numéricas

# Creamos una red neuronal multicapa para el reconocimiento de patrones
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, alpha=0.001, solver='adam', random_state=42)   #.MLPClassifier se utiliza para crear una red neuronal multicapa

# Entrenamos la red con algunos patrones
patterns = np.array([[1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
                     [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]])
labels = np.array([1, 0])  # Etiquetas para los patrones
mlp.fit(patterns, labels)

# Probamos la red con un patrón ruidoso
noisy_pattern = np.array([1, 1, 1, -1, 1, -1, 1, -1, 1, -1]).reshape(1, -1) # Patrón ruidoso
predicted_label = mlp.predict(noisy_pattern)    #.predict se utiliza para predecir la etiqueta del patrón ruidoso
print("Etiqueta predicha para el patrón ruidoso:")  # Imprimimos la etiqueta predicha
print(predicted_label)