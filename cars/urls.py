from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('cars/', views.cars, name='cars')
]
