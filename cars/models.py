from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


class Cars(models.Model):
    STATE_CHOICES = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'),
        ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'),
        ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
        ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
        ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
        ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
        ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
    )

    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.now().year + 1)]

    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    DOOR_CHOICES = (('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'))

    car_name = models.CharField(max_length=256, verbose_name='Car Name')
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(choices=YEAR_CHOICES)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    image = models.ImageField(upload_to='cars/%Y/%m/%d/')
    features = models.CharField(max_length=500, blank=True,choices=FEATURES_CHOICES)
    body_style = models.CharField(max_length=100, verbose_name='Body Style')
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=DOOR_CHOICES, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=150, verbose_name='VIN')
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=150, verbose_name='Fuel Type')
    owners = models.CharField(max_length=150)
    is_featured = models.BooleanField(default=False, verbose_name='Featured')
    created_data = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ['-created_data']

    def __str__(self):
        return f'{self.car_name} ({self.year})'

    def cars_image(self):
        return mark_safe('<img src="%s" height="50" style="border-radius:5px;"/>' % self.image.url)
    cars_image.short_description = 'Image'


class Images(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='images', verbose_name='Car')
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='cars/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name or f'Image for {self.cars.car_name}'

    def cars_image(self):
        return mark_safe('<img src="%s" height="50"/>' % self.image.url)
    cars_image.short_description = 'Preview'


class Message(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='First Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    car = models.ForeignKey(Cars, related_name='messages', on_delete=models.CASCADE)
    customer_need = models.CharField(max_length=200, verbose_name='Customer Need')
    car_name = models.CharField(max_length=200, verbose_name='Car Name')
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    create_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-create_data']

    def __str__(self):
        return f'{self.first_name} {self.last_name} — {self.car_name}'
