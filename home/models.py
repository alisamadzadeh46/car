from django.db import models
from django.utils.safestring import mark_safe


class Team(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='First Name')
    last_name = models.CharField(max_length=256, verbose_name='Last Name')
    designation = models.CharField(max_length=256)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d/')
    facebook = models.URLField(max_length=128, blank=True)
    twitter = models.URLField(max_length=128, blank=True)
    linkedin = models.URLField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def image_preview(self):
        return mark_safe('<img src="%s" height="50" style="border-radius:50px;"/>' % self.profile_image.url)
    image_preview.short_description = 'Photo'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name='Read')

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.subject}'
