from django.contrib import admin

# Register your models here.
from .models import Product, Bin


admin.site.register(Bin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'cost']

#admin.site.register(Product, ProductAdmin )