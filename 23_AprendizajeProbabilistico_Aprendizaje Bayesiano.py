#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Aprendizaje Bayesiano

#El aprendizaje bayesiano es un enfoque probabilístico para el aprendizaje automático que se basa en el teorema de Bayes.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Conjunto de datos de entrenamiento
correos = ['¡Gana dinero ahora!', '¡Haz clic aquí!', 'Necesito un favor', 'Hola, ¿cómo estás?'] 
etiquetas = ['spam', 'spam', 'no spam', 'no spam']  # Etiquetas de clase

# Se convierten los correos en una matriz de conteo de palabras
vectorizer = CountVectorizer()  # Convertimos una colección de documentos de texto en una matriz de recuentos de  tokens
X_train = vectorizer.fit_transform(correos) #se ajusta el vectorizador y se transforma el conjunto de datos de entrenamiento

#clasificador bayesiano ingenuo
clf = MultinomialNB()   

# Entrenar el clasificador
clf.fit(X_train, etiquetas) #.fit se utiliza para ajustar el modelo a los datos de entrenamiento

# Conjunto de datos de prueba
correos_test = ['¡Gana premios!', 'Hola, necesito tu ayuda']    
X_test = vectorizer.transform(correos_test) #transforma el conjunto de datos de prueba

# Hacemos predicciones en el conjunto de prueba
predicciones = clf.predict(X_test)

# Imprimimos las predicciones
print(predicciones)