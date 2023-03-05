from django.contrib import admin
from .models import Product, OrderItem, Order, Customer

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
