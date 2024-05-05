#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Probabilístico del Lenguaje
#Tema: Extracción de Información

#Extracción de información se utiliza para identificar entidades importantes en un texto.

import spacy    #spacy es una biblioteca de procesamiento de lenguaje natural

# Cargamos el modelo de lenguaje
nlp = spacy.load("en_core_web_sm")  #en_core_web_sm es un modelo de lenguaje en inglés

# Texto de entrada
texto = "Apple is looking at buying U.K. startup for $1 billion"    # lo que se va a analizar

# Procesamos el texto
doc = nlp(texto)    #npl se usa para procesar el texto

# Imprimimos las entidades nombradas, sus tipos y la explicación de los tipos
for ent in doc.ents:
    print(f"Texto: {ent.text}")   #imprime el texto
    print(f"Tipo: {ent.label_}")    #imprime el tipo
    print(f"Explicación: {spacy.explain(ent.label_)}")  #imprime la explicación
    print("---")