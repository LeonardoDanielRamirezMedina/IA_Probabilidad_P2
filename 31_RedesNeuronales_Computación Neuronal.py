#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Computación Neuronal

#la computación neuronal es un enfoque computacional que se basa en el funcionamiento del cerebro humano para desarrollar algoritmos y modelos de aprendizaje automático. Las redes neuronales son un tipo de modelo de aprendizaje automático que se inspira en la estructura y funcionamiento del cerebro humano.

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargamos el conjunto de datos de correos electrónicos
# Supongamos que tenemos un archivo CSV con datos de correos electrónicos
data = pd.read_csv('correos.csv')

# Preprocesamos los datos
caracteristicas = data.drop('es_spam', axis=1).values
objetivo = data['es_spam'].values

# Normalizamos las características
scaler = StandardScaler()
caracteristicas_norm = scaler.fit_transform(caracteristicas)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(caracteristicas_norm, objetivo, test_size=0.2, random_state=42)

# Creamos una red neuronal
model = Sequential([
    Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilamos el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamos el modelo
model.fit(X_train, y_train, epochs=10)

# Evaluamos el modelo en el conjunto de prueba
model.evaluate(X_test, y_test)