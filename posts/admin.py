from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'header', 'created_at', 'updated_at')
    search_fields = ['user__username', 'header', 'content']

admin.site.register(Post, PostAdmin)
