import tensorflow as tf
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from PIL import Image
import io
import base64
import os
from django.conf import settings

# Define the path to your model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'mnist_model.h5')

# Load the pre-trained model once when the server starts
model = tf.keras.models.load_model(MODEL_PATH)

def index(request):
    """
    View to render the page where the user can draw a digit.
    """
    return render(request, 'index.html')

def predict(request):
    """
    View to predict the digit based on the image data sent from the frontend.
    """
    if request.method == 'POST':
        # Get the image data (base64 encoded) from the request
        image_data = request.POST.get('image')
        # Remove the base64 header (the part before the actual base64 data)
        image_data = image_data.split(",")[1]
        
        # Decode the base64 image and convert it into a PIL Image
        img = Image.open(io.BytesIO(base64.b64decode(image_data)))
        # Convert image to grayscale and resize it to 28x28 pixels (MNIST image size)
        img = img.convert('L').resize((28, 28))

        # Convert image to a numpy array and normalize
        img_array = np.array(img).reshape(1, 28, 28, 1) / 255.0

        # Make prediction using the trained model
        predictions = model.predict(img_array)

        # Get the predicted digit (the index of the max value in the prediction)
        predicted_digit = np.argmax(predictions)

        # Return the prediction as a JSON response
        return JsonResponse({'digit': predicted_digit})

    # Return an error if the method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)
