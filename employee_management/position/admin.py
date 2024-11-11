from django.contrib import admin

# Register your models here.

from position.models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields]
    search_fields=['name']
    list_filter=['salary'] 


admin.site.register(Position, PositionAdmin)