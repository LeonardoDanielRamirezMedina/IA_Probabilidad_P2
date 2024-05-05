#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Reconocimiento de Escritura

import cv2
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Cargar el conjunto de datos de dígitos escritos a mano (MNIST)
digits = datasets.load_digits()

# Dividir los datos en características (X) y etiquetas (y)
X = digits.data
y = digits.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un clasificador de SVM
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train, y_train)

# Función para predecir dígitos escritos a mano
def predict_digit(image):
    # Preprocesar la imagen para que coincida con el formato de entrada del clasificador SVM
    image = cv2.resize(image, (8, 8))
    image = np.reshape(image, (1, -1))
    
    # Predecir el dígito utilizando el clasificador SVM entrenado
    prediction = svm_clf.predict(image)
    return prediction[0]

# Cargar una imagen de un dígito escrito a mano
image_path = 'numero4.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Predecir el dígito utilizando la función predict_digit
predicted_digit = predict_digit(image)

# Mostrar el dígito predicho
print("Dígito predicho:", predicted_digit)

# Mostrar la imagen
cv2.imshow('Imagen', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
