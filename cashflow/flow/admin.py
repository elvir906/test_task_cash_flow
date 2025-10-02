from django.contrib import admin
from .models import (Post,
                     Status,
                     FlowType,
                     Category,
                     SubCategory)


class PostAdmin(admin.ModelAdmin):
  list_display = ['pub_date', 'status', 'flow_type', 'category', 'subcategory', 'amount']


class StatusAdmin(admin.ModelAdmin):
  list_display = ['value']


class TypeAdmin(admin.ModelAdmin):
  list_display = ['value']

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['value']

class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ['value']


admin.site.register(Post, PostAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(FlowType, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
