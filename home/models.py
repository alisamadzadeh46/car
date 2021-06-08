from django.db import models
from django.utils.html import format_html


class Team(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='first name')
    last_name = models.CharField(max_length=256, verbose_name='last name')
    designation = models.CharField(max_length=256, verbose_name='designation')
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d/')
    facebook = models.URLField(max_length=128, verbose_name='facebook')
    twitter = models.URLField(max_length=128, verbose_name='twitter')
    google_plus = models.URLField(max_length=128, verbose_name='google_plus')
    create_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def image(self):
        return format_html('<img src="{}" height="50" style="border-radius:50px;"/>'.format(self.profile_image.url))
