import cv2
import os

def resize_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            filepath = os.path.join(directory, filename)
            image = cv2.imread(filepath)
            resized_image = cv2.resize(image, (100, 100))
            cv2.imwrite(filepath, resized_image)

resize_images('/home/Desktop/')
