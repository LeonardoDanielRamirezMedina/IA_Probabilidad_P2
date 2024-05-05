#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Perceptrón, ADALINE y MADALINE

# perceptron, adaline y madaline son algoritmos de aprendizaje supervisado que se utilizan para clasificar objetos en grupos basándose en sus características.

import numpy as np
from sklearn.linear_model import Perceptron #se utiliza para crear un perceptrón
from sklearn.neural_network import MLPClassifier #se utiliza para crear un MLP
from sklearn.datasets import make_classification    #se utiliza para generar un conjunto de datos de clasificación
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Generamos un conjunto de datos de clasificación binaria
X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1)    #.make_classification se utiliza para generar un conjunto de datos de clasificación

# Imprimimos los datos de entrada
print("Datos de entrada:")
print(X)    

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Entrenamos un perceptrón
clf_perceptron = Perceptron(tol=1e-3, random_state=0)   #.Perceptron se utiliza para crear un perceptrón. perceptron es un algoritmo de aprendizaje supervisado que se utiliza para clasificar objetos en grupos basándose en sus características.
clf_perceptron.fit(X_train, y_train)    #.fit se utiliza para entrenar el perceptrón

# Hacemos predicciones con el perceptrón y las imprimimos
y_pred_perceptron = clf_perceptron.predict(X_test)  #.predict se utiliza para hacer predicciones con el perceptrón
print("Predicciones del perceptrón:")   
print(y_pred_perceptron)    #imprime las predicciones del perceptrón

# Entrenamos un ADALINE (MLP con una sola capa y función de activación lineal)
clf_adaline = MLPClassifier(hidden_layer_sizes=(), activation='identity', solver='sgd', learning_rate_init=0.01, max_iter=1000)   #.MLPClassifier se utiliza para crear un MLP. MLP es un algoritmo de aprendizaje supervisado que se utiliza para clasificar objetos en grupos basándose en sus características.
clf_adaline.fit(X_train, y_train)   #.fit se utiliza para entrenar el ADALINE

# Hacemos predicciones con el ADALINE y las imprimimos
y_pred_adaline = clf_adaline.predict(X_test)    #.predict se utiliza para hacer predicciones con el ADALINE
print("Predicciones del ADALINE:")  
print(y_pred_adaline)   #imprime las predicciones del ADALINE

# Entrenamos un MADALINE (MLP con una capa oculta y función de activación lineal)
clf_madaline = MLPClassifier(hidden_layer_sizes=(5,), activation='identity', solver='sgd', learning_rate_init=0.01, max_iter=1000)  #.MLPClassifier se utiliza para crear un MLP. MLP es un algoritmo de aprendizaje supervisado que se utiliza para clasificar objetos en grupos basándose en sus características.
clf_madaline.fit(X_train, y_train)  #.fit se utiliza para entrenar el MADALINE

# Hacemos predicciones con el MADALINE y las imprimimos
y_pred_madaline = clf_madaline.predict(X_test)  #.predict se utiliza para hacer predicciones con el MADALINE
print("Predicciones del MADALINE:")
print(y_pred_madaline)  #imprime las predicciones del MADALINE