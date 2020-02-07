from django.contrib import admin

# Register your models here.
from .models import Driver, Ride

class DriverAdmin(admin.ModelAdmin):
    pass

class RideAdmin(admin.ModelAdmin):
    pass

admin.site.register(Driver,DriverAdmin)
admin.site.register(Ride,RideAdmin)