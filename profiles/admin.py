from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_owner', 'other_field', 'another_field')  # Adjust with actual fields

    def get_owner(self, obj):
        return obj.user.username  # Adjust this based on your User model
    get_owner.short_description = 'User'