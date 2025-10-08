from django.contrib import admin
# from django_mptt_admin.admin import DjangoMpttAdmin

from .models import (
    Post, Status, FlowType, Category, Subcategory
)


class PostAdmin(admin.ModelAdmin):
    list_display = [
      'pub_date', 'user', 'status', 'flow_type',
      'category', 'amount', 'comment',
  ]


class StatusAdmin(admin.ModelAdmin):
    list_display = ['value',]


class TypeAdmin(admin.ModelAdmin):
    list_display = ['value',]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['value',]

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['value', 'category']


admin.site.register(Post, PostAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(FlowType, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
