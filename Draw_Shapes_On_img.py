import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)

img = np.zeros([512, 512, 3], np.uint8)


#Draw a line on img
img = cv2.arrowedLine(img, (0,0),  (255, 255), (255, 56, 110), 10)
img = cv2.rectangle(img, (255, 255), (500,  500), (0, 0, 255), 5)
img = cv2.circle(img, (255, 255), 80, (130, 120, 110), -1)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (0, 500), font, 2, (100, 100, 255), 4, cv2.LINE_AA)


cv2.imshow('imgViewer', img)

cv2.waitKey(0)
cv2.destroyAllWindows()