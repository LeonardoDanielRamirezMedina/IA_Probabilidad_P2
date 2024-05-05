#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Redes Multicapa

#Las redes multicapa son un tipo de red neuronal que consta de múltiples capas de neuronas interconectadas.

from sklearn.datasets import fetch_california_housing   #se utiliza para cargar el conjunto de datos de precios de casas en California
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.neural_network import MLPRegressor #se utiliza para crear una red neuronal multicapa
from sklearn.preprocessing import StandardScaler    #se utiliza para normalizar las características

# Cargamos el conjunto de datos de precios de casas en California
housing = fetch_california_housing()

# Imprimimos los datos de entrada
print("Datos de entrada:")
print(housing.data)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, random_state=42)  #.train_test_split se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Normalizamos los datos
scaler = StandardScaler()   #.StandardScaler se utiliza para normalizar las características
X_train_scaled = scaler.fit_transform(X_train)  #.fit_transform se utiliza para normalizar las características
X_test_scaled = scaler.transform(X_test)    #.transform se utiliza para normalizar las características

# Entrenamos una red neuronal multicapa
mlp = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=1000, alpha=0.001, solver='adam', random_state=42)   #.MLPRegressor se utiliza para crear una red neuronal multicapa
mlp.fit(X_train_scaled, y_train)    #.fit se utiliza para entrenar la red neuronal

# Hacemos predicciones con la red neuronal y las imprimimos
y_pred = mlp.predict(X_test_scaled)   #.predict se utiliza para hacer predicciones con la red neuronal
print("Predicciones de la red neuronal:")   
print(y_pred)   #imprime las predicciones de la red neuronal