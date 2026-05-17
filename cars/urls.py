from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('cars/', views.cars, name='cars'),
    path('cars/<int:id>/', views.car_detail, name='car_detail'),
    path('search/', views.search, name='search'),
]
