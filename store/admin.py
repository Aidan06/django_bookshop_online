from django.contrib import admin
from .models import Genre, Book


@admin.register(Genre)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'slug', 'price',
                        'in_stock', 'created', 'updated']
        list_filter = ['in_stock', 'is_active']
        list_editable = ['price', 'in_stock']
        prepopulated_fields = {'slug': ('title',)}

