import numpy as np
import cv2

img = cv2.imread('Messi-jugada.jpg',cv2.IMREAD_GRAYSCALE) //CONVERTS THE COLOR OF THE PICTURE INTO THE GRAY
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imwrite('rey.jpeg',fh) //TO SAVE THE PICTURE
cv2.destroyAllWindows()
