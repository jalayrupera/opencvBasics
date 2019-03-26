import cv2
import numpy as np

img = cv2.imread('Messi-jugada.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (140,140),  (190,190), (255,255,255), 20)
cv2.rectangle(img, (140,150), (340,350), (255,0,0), 10)
cv2.circle(img, (970,400), 155, (0,0,255), -1)

poly = np.array([[30,60],[40,190],[450,670],[650,510]],np.int32)
#poly = np.reshape((-1,1,2))
cv2.polylines(img,[poly], True,(0,255,255), 15)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Shrey Vasani', (120,130),font,5,(200,255,200),10, cv2.LINE_AA)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
