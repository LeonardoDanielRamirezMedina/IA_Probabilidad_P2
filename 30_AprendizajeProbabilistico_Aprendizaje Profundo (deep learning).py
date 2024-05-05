#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Aprendizaje Probabilístico
#Tema: Aprendizaje Profundo (Deep Learning)

# El deep learning es una rama del aprendizaje automático que se enfoca en el uso de redes neuronales profundas para aprender representaciones de datos de alto nivel. En este enfoque, se utilizan múltiples capas de neuronas para aprender características complejas de los datos.

import tensorflow as tf
from tensorflow.keras import layers, models #se usa la librería keras para definir el modelo de red neuronal convolucional (CNN)
from tensorflow.keras.datasets import mnist #se importa el conjunto de datos MNIST
import matplotlib.pyplot as plt

# Cargamos el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()    #train_images y train_labels son las imágenes y etiquetas de entrenamiento, test_images y test_labels son las imágenes y etiquetas de prueba

# Preprocesamiento de datos
train_images = train_images.reshape((60000, 28, 28, 1))   #se cambia la forma de las imágenes de entrenamiento
train_images = train_images.astype('float32') / 255  #se normalizan las imágenes de entrenamiento

test_images = test_images.reshape((10000, 28, 28, 1))   #se cambia la forma de las imágenes de prueba
test_images = test_images.astype('float32') / 255   #se normalizan las imágenes de prueba

# Definir el modelo de red neuronal convolucional (CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  #se define la capa convolucional con 32 filtros y función de activación relu
    layers.MaxPooling2D((2, 2)),    #se define la capa de pooling
    layers.Conv2D(64, (3, 3), activation='relu'),   #se define la segunda capa convolucional con 64 filtros y función de activación relu
    layers.MaxPooling2D((2, 2)),    #se define la segunda capa de pooling
    layers.Conv2D(64, (3, 3), activation='relu'),  #se define la tercera capa convolucional con 64 filtros y función de activación relu
    layers.Flatten(),   #se aplana la salida de la capa convolucional
    layers.Dense(64, activation='relu'),    #se define una capa densa con 64 neuronas y función de activación relu
    layers.Dense(10, activation='softmax')  #se define la capa de salida con 10 neuronas y función de activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',     #se usa el optimizador Adam
              loss='sparse_categorical_crossentropy',       #se usa la función de pérdida de entropía cruzada categórica escasa
              metrics=['accuracy'])     #se usa la métrica de precisión

# Entrenar el modelo
history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)  #se entrena el modelo con 5 épocas y un tamaño de lote de 64

# Evaluar el modelo con el conjunto de datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)  #se evalúa el modelo con el conjunto de datos de prueba
print('Test accuracy:', test_acc)   #se imprime la precisión del modelo en el conjunto de datos de prueba

# Graficar la precisión de entrenamiento y validación a lo largo de las épocas
plt.plot(history.history['accuracy'], label='accuracy')  #se grafica la precisión de entrenamiento
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')   #se grafica la precisión de validación
plt.xlabel('Epoch')    #se muestra la época en el eje x
plt.ylabel('Accuracy')   #se muestra la precisión en el eje y
plt.ylim([0.9, 1])  #se establece el rango del eje y
plt.legend(loc='lower right')   #se muestra la leyenda en la esquina inferior derecha
plt.show()  #se muestra la gráfica
