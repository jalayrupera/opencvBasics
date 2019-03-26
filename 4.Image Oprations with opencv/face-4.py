import cv2
import numpy as np

img = cv2.imread('Messi-jugada.jpg', cv2.IMREAD_COLOR)
img[450,450] = [255,255,255]
px = img[450,450]
print(px)

# ROI - REGION OF IMAGE

#img[150:1000, 150:1000] = [255,255,255]

# CREATING NEW SUBIMAGE FROM ROI
watch_face = img[45:750, 42: 150]
img[0:705, 0:108] = watch_face

cv2.imshow('img',img)
cv2.imshow('imge',watch_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
