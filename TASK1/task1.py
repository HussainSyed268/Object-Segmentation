#task1 code
import cv2

image = cv2.imread('dipassignmentimg.jpg')
resized_image = cv2.resize(image, (256, 256))

cv2.imwrite('resized_image.jpg', resized_image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#END
