"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
import numpy as np

model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
global keras_model
keras_model = tf.keras.models.load_model(ece386-lab1/server/digits.keras)

# TODO: Create FastAPI App as global variable
global fastAPI


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    gray_img = img.convert("L")
    # TODO: convert image to numpy array of shape model expects
    size = (28, 28)
    return None


# TODO: Define predict POST function
