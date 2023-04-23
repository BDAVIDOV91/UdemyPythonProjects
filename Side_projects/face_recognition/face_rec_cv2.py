import cv2
import numpy as np

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('model.yml')

# Load images of yourself and create a dictionary of labels
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
labels = [0, 0, 0] # All images are of yourself
face_images = []
for image_path in image_paths:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    for (x, y, w, h) in faces:
        face_images.append(gray[y : y + h, x : x + w])
    
# Train face recognition model
recognizer.train(face_images, np.array(labels))

# Load image uploaded by user
uploaded_image = cv2.imread('uploaded_image.jpg')
gray_uploaded = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

# Detect face in uploaded image
faces = face_cascade.detectMultiScale(gray_uploaded, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

# If face is detected, recognize it
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    face_roi = gray_uploaded[y : y + h, x : x + w]
    label, confidence = recognizer.predict(face_roi)
    if label == 0:
        print('Welcome back!')
    else:
        print('Sorry, you are not authorized.')
