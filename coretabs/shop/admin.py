from django.contrib import admin
from .models import Product,Category
import decimal

# Register your models here.
admin.site.site_header = "Coretabs Online Shop Administration"
admin.site.site_title = "Coretabs Online Shop Administration"
# admin.site.index_title = ""

'''
#List Action Alternative
def discount(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * decimal.Decimal('0.8')
        product.save()


discount.short_description='Apply 20%% DISCOUNT'
'''

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'price', 'stock', 'category',)
    list_filter = ('created_at', 'category',)
    actions = ['discount',]

    # List Action as Model Admin Method
    def discount(self, request, queryset):
        for product in queryset:
            product.price = product.price * decimal.Decimal('0.8')
            product.save()
    discount.short_description = 'Apply 20%% DISCOUNT'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['name']
    list_display = ('name', 'description',)
