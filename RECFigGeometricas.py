import cv2 # CV2: Biblioteca de Python especializada en imágenes
import numpy as np

image = cv2.imread('./Recursos/fignew.JPG') # Imagen a trabajar
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Escala de grises
canny = cv2.Canny(gray,10,150) # Binarización y construcción de bordes
canny = cv2.dilate(canny,None,iterations=1) # Esta función asegura los perímetros
canny = cv2.erode(canny,None,iterations=1) # para evitar confusiones
cnts,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # Contornos

for c in cnts: # Cuenta los vértices en cada contorno
    
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    x,y,w,h = cv2.boundingRect(approx)
    
    # Definimos una variable para las esquinas para acelerar el proceso
    corners = len(approx)
    
    # Aqui desarrollamos la comparación de esquinas y sus figuras correspondientes
    match corners:
        case 3:
            cv2.putText(image,'Triangulo',(x,y-5),1,1,(0,255,0),1)
        case 4:
            aspectRatio = float(w)/h
            if aspectRatio > 0.95 and aspectRatio < 1.05:
                cv2.putText(image,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
            else:
                cv2.putText(image,'Rectangulo', (x,y-5),1,1,(0,255,0),1)
        case 5:
            cv2.putText(image,'Pentagono',(x,y-5),1,1,(0,255,0),1)
        case 6:
            cv2.putText(image,'Hexagono',(x,y-5),1,1,(0,255,0),1)
        case 8:
            cv2.putText(image,'Octagono',(x,y-5),1,1,(0,255,0),1)
        case 10:
            cv2.putText(image,'Estrella',(x,y-5),1,1,(0,255,0),1)
        case _:
            aspectRatio = float(w)/h
            if aspectRatio > 0.95 and aspectRatio < 1.05:
                cv2.putText(image,'Circulo',(x,y-5),1,1,(0,255,0),1)
            else:
                cv2.putText(image,'Ovalo',(x,y-5),1,1,(0,255,0),1)

    # Muestra la imagen en pantalla y dibuja los contornos
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)
'''
cv2.imshow('canny',canny)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''