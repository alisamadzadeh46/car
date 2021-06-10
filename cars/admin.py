from django.contrib import admin
from .models import Cars, Images


class CarsImageInline(admin.TabularInline):
    model = Images
    extra = 5


@admin.register(Cars)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'state', 'city', 'year', 'cars_image','is_featured']
    list_filter = ['car_name', 'state', 'city', 'year', 'price', 'fuel_type']
    readonly_fields = ('cars_image',)
    inlines = [CarsImageInline]
    search_fields = ['car_name', 'state', 'city', 'year', 'price', 'fuel_type']
    list_editable = ('is_featured',)


@admin.register(Images)
class Image(admin.ModelAdmin):
    list_display = ['cars', 'name', 'cars_image']
    readonly_fields = ('cars_image',)
