#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico
#Tema: Ponderación de Verosimilitud


#la ponderación de verosimilitud es una técnica que se utiliza para combinar la información de diferentes fuentes de datos.

import numpy as np   #se importa numpy para trabajar con arreglos
import pandas as pd  #se importa pandas para trabajar con DataFrames
from sklearn.model_selection import train_test_split    #se importa train_test_split para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.linear_model import LogisticRegression   #se importa la regresión logística
from sklearn.metrics import log_loss    #se usa log_loss para calcular la verosimilitud

#tenemos un dataset con tres columnas: 'Edad', 'Salario', 'Compra' (1 si el cliente realizó una compra, 0 en caso contrario)
df = pd.DataFrame({
    'Edad': np.random.randint(18, 70, 1000),    #se generan 1000 números aleatorios entre 18 y 70
    'Salario': np.random.randint(30000, 80000, 1000),   #se generan 1000 números aleatorios entre 30000 y 80000
    'Compra': np.random.randint(0, 2, 1000) #se generan 1000 números aleatorios entre 0 y 2
})

X = df[['Edad', 'Salario']]
y = df['Compra']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar un modelo de regresión logística utilizando la verosimilitud como criterio de ajuste
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Obtener las probabilidades predichas para los datos de prueba
probabilidades = modelo.predict_proba(X_test)

# Calcular la verosimilitud de los datos de prueba dado el modelo
verosimilitud = -log_loss(y_test, probabilidades)   

# Imprimir la verosimilitud 
print(f'La verosimilitud de los datos de prueba dado el modelo es {verosimilitud:.3f}')