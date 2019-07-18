from django.contrib import admin
from order.models import LoginModel, Order, FoodItem,FoodClass

# Register your models here.
admin.site.register(LoginModel)
admin.site.register(Order)
admin.site.register(FoodItem)
admin.site.register(FoodClass)