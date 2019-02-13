import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(3,480)
face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

samples = int(input("How many samples?"))
face_id = input('\n Enter id of the new usser and press ENTER ')
print("\n Look at the camera and wait")
# start counting with an offset so you don't overwrite past photos
offset = 626
count = offset
while(True):
	print(count)
	ret, img = cam.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
		count += 1
		# Save faces to dataset
		cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
		cv2.imshow('image', img)
	k = cv2.waitKey(100) & 0xff 
	if k == 27:
		break
	elif count >= samples + offset: 
		break
print("\n Completed. Exiting ")
cam.release()
cv2.destroyAllWindows()