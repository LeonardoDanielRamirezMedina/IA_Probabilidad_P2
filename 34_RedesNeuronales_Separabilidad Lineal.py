#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Separabilidad Lineal

# la separabilidad lineal es una propiedad de los datos que se pueden dividir en dos grupos utilizando una línea recta.

from sklearn import datasets    #se utiliza para cargar el conjunto de datos Iris
from sklearn.svm import SVC #se utiliza para crear un Support Vector Machine
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Cargamos el conjunto de datos de flores Iris
iris = datasets.load_iris()

# Imprimimos los datos de entrada
print("Datos de entrada:")
print(iris.data)    

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)     #.train_test_split se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Usamos un SVM con un kernel lineal para clasificar las flores
clf = SVC(kernel='linear', C=1.0)   #.svc se utiliza para crear un Support Vector Machine con un kernel lineal
clf.fit(X_train, y_train)   #.fit se utiliza para entrenar el SVM con los datos de entrenamiento

# Hacemos predicciones con el SVM y las imprimimos
y_pred = clf.predict(X_test)    #.predict se utiliza para hacer predicciones con el SVM
print("Predicciones del SVM:")      
print(y_pred)   #imprime las predicciones del SVM