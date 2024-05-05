#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Preprocesado: Filtros

# el tema de los filtros es muy importante en el procesamiento de imágenes, ya que permiten mejorar la calidad de las imágenes y extraer información relevante. 
#Uno de los filtros más comunes es el filtro de suavizado, que se utiliza para reducir el ruido y las imperfecciones de una imagen. En este ejemplo, se aplica un filtro de suavizado a una imagen utilizando el filtro de Gauss.

import cv2  # lo utilizamos para cargar y mostrar imágenes
import numpy as np  # lo utilizamos para realizar operaciones matemáticas en las imágenes

# Cargamos la imagen
imagen = cv2.imread('link.jpg') 

# Aplicar filtro de suavizado
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)  # (5, 5) es el tamaño del kernel y 0 es la desviación estándar

# Mostrar imagen original y suavizada
cv2.imshow('Imagen Original', imagen)   
cv2.imshow('Imagen Suavizada', imagen_suavizada)

cv2.waitKey(0)  # esperar a que se presione una tecla
cv2.destroyAllWindows() # cerrar todas las ventanas