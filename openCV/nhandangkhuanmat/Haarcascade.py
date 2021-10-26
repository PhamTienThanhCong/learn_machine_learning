import cv2

face     = cv2.CascadeClassifier('nhandangkhuanmat/haarcascade_frontalface_default.xml')
simle    = cv2.CascadeClassifier('nhandangkhuanmat/haarcascade_smile.xml')
font = cv2.FONT_HERSHEY_COMPLEX


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray_img)
    if (len(faces) > 0):
        for (x,y,w,h) in faces:
            img_face = img[y:y+w,x:x+h]
            the_smiles = simle.detectMultiScale(img_face)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            if (len(the_smiles) > 0):
                for (x1,y1,w1,h1) in the_smiles:
                    if (y1*2>h and w1*7>w*2):
                        cv2.rectangle(img,(x1+x,y1+y),(x1+w1+x,y1+h1+y),(0,0,255),2)
                        img = cv2.putText(img, 'please wear KhauTrang', (50,100), font, 1.3, (0,0,255), 2, cv2.LINE_AA)
            else:
                        img = cv2.putText(img, 'Thanks you', (190,100), font, 1.3, (0,255,0), 2, cv2.LINE_AA)
    else:
                        img = cv2.putText(img, 'welcome', (200,100), font, 1.3, (0,255,0), 2, cv2.LINE_AA)


    #cv2.imshow('video',img_face)
    cv2.imshow('video',img)
    if cv2.waitKey(1) == ord('f'):
        break

cap.release()
cv2.destroyAllWindows


# font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
        # for box in faces:
        #     x1,y1,width,height=box
        #     x2,y2=x1+width,y1+height
        #     cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)