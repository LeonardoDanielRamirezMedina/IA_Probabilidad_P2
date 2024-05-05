#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Máquinas de Vectores Soporte (Núcleo)

# Las máquinas de vectores soporte (SVM) son un tipo de algoritmo de aprendizaje supervisado que se utiliza para clasificar objetos en grupos basándose en sus características.


from sklearn import datasets    #se utiliza para cargar el conjunto de datos Iris
from sklearn import svm  #se utiliza para crear un Support Vector Machine
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.metrics import classification_report   #se utiliza para imprimir un informe de clasificación

# Cargamos el conjunto de datos Iris
iris = datasets.load_iris()

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Creamos una SVM con un núcleo gaussiano
clasificador = svm.SVC(kernel='rbf', probability=True)  #.svc se utiliza para crear un Support Vector Machine con un núcleo gaussiano

# Entrenamos la SVM
clasificador.fit(X_entrenamiento, y_entrenamiento)  #.fit se utiliza para entrenar la SVM con los datos de entrenamiento

# Hacemos predicciones en el conjunto de prueba
y_prediccion = clasificador.predict(X_prueba)   #.predict se utiliza para hacer predicciones en el conjunto de prueba

# Imprimimos un informe de clasificación
print(classification_report(y_prueba, y_prediccion))    