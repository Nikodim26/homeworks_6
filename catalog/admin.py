from django.contrib import admin

from catalog.models import Category, Product
from users.models import User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ('name','description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price','category')
    list_filter = ('category',)
    search_fields = ('name','description')

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','email','phone_number')
    search_fields = ('email','phone_number')