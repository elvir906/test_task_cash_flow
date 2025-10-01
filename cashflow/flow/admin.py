from django.contrib import admin
from .models import Post, Status


class PostAdmin(admin.ModelAdmin):
  list_display = ['pub_date', 'status']


class StatusAdmin(admin.ModelAdmin):
  list_display = ['value']


admin.site.register(Post, PostAdmin)
admin.site.register(Status, StatusAdmin)
