import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array


def preprocess_image(image, target_size=(250, 190)):
    """
    Preprocess the image to the required input format for the CNN model.

    :param image: PIL Image instance
    :param target_size: Target size to resize the image (   s250x190)
    :return: Preprocessed image as a NumPy array with shape (1, 250, 190, 1)
    """
    # Convert the image to grayscale as the model expects single-channel input
    image = image.convert("L")

    # Resize the image to the target size (250x190)
    image = image.resize(target_size)

    # Convert the image to a NumPy array
    image = img_to_array(image)

    # Normalize the image to the range [0, 1]
    image = image / 255.0

    # Expand dimensions to match the input shape of the model: (1, 250, 190, 1)
    image = np.expand_dims(image, axis=0)

    return image


def classify_face_shape(model, image):
    """
    Predict the face shape using the pre-trained CNN model.

    :param model: The loaded CNN model
    :param image: Preprocessed image with shape (1, 250, 190, 1)
    :return: Predicted face shape as a string
    """
    # Make predictions using the model
    predictions = model.predict(image)

    # Get the index of the highest probability
    face_shape_idx = np.argmax(predictions, axis=1)[0]

    # Define the mapping of indices to face shape labels
    face_shape_labels = ['heart', 'oblong', 'oval', 'round', 'square']

    return face_shape_labels[face_shape_idx]
