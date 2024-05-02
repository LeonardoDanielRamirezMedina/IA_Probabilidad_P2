#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Inferencia por Enumeración

#La inferencia por enumeración es un enfoque que consiste en enumerar todas las posibles combinaciones de eventos para calcular la probabilidad de un evento en particular.

def calcular_probabilidad_ventas():
    # Definición de probabilidades 
    P_compra_A = 0.3  # Probabilidad de comprar el videojuego A
    P_compra_B_dado_A = 0.6  # Probabilidad de comprar el videojuego B dado que ya compró A
    P_compra_C_dado_A_B = 0.4  # Probabilidad de comprar el videojuego C dado que ya compró A y B

    # Calculamos P(compra A ∩ compra B ∩ compra C) usando la regla del producto
    P_ventas = P_compra_A * P_compra_B_dado_A * P_compra_C_dado_A_B

    return P_ventas

probabilidad_ventas = calcular_probabilidad_ventas()    # Llamamos a la función para calcular la probabilidad de que un cliente compre los videojuegos A, B y C
print(f"La probabilidad de que un cliente compre los videojuegos A, B y C es: {probabilidad_ventas:.4f}")   # Mostramos el resultado
