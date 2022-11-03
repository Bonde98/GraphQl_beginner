from django.contrib import admin

# Register your models here.
from .models import Category, Grocery, Book

admin.site.register(Category)
admin.site.register(Grocery)
admin.site.register(Book)