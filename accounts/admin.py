from django.contrib import admin
from django.contrib.auth.models import User

# User already registered hota hai by default
# Bas customize karte hain
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined']
    search_fields = ['username', 'email']