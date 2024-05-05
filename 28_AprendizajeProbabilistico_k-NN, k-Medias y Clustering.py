#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: k-NN, k-Medias y Clustering

# El algoritmo k-NN es un algoritmo de aprendizaje supervisado que se utiliza para clasificar objetos en grupos basándose en sus características.

from sklearn.feature_extraction.text import TfidfVectorizer #se utiliza para convertir las descripciones de las películas en una matriz TF-IDF
from sklearn.cluster import KMeans, AgglomerativeClustering #se utiliza para crear y ajustar modelos de agrupamiento
from sklearn.neighbors import KNeighborsClassifier  #se utiliza para crear y entrenar un clasificador k-NN
from sklearn.model_selection import train_test_split    #se utiliza para dividir los datos en conjuntos de entrenamiento y prueba

# Conjunto de datos de películas
descripciones = ['Una gran aventura espacial con mucha acción y efectos especiales',
                 'Un drama profundo sobre la vida de una familia',
                 'Una comedia hilarante con un elenco estelar',
                 'Un thriller de acción con muchas persecuciones y tiroteos',
                 'Una película de terror que te mantendrá en vilo todo el tiempo',
                 'Un drama histórico ambientado en la Segunda Guerra Mundial']
generos = ['Ciencia Ficción', 'Drama', 'Comedia', 'Acción', 'Terror', 'Drama Histórico']

# Convertimos las descripciones en una matriz TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(descripciones) # Convertimos las descripciones en una matriz TF-IDF

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, generos, test_size=0.2, random_state=42) # Dividimos los datos en conjuntos de entrenamiento y prueba

knn = KNeighborsClassifier(n_neighbors=3)   # Creamos un clasificador k-NN con 3 vecinos
knn.fit(X_train.toarray(), y_train) # Entrenamos el clasificador con los datos de entrenamiento

kmeans = KMeans(n_clusters=3)   # Creamos un modelo K-Means con 3 clusters
kmeans.fit(X_train.toarray())   # Ajustamos el modelo a los datos de entrenamiento

agg = AgglomerativeClustering(n_clusters=3) # Creamos un modelo de agrupamiento jerárquico con 3 clusters
agg.fit(X_train.toarray())  # Ajustamos el modelo a los datos de entrenamiento

predicciones_knn = knn.predict(X_test.toarray())    # Predecimos las etiquetas de los datos de prueba con el clasificador k-NN
predicciones_kmeans = kmeans.predict(X_test.toarray())  # Predecimos las etiquetas de los datos de prueba con el modelo K-Means

# Imprimimos las predicciones
print('Predicciones k-NN:', predicciones_knn)
print('Predicciones k-Means:', predicciones_kmeans)