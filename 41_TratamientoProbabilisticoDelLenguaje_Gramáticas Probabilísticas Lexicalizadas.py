#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Tratamiento Probabilístico del Lenguaje
#Tema: Gramáticas Probabilísticas Lexicalizadas

# las gramáticas probabilísticas lexicalizadas son una extensión de las gramáticas probabilísticas que incluyen reglas de producción con palabras concretas en lugar de categorías gramaticales.

import nltk  #nltk es una biblioteca de procesamiento de lenguaje natural
from nltk import Nonterminal    #Nonterminal se usa para representar una categoría gramatical
from nltk.probability import DictionaryProbDist   #DictionaryProbDist se usa para representar una distribución de probabilidad

# Definimos las reglas de producción y sus probabilidades
rules = {
    Nonterminal('S'): DictionaryProbDist({  #DictionaryProbDist se usa para representar una distribución de probabilidad
        'NP VP': 0.9,       #NP VP es una regla de producción
        'Interj S': 0.1    #Interj S es una regla de producción
    }),
    Nonterminal('NP'): DictionaryProbDist({ 
        'Det N': 0.6,   # 0.6 es la probabilidad de la regla de producción
        'Det N PP': 0.4 # 0.4 es la probabilidad de la regla de producción
    }),
    Nonterminal('VP'): DictionaryProbDist({
        'V NP': 0.5,    # 0.5 es la probabilidad de la regla de producción
        'VP PP': 0.5    # 0.5 es la probabilidad de la regla de producción
    }),
    Nonterminal('PP'): DictionaryProbDist({
        'P NP': 1.0    # 1.0 es la probabilidad de la regla de producción
    }),
}

# Creamos la gramática probabilística lexicalizada
lpg = nltk.PCFG.fromstring("""  
    S -> NP VP [1.0]    
    NP -> Det N [0.5] | Det N PP [0.5]
    VP -> V NP [0.5] | VP PP [0.5]
    PP -> P NP [1.0]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'chased' [0.5] | 'sat' [0.5]
    P -> 'on' [0.5] | 'in' [0.5]
""")

# Creamos un analizador de árboles sintácticos con la gramática
parser = nltk.ViterbiParser(lpg)  #ViterbiParser se usa para analizar oraciones con una gramática probabilística

# Analizamos una oración
sentence = 'the dog chased a cat'.split()  #split() se usa para dividir una cadena en una lista de palabras
for tree in parser.parse(sentence): #parse() se usa para analizar una oración
    print(tree) #Imprime el árbol sintáctico