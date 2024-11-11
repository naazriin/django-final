from django.contrib import admin

# Register your models here.

from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    search_fields=['name','surname']
    list_filter=['name']


admin.site.register(Employee, EmployeeAdmin)