from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Specify fields to display in the admin list view
    list_display = ('name', 'price')
    search_fields = ('name',)  # Add a search bar for the name field
    list_filter = ('price',)  # Add filter options for price

    # Optional: Customizing the form in the admin panel
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'price')
        }),
        ('Additional Information', {
            'fields': ('description',)
        }),
    )
