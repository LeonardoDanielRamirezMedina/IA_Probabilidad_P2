#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Eliminación de Variables

#La eliminación de variables es un enfoque que consiste en eliminar las variables intermedias para calcular la probabilidad de un evento en particular.

# Definimos las probabilidades condicionales
P_A = {'compra': 0.2, 'no_compra': 0.8} # Probabilidad de comprar y no comprar
P_B_given_A = {'compra': {'compra': 0.6, 'no_compra': 0.4}, 'no_compra': {'compra': 0.3, 'no_compra': 0.7}} # Probabilidad de comprar y no comprar dado que ya compró
P_C_given_B = {'compra': {'compra': 0.7, 'no_compra': 0.3}, 'no_compra': {'compra': 0.4, 'no_compra': 0.6}} # Probabilidad de comprar y no comprar dado que ya compró A y B

# Definir la función de eliminación de variables
def eliminacion_variables(P_A, P_B_given_A, P_C_given_B, C):    #esta funcion recibe las probabilidades de las variables A, B y C, y la variable C
    P_A_given_C = {'compra': 0, 'no_compra': 0}   #inicializamos la probabilidad de A dado C
    for A in ['compra', 'no_compra']:   #iteramos sobre las posibles opciones de A
        for B in ['compra', 'no_compra']:   #iteramos sobre las posibles opciones de B
            P_A_given_C[A] += P_A[A] * P_B_given_A[A][B] * P_C_given_B[B][C]    #calculamos la probabilidad de A dado C
    return P_A_given_C  #retornamos la probabilidad de A dado C

# Calcular la probabilidad de A dado C
P_A_given_C = eliminacion_variables(P_A, P_B_given_A, P_C_given_B, 'compra')    #llamamos a la función para calcular la probabilidad de A dado C
print(f"P(A = 'compra' | C = 'compra') = {P_A_given_C['compra']:.2f}")  #mostramos el resultado