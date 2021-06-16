from django.contrib import admin
from .models import Team, Contact


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'image']
    readonly_fields = ['image', ]
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']
