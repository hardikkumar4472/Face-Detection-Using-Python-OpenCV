import cv2
a=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
b=cv2.VideoCapture(0) #For camera input
while True:
    c_rec,d_img=b.read()
    e=cv2.cvtColor(d_img,cv2.COLOR_BGR2GRAY)
    f=a.detectMultiScale(e,1.3,6)
    for (x,y,w,h) in f:
        cv2.rectangle(d_img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',d_img)
    h= cv2.waitKey(40) & 0xFF
    if h==40:
        break
b.release()
cv2.destroyAllWindows()
