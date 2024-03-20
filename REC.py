import cv2

# Abre la cámara web
cap = cv2.VideoCapture(0)

while True:
    # Leer un marco de la cámara web
    ret, frame = cap.read()

    # Comprobar si el marco se capturó correctamente
    if not ret:
        print("Error: Falló la captura del marco")
        break

    # Realizar tareas de visión computacional en el marco
    # Por ejemplo, puede aplicar filtros, detectar bordes, etc.

    # Esperar 20 ms antes de procesar el siguiente marco
    cv2.waitKey(20)

    # Salir del bucle si el usuario presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara web y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()