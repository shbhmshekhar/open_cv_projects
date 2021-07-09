import cv2

img = cv2.imread('messi5.jpg')

'''print(img.shape) #return tuple of no of rows, colmns 7 channels
print(img.size) #returns total no of px is accessed
print(img.dtype) # returns img dataType'''

points = []

def getCoord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        if len(points) >= 2:
            [x1] = points[-1]
            (x2, y2) = points[-2]

            print(points)

b,g,r = cv2.split(img)

img = cv2.merge((b, g, r))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()