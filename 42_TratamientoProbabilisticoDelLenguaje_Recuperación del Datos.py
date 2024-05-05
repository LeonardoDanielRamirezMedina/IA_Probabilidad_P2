#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Probabilístico del Lenguaje
#Tema: Recuperación del Datos

#Recuperacion de datos se utiliza para encontrar documentos relevantes en una colección de documentos.

from sklearn.feature_extraction.text import CountVectorizer #se usa para convertir texto en vectores de características
from sklearn.metrics.pairwise import cosine_similarity  #se usa para calcular la similitud del coseno entre dos vectores

# Base de datos de libros
libros = [
    "El gran Gatsby",
    "Matar a un ruiseñor",
    "1984",
    "Un cuento de dos ciudades",
    "El señor de los anillos"
]

# Consulta de búsqueda
consulta = "Gatsby" 

# Convertimos los libros y la consulta a vectores de características
vectorizer = CountVectorizer().fit_transform(libros + [consulta])   #fit_transform se usa para ajustar el modelo y luego transformar los datos
vectors = vectorizer.toarray()  #toarray se usa para convertir la matriz dispersa en una matriz densa

# Calculamos la similitud del coseno entre la consulta y cada libro
similitudes = cosine_similarity(vectors)[-1][:-1]   #cosine_similarity se usa para calcular la similitud del coseno entre dos vectores

# Imprimimos los libros ordenados por su similitud con la consulta
for libro, similitud in sorted(zip(libros, similitudes), key=lambda x: -x[1]):      #sorted se usa para ordenar los elementos de una lista.ke
    print(f"{libro}: {similitud}")  #imprime el libro y su similitud con la consulta