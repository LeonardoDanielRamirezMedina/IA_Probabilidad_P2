#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Redes Neuronales
#Tema: Gramáticas Probab. Independ. del Contexto

#La gramática probabilística independiente del contexto es una gramática formal que se utiliza para describir la estructura de las oraciones en un lenguaje natural.
import random

# Definimos una gramática probabilística independiente del contexto para generar oraciones
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["Det", "N", "PP"], ["I"]],
    "Det": [["an"], ["my"]],
    "N": [["elephant"], ["pajamas"]],
    "VP": [["V", "NP"], ["V", "NP", "PP"]],
    "V": [["shot"]],
    "PP": [["P", "NP"]],
    "P": [["in"]]
}

# Generamos una oración aleatoria
def generate_sentence(symbol):  
    if symbol not in grammar:   # Si el símbolo no está en la gramática, es un terminal
        return [symbol]        # Devolvemos el símbolo como una lista
    expansion = random.choice(grammar[symbol])  # Elegimos una expansión aleatoria para el símbolo
    return [word for symbol in expansion for word in generate_sentence(symbol)] # Generamos recursivamente las palabras de la expansión

random_sentence = ' '.join(generate_sentence("S"))  # Generamos una oración aleatoria a partir del símbolo inicial S
print(f"Oración generada: {random_sentence}")      # Imprimimos la oración generada