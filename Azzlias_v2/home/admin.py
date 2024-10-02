from django.contrib import admin
from .models import *

# Inline display of products in the Category view
class ProductInline(admin.TabularInline):
    model = Product
    extra = 1  # Number of empty forms to display for adding products directly within the category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Show category name and slug
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name
    search_fields = ['name']  # Add search functionality for category names
    inlines = [ProductInline]  # Inline display of related products in the category admin


admin.site.register(BestSeller)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'fabric_type', 'color', 'stock', 'date_added')
    list_filter = ('category', 'fabric_type', 'color')
    search_fields = ['name', 'category__name']
    list_editable = ('price', 'stock')
    prepopulated_fields = {'slug': ('name',)}  # Auto-populate the slug from name
    readonly_fields = ('date_added',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'price', 'discount_price', 'meesho_affiliate_link','amazon_affiliate_link', 'image', 'slug')
        }),
        ('Product Information', {
            'fields': ('fabric_type', 'sizes', 'color', 'stock')
        }),
        ('Other Details', {
            'fields': ('date_added',)
        }),
    )
    inlines = [ProductImageInline]  # Add the inline for product images


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)