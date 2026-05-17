from django.contrib import admin
from .models import Team, Contact


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation', 'image_preview']
    readonly_fields = ['image_preview', 'created_at']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'phone', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
