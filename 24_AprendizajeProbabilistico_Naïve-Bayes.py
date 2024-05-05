#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Naïve-Bayes

from sklearn.feature_extraction.text import CountVectorizer #se utiliza para convertir una colección de documentos de texto en una matriz de recuentos de tokens
from sklearn.naive_bayes import MultinomialNB   #se utiliza para implementar el clasificador Naïve-Bayes
from sklearn import metrics #se utiliza para evaluar la precisión del clasificador

# Conjunto de datos de entrenamiento
mensajes = ['¡Gana dinero ahora!', '¡Haz clic aquí!', 'Necesito un favor', 'Hola, ¿cómo estás?']
etiquetas = ['spam', 'spam', 'no spam', 'no spam']

# Convertimos los mensajes en una matriz de conteo de palabras
vectorizer = CountVectorizer()  # Convertimos una colección de documentos de texto en una matriz de recuentos de tokens
X_train = vectorizer.fit_transform(mensajes)    #se ajusta el vectorizador y se transforma el conjunto de datos de entrenamiento

# Crear un clasificador Naïve-Bayes
clf = MultinomialNB()   #se crea un clasificador Naïve-Bayes

# Entrenar el clasificador
clf.fit(X_train, etiquetas) #.fit se utiliza para ajustar el modelo a los datos de entrenamiento

# Conjunto de datos de prueba
mensajes_test = ['¡Gana premios!', 'Hola, necesito tu ayuda']   
X_test = vectorizer.transform(mensajes_test)    #transforma el conjunto de datos de prueba

predicciones = clf.predict(X_test)  #se utilizan las predicciones para predecir el conjunto de datos de prueba

# Imprimir las predicciones
print(predicciones) #se imprimen las predicciones