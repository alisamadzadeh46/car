from django.urls import path
from .views import *

app_name = 'cars'
urlpatterns = [
    path('cars/', view.cars, name='cars')
]
