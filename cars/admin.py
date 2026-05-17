from django.contrib import admin
from .models import Cars, Images, Message


class CarsImageInline(admin.TabularInline):
    model = Images
    extra = 3
    readonly_fields = ['cars_image']


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'model', 'year', 'price', 'city', 'state', 'cars_image', 'is_featured', 'created_data']
    list_filter = ['state', 'city', 'year', 'fuel_type', 'body_style', 'transmission', 'is_featured']
    readonly_fields = ['cars_image', 'created_data', 'updated_at']
    inlines = [CarsImageInline]
    search_fields = ['car_name', 'model', 'city', 'vin_no']
    list_editable = ['is_featured']
    list_per_page = 20


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['cars', 'name', 'cars_image']
    readonly_fields = ['cars_image']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'car_name', 'email', 'phone', 'city', 'create_data']
    list_filter = ['city', 'state', 'create_data']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'car_name']
    list_per_page = 20
    readonly_fields = ['create_data']
