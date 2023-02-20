import cv2
import time

# index give the camera option on your pc or video path
video = cv2.VideoCapture(0)
#'f' will show us how many frames we got in the time before we shut it down
f=0

while True:
    f=f+1
    check, frame = video.read()

    print(check)
    print(frame)

    #converting the picture GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #holds camera 3 sec before release (closing)
    #creating windows so we can  appear
    #time.sleep(3)
    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1)
    #use 'q' key to break
    if key == ord('q'):
        break
print(f)
    
video.release()
cv2.destroyAllWindows