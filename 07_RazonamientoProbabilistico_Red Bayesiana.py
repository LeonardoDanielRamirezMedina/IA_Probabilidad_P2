#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Red Bayesiana

# Una red bayesiana es un modelo gráfico que representa las relaciones probabilísticas entre un conjunto de variables

# Definimos las probabilidades a priori para la variable Lluvia
probabilidades_lluvia = {'llueve': 0.2, 'no_llueve': 0.8}

# Definimos las probabilidades condicionales para la variable Paraguas
probabilidades_paraguas = {
    'llueve': {'con_paraguas': 0.9, 'sin_paraguas': 0.1},   # Probabilidad de que alguien lleve paraguas si llueve
    'no_llueve': {'con_paraguas': 0.2, 'sin_paraguas': 0.8} # Probabilidad de que alguien lleve paraguas si no llueve
}

# Función para calcular la probabilidad posterior de la lluvia dado el paraguas
def probabilidad_posterior_lluvia(paraguas):    # Paraguas puede ser 'con_paraguas' o 'sin_paraguas'
    # Inicializamos la probabilidad posterior
    probabilidad_posterior = {'llueve': 0, 'no_llueve': 0}  # Inicializamos la probabilidad posterior para cada estado de la lluvia
    
    # Calculamos la probabilidad posterior para cada estado de la lluvia
    for lluvia in ['llueve', 'no_llueve']:  # Iteramos sobre los posibles estados de la lluvia
        probabilidad_posterior[lluvia] = probabilidades_lluvia[lluvia] * probabilidades_paraguas[lluvia][paraguas]  # Calculamos la probabilidad posterior
    
    # Normalizamos la probabilidad posterior para que sume 1
    total = sum(probabilidad_posterior.values())    # Sumamos las probabilidades para obtener el total
    for lluvia in ['llueve', 'no_llueve']:  # Iteramos sobre los posibles estados de la lluvia
        probabilidad_posterior[lluvia] /= total # Normalizamos la probabilidad posterior
        probabilidad_posterior[lluvia] = round(probabilidad_posterior[lluvia], 2) # Redondeamos a dos decimales
    return probabilidad_posterior

# Calculamos la probabilidad posterior de la lluvia dado que vemos a alguien con un paraguas
print(probabilidad_posterior_lluvia('con_paraguas'))