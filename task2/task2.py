#TASK2 CODE
import cv2

image = cv2.imread('resized_image.jpg')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_image.jpg', grayscale_image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#END
