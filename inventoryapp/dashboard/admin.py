from django.contrib import admin

# Register your models here.
from .models import Product, Order
from django.contrib.auth.models import Group

#admin.site.unregister(Group)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','category','quantity')
    list_filter=  ['category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)