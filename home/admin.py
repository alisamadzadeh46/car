from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'image']
    readonly_fields = ['image', ]
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation', ]
