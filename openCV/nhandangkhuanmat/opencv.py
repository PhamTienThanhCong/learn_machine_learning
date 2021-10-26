import cv2

camera_id = 0

cap =  cv2.VideoCapture(camera_id)

def camera(type_img):
    while True:
        ret, img = cap.read()
        gray_img = cv2.cvtColor(img , type_img)   
        cv2.imshow("camera",gray_img) 
        if cv2.waitKey(1) == ord('f'):
            break


color1 = cv2.COLOR_BGR2GRAY
color2 = cv2.COLOR_BGR2HLS
color3 = cv2.COLOR_BGR2HSV
color4 = cv2.COLOR_BGR2LAB

while True:
    ret, img = cap.read()
    cv2.imshow("camera",img) 
    if cv2.waitKey(1) == ord('f'):
        break

camera(color1)
camera(color2)
camera(color3)
camera(color4)

cap.release()
cv2.destroyAllWindows() 