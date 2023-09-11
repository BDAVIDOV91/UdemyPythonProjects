import cv2
import os
import numpy as np

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load face recognition model
face_recognizer = cv2.face_LBPHFaceRecognizer.create()
face_recognizer.read('model.yml')

# Load labeled images and labels
labeled_images_dir = 'labeled_images'
label_dict = {}
id = 0

# Loop over each subdirectory in the labeled images directory
for label_name in os.listdir(labeled_images_dir):
    label_folder_path = os.path.join(labeled_images_dir, label_name)
    if os.path.isdir(label_folder_path):
        label_dict[id] = label_name
        id += 1

# Function to recognize faces in an image
def recognize_faces_in_image(image_path):
    uploaded_image = cv2.imread(image_path)
    gray_uploaded = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_uploaded, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray_uploaded[y:y + h, x:x + w]
        label_id, confidence = face_recognizer.predict(face_roi)

        if label_id in label_dict:
            recognized_name = label_dict[label_id]
            print(f"Recognized: {recognized_name} (Confidence: {confidence})")

            cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(uploaded_image, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            print(f"Unrecognized label ID: {label_id}")

    cv2.imshow('Image', uploaded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load and recognize faces in uploaded images
image_filenames = ['labeled_images/110.jpg']

for filename in image_filenames:
    recognize_faces_in_image(filename)