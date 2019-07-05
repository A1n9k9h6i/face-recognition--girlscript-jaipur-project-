#eror at line 26
import cv2
import numpy as np 

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyedetect =  cv2.CascadeClassifier('haarcascade_eye.xml')

sampleNum = 0

uid = int(input('enter user id'))
name = input('Enter your name')

cam = cv2.VideoCapture(0)


while(True):
	ret,img = cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = facedetect.detectMultiScale(gray,1.3,5)


	for(x,y,w,h) in faces:
		sampleNum+=1
		cv2.imwrite('datasets color/data/'+str(uid)+'_'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyedetect.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.waitKey(500)

	cv2.imshow('face',img)
    cv2.imshow('eye',img)
	cv2.waitKey(1)
	if(sampleNum>10):
		break

cam.release()
cv2.destroyAllWindows()