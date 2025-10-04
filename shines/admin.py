from django.contrib import admin
from .models import Service, Booking, Join_Us

# Register your models here.
admin.site.register(Service)
admin.site.register(Booking)    
admin.site.register(Join_Us)