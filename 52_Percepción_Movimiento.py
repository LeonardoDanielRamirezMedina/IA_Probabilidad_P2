#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Percepción
#Tema: Movimiento

import cv2

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Leer los primeros dos cuadros
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:
    # Convertir los cuadros a escala de grises
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Calcular la diferencia absoluta entre los cuadros
    diff = cv2.absdiff(gray1, gray2)
    
    # Aplicar umbral para resaltar las diferencias significativas
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
    # Dilatar el umbral para eliminar el ruido
    dilated = cv2.dilate(thresh, None, iterations=2)
    
    # Encontrar contornos de objetos en movimiento
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar contornos en el cuadro original
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Mostrar el cuadro con objetos en movimiento
    cv2.imshow('Movimiento detectado', frame1)
    
    # Actualizar los cuadros para el próximo ciclo
    frame1 = frame2
    ret, frame2 = cap.read()
    
    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
