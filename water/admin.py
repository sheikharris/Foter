from django.contrib import admin
# Register your models here.
from .models import owners,owners_temp


admin.site.register(owners)
admin.site.register(owners_temp)
