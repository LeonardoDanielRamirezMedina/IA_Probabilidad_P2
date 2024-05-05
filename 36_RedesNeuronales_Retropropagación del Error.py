#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Retropropagación del Error

# La retropropagación del error es un algoritmo de aprendizaje supervisado que se utiliza para entrenar redes neuronales.

from sklearn.datasets import fetch_california_housing   #se utiliza para cargar el conjunto de datos de precios de viviendas en California
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.neural_network import MLPRegressor #se utiliza para crear una red neuronal con retropropagación del error
from sklearn.preprocessing import StandardScaler    #se utiliza para normalizar los datos
from sklearn.metrics import r2_score    #se utiliza para calcular el coeficiente de determinación R^2

# Cargamos el conjunto de datos de precios de viviendas en California
housing = fetch_california_housing()

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, random_state=42)

# Normalizamos los datos
scaler = StandardScaler()   #.StandardScaler se utiliza para normalizar los datos
X_train_scaled = scaler.fit_transform(X_train)  #.fit_transform se utiliza para normalizar los datos de entrenamiento
X_test_scaled = scaler.transform(X_test)    #.transform se utiliza para normalizar los datos de prueba

# Entrenamos una red neuronal con retropropagación del error
mlp = MLPRegressor(hidden_layer_sizes=(100, 100), max_iter=1000, alpha=0.001, solver='adam', random_state=42)   #.MLPRegressor se utiliza para crear una red neuronal con retropropagación del error
mlp.fit(X_train_scaled, y_train)    #.fit se utiliza para entrenar la red neuronal con los datos de entrenamiento

# Hacemos predicciones con la red neuronal
y_pred = mlp.predict(X_test_scaled)

# Imprimimos los puntajes de entrenamiento y prueba
print("Puntaje de entrenamiento:", mlp.score(X_train_scaled, y_train))
print("Puntaje de prueba:", mlp.score(X_test_scaled, y_test))

# Imprimimos los primeros 10 valores predichos y reales
print("Primeros 10 valores predichos:", y_pred[:10])
print("Primeros 10 valores reales:", y_test[:10])