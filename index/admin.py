from django.contrib import admin
from .models import food,Popular_food
# Register your models here.

class foodView(admin.ModelAdmin):
    list_display=[
    'name',
    'hotel_name',
    'location'
    ]

admin.site.register(food,foodView)
admin.site.register(Popular_food)
