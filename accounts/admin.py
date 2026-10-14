from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'state']
    list_filter = ['city', 'state']
    search_fields = ['user__username', 'user__email', 'phone']
