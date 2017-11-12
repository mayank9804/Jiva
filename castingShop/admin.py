from django.contrib import admin
# Register your models here.
from .models import Products,Orders,CustomizeOrders
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description']

    prepopulated_fields = {'slug':('name',)}
admin.site.register(Products,ProductAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','created','company_profit','total_cost']

admin.site.register(Orders,OrdersAdmin)

class CustomOrdersAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','created','company_profit','total_cost','shape']

admin.site.register(CustomizeOrders,CustomOrdersAdmin)
