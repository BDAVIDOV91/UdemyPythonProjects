import cv2
import numpy as np
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load face images and labels
path = 'labeled_images'
face_images = []
labels = []
label_dict = {}
id = 0

for dirname in os.listdir(path):
    if not os.path.isdir(os.path.join(path, dirname)):
        continue
    label = dirname
    if label not in label_dict:
        label_dict[label] = id
        id += 1
        
    for filename in os.listdir(os.path.join(path, dirname)):
        if filename.endswith('.jpg'):
            image = cv2.imread(os.path.join(path, dirname, filename))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
            for (x, y, w, h) in faces:
                face_images.append(gray[y : y + h, x : x + w])
                labels.append(label_dict[label])
    
# Train face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(face_images, np.array(labels, dtype = np.int32))

# Save the trained model to a file
recognizer.write('model.yml')

# Load image uploaded by user
uploaded_image = cv2.imread('labeled_images/11.jpg')
gray_uploaded = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)
recognizer.read('model.yml')


# Detect face in uploaded image
faces = face_cascade.detectMultiScale(gray_uploaded, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

# If face is detected, recognize it
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    face_roi = gray_uploaded[y : y + h, x : x + w]
    label, confidence = recognizer.predict(face_roi)
    if label == 0:
        print('I recognized you, Bobby!')
    else:
        print('Sorry, you are not authorized.')
