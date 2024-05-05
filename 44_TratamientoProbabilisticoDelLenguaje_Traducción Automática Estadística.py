#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Probabilístico del Lenguaje
#Tema: Traducción Automática Estadística

from nltk.translate import PhraseTable  #se usa para almacenar las traducciones de las frases
from nltk.translate.stack_decoder import StackDecoder   #se usa para decodificar la pila

# Tabla de frases
phrase_table = PhraseTable()    #almacena las traducciones de las frases
phrase_table.add(('the cat', 'le chat'), logprob=0.3)   #agrega una traducción de la frase
phrase_table.add(('sat on', 's\'est assis sur'), logprob=0.4)   
phrase_table.add(('the mat', 'le tapis'), logprob=0.2)

# Decodificador de pila
decoder = StackDecoder(phrase_table)

# Frase de entrada
frase = 'the cat sat on the mat'    #frase que se va a traducir

# Traducimos la frase
traduccion = decoder.translate(frase)   #translate se usa para traducir la frase

print(traduccion)   #imprime la traducción de la frase