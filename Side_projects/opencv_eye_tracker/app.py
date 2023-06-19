import cv2

# Load the pre-trained Haar cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Constants for calibration
calibration_points = [(100, 100), (400, 100), (400, 400), (100, 400)]  # Define the calibration points as per your screen resolution
calibration_index = 0
calibration_complete = False

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform eye detection
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate the center of the eye
        eye_center = (x + w // 2, y + h // 2)

        if calibration_complete:
            # Project the gaze onto the image
            # Perform gaze estimation based on eye movement tracking and calibration data
            # Highlight or overlay the region of interest based on the estimated gaze

            # For demonstration, we'll just display the coordinates of the gaze point
            cv2.putText(frame, f"Gaze Point: {eye_center}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        else:
            # Display calibration point
            cv2.circle(frame, calibration_points[calibration_index], 10, (255, 0, 0), -1)
            cv2.putText(frame, "Calibration", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame with eye detection
    cv2.imshow('Eye Tracker', frame)

    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check for the 'c' key press to calibrate
    if cv2.waitKey(1) & 0xFF == ord('c'):
        if calibration_index < len(calibration_points):
            calibration_index += 1
            if calibration_index == len(calibration_points):
                calibration_complete = True

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()