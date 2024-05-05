#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Modelo Probabilístico del Lenguaje: Corpus

# Un modelo probabilístico del lenguaje es una forma de representar la probabilidad de una secuencia de palabras en un lenguaje natural.

from collections import defaultdict #se utiliza para crear diccionarios con valores predeterminados

# Definimos un corpus de texto
corpus = ["el gato come pescado", "el perro come huesos", "el gato juega con el perro", "el perro persigue al gato"]    

# Generamos los bigramas del corpus
bigrams = defaultdict(list) # Diccionario de listas para almacenar los bigramas
for sentence in corpus: # Recorremos cada oración en el corpus
    words = sentence.split()    # Dividimos la oración en palabras
    for i in range(len(words) - 1): # Recorremos cada palabra en la oración
        bigrams[words[i]].append(words[i + 1])  # Añadimos la palabra siguiente como un bigrama

# Predecimos la siguiente palabra después de "el"
word = "el"
next_word = max(bigrams[word], key=bigrams[word].count)   # Predecimos la palabra más probable después de "el" basándonos en la frecuencia de los bigramas
print(f"La palabra más probable después de '{word}' es '{next_word}'")  # Imprimimos la palabra predicha