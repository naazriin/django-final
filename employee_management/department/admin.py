from django.contrib import admin

# Register your models here.

from department.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]
    search_fields=['name']
    list_filter=['name']

admin.site.register(Department, DepartmentAdmin)
