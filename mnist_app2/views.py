# mnist_app2/views.py
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from tensorflow.keras.models import load_model

# Example view for home page
def index(request):
    return render(request, 'index.html')

# Example prediction view
def predict(request):
    model_path = settings.MODEL_PATH  # Access model path from settings
    model = load_model(model_path)
    # Prediction logic here
    return JsonResponse({"prediction": "result"})
