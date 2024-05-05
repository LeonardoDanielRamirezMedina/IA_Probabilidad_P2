#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Texturas y Sombras

# La textura es una propiedad importante de las imágenes que se utiliza para describir la apariencia de una superficie.

from PIL import Image   # lo utilizamos para cargar y mostrar imágenes
import numpy as np  # lo utilizamos para realizar operaciones matemáticas en las imágenes

# Cargamos imagen
imagen = Image.open('link.jpg').convert('L')  # Convertimos a escala de grises. 'L' es el modo de escala de grises
imagen = np.array(imagen)   # Convertimos la imagen a un arreglo de numpy

# Calculamos la textura como la desviación estándar de la imagen
textura = np.std(imagen)

# Calculamos la cantidad de sombras como la cantidad de píxeles oscuros
# Consideramos un pixel como "oscuro" si su valor es menor a 128
sombras = np.sum(imagen < 128)

print(f"Textura: {textura}")    # Mostramos la textura
print(f"Sombras: {sombras}")    # Mostramos la cantidad de sombras