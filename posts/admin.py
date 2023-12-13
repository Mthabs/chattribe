from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'get_owner', 'created_at')  # Assuming 'user' is a ForeignKey in your Post model

    def get_owner(self, obj):
        return obj.owner.username  # Adjust this based on your User model
    get_owner.short_description = 'User'
