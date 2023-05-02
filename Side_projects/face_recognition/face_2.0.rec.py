import cv2
import numpy as np
import os

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('model.yml')


# Load face images and labels
path = 'labeled_images'
face_images = []
labels = []
confidences = []
label_dict = {}
id = 0

# Loop over each subdirectory in each faces folder
faces_folder_paths = ['labeled_images/bobby', 'labeled_images/aleks', 'labeled_images/marti']

# Loop over each subdirectory in the faces folder
for faces_folder_path in faces_folder_paths:

    # Loop over each subdirectory in the faces folder
    for label_name in os.listdir(faces_folder_path):

        # Get the full path to the label's folder
        label_folder_path = os.path.join(faces_folder_path, label_name)

        # Check if the path is a directory
        if not os.path.isdir(label_folder_path):
            continue

        # Loop over each image in the label's folder
        for filename in os.listdir(label_folder_path):

            # Get the full path to the image file
            image_path = os.path.join(label_folder_path, filename)

            # Check if the path is a file and if it is an image file
            if not os.path.isfile(image_path) or not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            # Get the label ID from the folder name
            label_id = int(label_name)

            # Add the label ID and name to the dictionary
            label_dict[label_id] = label_name

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
                # Make prediction on face image and get confidence value
                face_roi = gray[y : y + h, x : x + w]
                features = face_recognizer.predict(face_roi)
                confidences.append(features[1])

# Train recognizer on face images and labels
face_recognizer.train(face_images, np.array(labels))

# Load images uploaded by user
image_filenames = ['labeled_images/001.jpg']

for filename in image_filenames:
    # Load image
    uploaded_image = cv2.imread(filename)
    # Resize the image to fit in the window
    uploaded_image = cv2.resize(uploaded_image, (0,0), fx=0.5, fy=0.5)
    # Convert to grayscale
    gray_uploaded = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray_uploaded, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
    # Loop over each detected face
    for (x, y, w, h) in faces:
    # Extract the face region of interest (ROI)
        face_roi = gray_uploaded[y:y+h, x:x+w]
        # Recognize the face using the trained recognizer
        features = face_recognizer.predict(face_roi)
        label_id = features[0]
        confidence = features[1]
            
        if label_id in label_dict:
            name = label_dict[label_id]
            print(f"Recognized: {name}")
            # Draw a green rectangle around each face and display the image
            cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(uploaded_image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            print(f"Unrecognized label ID: {label_id}")

        # Show the image
        cv2.imshow('Image', uploaded_image)
        cv2.waitKey(0)

    
# If face is detected, recognize it
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    face_roi = gray_uploaded[y : y + h, x : x + w]
    label, confidence = face_recognizer.predict(face_roi)
    if label == label_dict['bobby']:
        result = 'Recognized: Bobkata!'
    elif label == label_dict['aleks']:
        result = 'It\'s Aleks...She is lovely !'
    elif label == label_dict['marti']:
        result = 'WoW!It\'s the little tornado ! IT\'S MARTI!'
    else:
        result = 'Sorry, you are not authorized.'
    
    # Print the result in the terminal
    print(result)
    
else:
    print('No face detected.')
                
cv2.destroyAllWindows()