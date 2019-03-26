import cv2


Capture = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))


while True:
    ret,frame = Capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
    cv2.imshow('new',gray)
    cv2.imshow('RGB',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


Capture.release()
out.release()
cv2.destroyAllWindows()
