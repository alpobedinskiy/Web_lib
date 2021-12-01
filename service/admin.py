from django.contrib import admin

# Register your models here.
from .models import Product, Bin, Home


admin.site.register(Bin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'cost', 'is_active']
    fields = ['id', 'title']
    list_filter = ['cost']
    search_fields = ['title']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['size', 'cost', 'adr', 'bal']
    #fields = ['id', 'title']
    #list_filter = ['cost']
    #search_fields = ['title']
#admin.site.register(Product, ProductAdmin )