import cv2

image = cv2.imread('./Recursos/figuras.JPG')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,10,150)
canny = cv2.dilate(canny,None,iterations=1)
canny = cv2.erode(canny,None,iterations=1)
cnts,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    x,y,w,h = cv2.boundingRect(approx)
    
    corners = len(approx)
    
    match corners:
        case 3:
            cv2.putText(image,'Triangulo',(x,y-5),1,1,(0,255,0),1)
        case 4:
            aspectRatio = float(w)/h
            if aspectRatio > 0.95 and aspectRatio < 1.05:
                cv2.putText(image,'Cuadrado',(x,y-5),1,1,(0,255,0),1)
            else:
                cv2.putText(image,'Rectangulo',(x,y-5),1,1,(0,255,0),1)
        case 5:
            cv2.putText(image,'Pentagono',(x,y-5),1,1,(0,255,0),1)
        case 6:
            cv2.putText(image,'Hexagono',(x,y-5),1,1,(0,255,0),1)
        case _:
            cv2.putText(image,'Circulo',(x,y-5),1,1,(0,255,0),1)
    
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)