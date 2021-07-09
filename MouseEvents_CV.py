import cv2
import numpy as np

#list available events
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

#callback fn for mouse event
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print('x:' + x + ' y: ' + y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 0, 0), 1)
        cv2.imshow('image', img)


    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        bgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, bgr, (x, y), font, .5, (255, 0, 255), 1)
        cv2.imshow('image', img)


#img = np.zeros((512, 512), np.uint8) #create a black img using numpy
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()