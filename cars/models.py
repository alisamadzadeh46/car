from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe


class Cars(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
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

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    car_name = models.CharField(max_length=256, verbose_name='car name')
    state = models.CharField(choices=state_choice, max_length=100, verbose_name='state')
    city = models.CharField(max_length=100, verbose_name='city')
    color = models.CharField(max_length=100, verbose_name='color')
    model = models.CharField(max_length=100, verbose_name='model')
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=100, verbose_name='condition')
    price = models.IntegerField(verbose_name='price')
    description = RichTextUploadingField(verbose_name='description')
    image = models.ImageField(blank=False, null=False, upload_to="cars/%Y/%m/%d/")
    features = models.CharField(choices=features_choices, max_length=150, verbose_name='features')
    body_style = models.CharField(max_length=100, verbose_name='body style')
    engine = models.CharField(max_length=100, verbose_name='engine')
    transmission = models.CharField(max_length=100, verbose_name='transmission')
    interior = models.CharField(max_length=100, verbose_name='interior')
    miles = models.IntegerField(verbose_name='miles')
    doors = models.CharField(choices=door_choices, max_length=150, verbose_name='doors')
    passengers = models.IntegerField(verbose_name='passengers')
    vin_no = models.CharField(max_length=150, verbose_name='doors')
    mileage = models.IntegerField(verbose_name='mileage')
    fuel_type = models.CharField(max_length=150, verbose_name='fuel')
    owners = models.CharField(max_length=150, verbose_name='owners')
    is_featured = models.BooleanField(max_length=150, verbose_name='featured')
    created_data = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Cars'
        verbose_name_plural = 'Cars'

    def cars_image(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))


class Images(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="Cars")
    name = models.CharField(max_length=50, blank=True, verbose_name="name")
    image = models.ImageField(blank=True, upload_to="cars/%Y/%m/%d/", verbose_name="image")

    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def cars_image(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    def __str__(self):
        return self.name
