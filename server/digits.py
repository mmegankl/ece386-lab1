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
from fastapi import FastAPI
import requests
from typing import Annotated
from fastapi import FastAPI, File, UploadFile

model_path: str = "./server/digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
keras_model = load_model(model_path)

# TODO: Create FastAPI App as global variable
app: FastAPI = FastAPI()


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    gray_img = img.convert("L")
    # TODO: convert image to numpy array of shape model expects
    size = (28, 28)
    gray_img = gray_img.resize(size)
    img_arr = np.array(gray_img)
    return np.expand_dims(img_arr, axis=0)


# TODO: Define predict POST function - post req to predict


@app.post("/predict")
def predict_function(img: Annotated[bytes, File()]):
    processed_img = image_to_np(img)  # convert your image
    prediction = keras_model.predict(processed_img)  # numpy array

    return int(np.argmax(prediction))  # expecting bytes (img)

    # requests.post()
    # return 0
