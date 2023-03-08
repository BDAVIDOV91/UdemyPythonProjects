import cv2

# Load the image
image = cv2.imread('carinanebula3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours by area (from largest to smallest)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Find the brightest stars
brightest_contours = []
N = 5
for contour in contours[:N]:
    area = cv2.contourArea(contour)
    if area > 1000: # Adjust this threshold to filter out noise
        brightest_contours.append(contour)


# Draw squares around the brightest stars
for contour in brightest_contours:
    # Get the coordinates of the bounding box
    x, y, w, h = cv2.boundingRect(contour)
    
    # Draw a green square around the contour
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


# Display the image with the squares and wait for a key press
num_stars = len(contours)
print(f"Total number of stars: {num_stars}")
cv2.imshow('image', image)
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): # Press 'q' to exit
        break


# Close all windows
cv2.destroyAllWindows()

