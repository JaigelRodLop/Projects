import cv2

image = cv2.imread('./Recursos/rexxar.jpg')

grayscaleImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

resizedImage = cv2.resize(grayscaleImage,None,fx=0.5,fy=0.5)

cv2.imshow('Original Image',image)
cv2.imshow('Grayscale Image', grayscaleImage)
cv2.imshow('Resized Image',resizedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()