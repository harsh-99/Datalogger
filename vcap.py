import numpy as np
import cv2
import datetime
import requests
import time

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('out.avi', 0, 5, (640,480),0)
start=datetime.datetime.now()
while(cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret==True:
        #frame = cv2.flip(frame,0)
        out.write(frame)
        time.sleep(0.2)
        now=datetime.datetime.now()
        if now-start > datetime.timedelta(0, 5, 0):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

'''
url = 'http://shubhagrawal.in/agv_new1.php?'
files = {'file': open('out.avi', 'rb')}
r = requests.post(url, files=files)
'''
