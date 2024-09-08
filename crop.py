import cv2
# Load the image
image = cv2.imread('images/heart/avoid_1.jpg')
# Define the cropping coordinates (x, y, width, height)
x, y, w, h = 100, 50, 300, 200
# Crop the image
cropped_image = image[y:y+h, x:x+w]
# Define the new size (width, height)
new_size = (150, 100)  # Example: new width = 150, new height = 100
# Resize the cropped image
resized_image = cv2.resize(cropped_image, new_size)
# Save the cropped and resized image
cv2.imwrite('cropped_resized_image.jpg', resized_image)
# Display the cropped and resized
cv2.imshow('Cropped and Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()