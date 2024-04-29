from django.contrib import admin
from home.models import *
# Register your models here.

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)

admin.site.register(Hotels)

admin.site.register(state)

admin.site.register(Booking)

