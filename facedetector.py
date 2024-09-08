import cv2
import numpy as np
from PIL import Image

def detect_face(image):
    # Convert PIL image to a format suitable for OpenCV
    open_cv_image = np.array(image.convert('RGB'))
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

    # Load the pre-trained face detector from OpenCV
    face_cascade_path = 'haarcascade_frontalface_default.xml'  # Update this path
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    # Add a confidence threshold to filter out small detections
    faces = [face for face in faces if face[2] > 100 and face[3] > 100]  # Example: only keep faces larger than 100x100 pixels

    if len(faces) == 0:
        return False, None  # No valid face detected

    # Assume the first detected face is the target
    x, y, w, h = faces[0]
    face_image = open_cv_image[y:y + h, x:x + w]


    # Convert the detected face area back to PIL format
    face_image_pil = Image.fromarray(face_image[:, :, ::-1].copy())

    return True, face_image_pil
