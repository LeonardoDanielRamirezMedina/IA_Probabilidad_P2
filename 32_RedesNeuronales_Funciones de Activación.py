#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Redes Neuronales

import numpy as np
from tensorflow.keras.models import Sequential  #se utiliza para crear un modelo secuencial
from tensorflow.keras.layers import Dense   #se utiliza para agregar capas densas a la red neuronal
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.preprocessing import StandardScaler    #se utiliza para normalizar las características


# El objetivo es si el correo electrónico es spam (1) o no (0)
caracteristicas = np.random.rand(1000, 10)  # Generamos características aleatorias
objetivo = np.random.randint(2, size=1000)  # Generamos objetivos aleatorios

# Normalizamos las características
scaler = StandardScaler()   #.StandardScaler se utiliza para normalizar las características
caracteristicas_norm = scaler.fit_transform(caracteristicas)    #.fit_transform se utiliza para normalizar las características

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(caracteristicas_norm, objetivo, test_size=0.2, random_state=42) #.train_test_split se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Creamos una red neuronal con una función de activación sigmoide en la capa de salida
model = Sequential([
    Dense(64, activation='relu', input_shape=[X_train.shape[1]]),   #.Dense se utiliza para agregar una capa densa a la red neuronal
    Dense(64, activation='relu'),   
    Dense(1, activation='sigmoid')
])

# Compilamos el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamos el modelo
model.fit(X_train, y_train, epochs=10)

# Evaluamos el modelo en el conjunto de prueba
model.evaluate(X_test, y_test)