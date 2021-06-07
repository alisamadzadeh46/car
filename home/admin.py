from django.contrib import admin
from .models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation']
    readonly_fields = ['image',]
