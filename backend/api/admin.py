from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

# admin.site.register(usermodel)
admin.site.register(customer)
admin.site.register(address)



class address_admin(admin.ModelAdmin):
    class Meta:
        model:address
        fields = ["name", "title"]

admin.site.register(category)
admin.site.register(product)
admin.site.register(Order)
admin.site.register(cart)



