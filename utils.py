from tensorflow.keras.preprocessing import image
import numpy as np


def preprocess_image(image: Image.Image, target_size=(224, 224)) -> np.ndarray:
    """
    Preprocess the input image to be suitable for model prediction.

    Args:
    - image: PIL Image object, the image to preprocess.
    - target_size: tuple, the size to which the image should be resized.

    Returns:
    - preprocessed_image: np.ndarray, the processed image ready for prediction.
    """
    # Convert image to grayscale
    image = image.convert('L')

    # Resize image
    image = image.resize(target_size)

    # Convert image to array
    image_array = np.array(image)

    # Normalize the pixel values
    image_array = image_array / 255.0

    # Expand dimensions to match the input shape required by the model
    preprocessed_image = np.expand_dims(image_array, axis=-1)  # Adding channel dimension for grayscale

    return np.expand_dims(preprocessed_image, axis=0)
