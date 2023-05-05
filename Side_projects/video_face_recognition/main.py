import cv2
import threading
from deepface import DeepFace

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 487)

counter = 0
face_match = False
reference_img = cv2.imread('reference02.jpg')

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img.copy())
        if result['verified']:
            face_match = True
        else:
            face_match = False
    except Exception as e:
        print('Error:', e)
        face_match = False
    

while True:
    ret, frame = capture.read()
    
    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target = check_face, args = (frame.copy(), )).start()
            except ValueError:
                pass
            
        counter += 1
        
        if face_match:
            cv2.putText(frame, 'MATCH', (20, 450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, 'NOT MATCH', (20, 450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), 3)
        
        cv2.imshow('video', frame)

                
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
   
cv2.destroyAllWindows() 