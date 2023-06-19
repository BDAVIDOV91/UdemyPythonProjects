import cv2

# Load the pre-trained Haar cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale for eye detection
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform eye detection
    eyes = eye_cascade.detectMultiScale(grey, scaleFactor = 1.3, minNeighbors = 5)
    
    # Draw rectangles around the detected eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the frame with eye detection
    cv2.imshow('Eye Tracker', frame)

    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()