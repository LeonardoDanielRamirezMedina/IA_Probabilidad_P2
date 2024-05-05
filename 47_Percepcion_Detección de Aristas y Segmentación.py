#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Detección de Aristas y Segmentación

# La detección de bordes es una técnica importante en el procesamiento de imágenes, ya que permite identificar los límites de los objetos en una imagen.

import cv2  # lo utilizamos para cargar y mostrar imágenes
import numpy as np  # lo utilizamos para realizar operaciones matemáticas en las imágenes

# Cargamos la imagen con la que vamos a trabajar en escala de grises
imagen = cv2.imread('link.jpg', cv2.IMREAD_GRAYSCALE)

# Detectar bordes
bordes = cv2.Canny(imagen, 100, 200)    # 100 y 200 son los umbrales mínimo y máximo

# Mostrar imagen original y bordes
cv2.imshow('Imagen Original', imagen)       # Mostramos la imagen original
cv2.imshow('Bordes', bordes)    # Mostramos la imagen con los bordes detectados

cv2.waitKey(0)  # esperar a que se presione una tecla
cv2.destroyAllWindows() # cerrar todas las ventanas