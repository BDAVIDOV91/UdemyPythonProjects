import cv2
import time

first_frame = None

# index give the camera option on your pc or video path
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    #converting the picture GRAY and blurry in two windows
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue
    
    #creating the different frames
    delta_frame = cv2. absdiff(first_frame, gray)
    
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        
        #building rectangle in the frame
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3) 
           
        
    #appearing for the frames
    cv2.imshow('Capturing', gray)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Color Frame', frame)

    key = cv2.waitKey(1)
    #use 'q' key to break
    if key == ord('q'):
        break

    
video.release()
cv2.destroyAllWindows