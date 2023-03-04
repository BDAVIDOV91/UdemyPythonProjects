import cv2
import numpy as np

# Load the astronomical image
image = cv2.imread('astronomical_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to convert the image to binary
_, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and extract the galaxies
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:  # Filter out small contours
        x, y, w, h = cv2.boundingRect(cnt)
        galaxy = image[y:y + h, x:x + w]
        # TODO: Name the galaxy using astronomical databases or other methods


   #This code loads an astronomical image, converts it to grayscale, applies Gaussian blur and thresholding to extract the contours, and loops through the contours to extract the galaxies. The galaxies are extracted by computing the bounding rectangle of each contour and then cropping the image to that rectangle.

  #However, this is just a basic example, and a complete system for identifying and naming galaxies would require much more processing and analysis, including feature extraction and classification using machine learning algorithms.




