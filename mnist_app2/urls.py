from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page route
    path('predict/', views.predict, name='predict'),  # Prediction route
]