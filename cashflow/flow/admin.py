from django.contrib import admin

from .models import Field

class FieldAdmin(admin.ModelAdmin):
  list_display = ['pub_date', 'status']


admin.site.register(Field, FieldAdmin)
