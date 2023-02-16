from django.contrib import admin

from .models import Country, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'country']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'is_active']
