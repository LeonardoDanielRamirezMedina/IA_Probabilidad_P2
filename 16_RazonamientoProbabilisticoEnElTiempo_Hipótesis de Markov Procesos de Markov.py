#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Hipótesis de Markov: Procesos de Markov

#este tema se aplica en la predicción de eventos futuros, basándose en eventos pasados, es decir, se basa en la probabilidad condicional de que un evento futuro dependa solo del evento inmediatamente anterior.	

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity  # se utiliza la función cosine_similarity de la librería sklearn.metrics.pairwise para calcular la similitud entre los usuarios

#matriz de calificaciones de usuarios y películas
calificaciones = np.array([
    [5, 4, 0, 0, 1],
    [4, 0, 0, 5, 2],
    [0, 4, 5, 0, 1],
    [5, 5, 0, 1, 2],
    [0, 0, 4, 4, 0],
])

#lista de nombres de películas
peliculas = ['Pelicula 1', 'Pelicula 2', 'Pelicula 3', 'Pelicula 4', 'Pelicula 5']

#se calcula la similitud entre los usuarios
similitud = cosine_similarity(calificaciones)

#se obtiene el usuario más similar a cada usuario
usuarios_mas_similares = np.argmax(similitud, axis=1)   #argmax es una función que devuelve el índice del valor máximo en un array

# Recomendar a cada usuario las películas que le gustaron al usuario más similar
recomendaciones = []
for usuario, usuario_similar in enumerate(usuarios_mas_similares):  #enumerate se utiliza para obtener el índice y el valor de un array
    gustadas_por_similar = np.where(calificaciones[usuario_similar] > 0)        #where se utiliza para obtener los índices de los elementos que cumplen una condición
    recomendaciones.append([peliculas[i] for i in gustadas_por_similar[0]])   #se obtienen las películas que le gustaron al usuario similar y se agregan a la lista de recomendaciones

for i, recs in enumerate(recomendaciones):  #enumerate se utiliza para obtener el índice y el valor de un array
    print(f'Recomendaciones para el usuario {i+1}: {recs}') #se imprimen las recomendaciones para cada usuario