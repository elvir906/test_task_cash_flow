from django.contrib import admin
from .models import Field, Status


class FieldAdmin(admin.ModelAdmin):
  list_display = ['pub_date', 'status']


class StatusAdmin(admin.ModelAdmin):
  list_display = ['value']


admin.site.register(Field, FieldAdmin)
admin.site.register(Status, StatusAdmin)
