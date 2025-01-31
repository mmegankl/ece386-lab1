# Digits Server

1. What the server does
Receives request from the client and utilizes the image derived from its path (from the client). The server then converts the image to the correct format (np.array), resizes and converts to grayscale and puts it through the previously-made keras model. The model returns a np.array of the predictions, and returns to the client the class of the highest confidence.

## Usage

2. Setup and running server
Code aside, we activate/setup fastapi and it gives us an IP address (127.0.0.1) as well as port (8000). Once activated, we can go to the client side for it to request.

