from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import (Post,
                     Status,
                     FlowType,
                     Category)


class PostAdmin(admin.ModelAdmin):
  list_display = [
    'pub_date', 'user', 'status', 'flow_type', 'category', 'amount'
  ]


class StatusAdmin(admin.ModelAdmin):
  list_display = ['value']


class TypeAdmin(admin.ModelAdmin):
  list_display = ['value']

class CategoryAdmin(DjangoMpttAdmin):
  list_display = ['value']


admin.site.register(Post, PostAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(FlowType, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
