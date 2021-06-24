from django.contrib import admin

from .models import *


@admin.register(Desktop,Mobiles,Laptop)

class ViewAdmin(admin.ModelAdmin):
    pass






