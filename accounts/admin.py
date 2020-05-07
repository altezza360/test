from django.contrib import admin
from .models import Specialist,  Product, Order, Manager, Customer

admin.site.register(Specialist)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(Customer)
