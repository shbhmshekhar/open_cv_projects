import cv2

#print(cv2.__version__) #Ver

#Read, write and show image

#Read
img = cv2.imread('lena.jpg', 1)#read img 0: BnW, 1: color , -1: as it is with alpha
#print(img);
#if(img != None):
cv2.imshow('imgdisplay', img) #showimg img
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('Lena_copy.png',img) #Write Img as file
    cv2.destroyAllWindows()

#Read, Write and show video frm camera
cap = cv2.VideoCapture(0) # Capture videos by specifying index of device OR file name

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(4, 7000)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_XI_FRAMERATE))
#print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()