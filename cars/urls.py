from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('cars/', views.cars, name='cars'),
    path('<int:id>/', views.car_detail, name='car_detail')
]
