import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
f = open("output.csv","w")
f.write("t,x,y\n")
start = time.time()

while(True):
	ret, frame = cap.read()

	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	low_color = np.array([160, 75, 75])
	upper_color = np.array([180, 255, 255])

	ex_img = cv2.inRange(hsv,low_color,upper_color)

	x = np.argmax(np.sum(ex_img,axis=0))
	y = np.argmax(np.sum(ex_img,axis=1))

	t = time.time() - start
	f.write(str(t)+","+str(x)+","+str(y)+"\n")
	print(str(t)+","+str(x)+","+str(y)+"\n")

	cv2.circle(frame,(x,y),10,(0,255,0))

	cv2.imshow('frame',frame)

	if t > 120:
		break

	key = cv2.waitKey(1) & 0xFF

	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
f.close()