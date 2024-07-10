from django.urls import path
from .views import *

urlpatterns = [
    path('food_zone/', FoodZoneRegistrationAPIView.as_view()),
    path('it_expo/', ITExpoRegistrationAPIView.as_view())
]