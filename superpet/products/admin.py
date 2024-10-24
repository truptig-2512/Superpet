from django.contrib import admin
from .models import Products,Category

# Register your models here.
#admin.site.register(Products)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','product_price','product_brand','category']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']
    
admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)